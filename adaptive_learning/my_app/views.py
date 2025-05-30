from collections import defaultdict
import os
from datetime import timezone
from .ML.ncdm_inference import load_model, predict
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Assessment, Question, Student, AssessmentResponse, Option, VideoModule, Subtopic, Progress, Topic, \
    VideoProgress, ExperimentAssessmentScore
import logging
import numpy as np
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
import pandas as pd
from huggingface_hub import InferenceClient
from my_app.chatbot_utils import get_chatbot_resources
from dotenv import load_dotenv
import requests
load_dotenv()


BASE_DIR = settings.BASE_DIR
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'my_app/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Manually authenticate user using email instead of username
        print(f"Attempting to authenticate user: {email}")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print(f"Authentication successful: {user.email}")
            login(request, user)
            messages.success(request, f"Welcome back, {email}!")
            return redirect('home')  # Redirect to success page after login
        else:
            print("Authentication failed")
            messages.error(request, "Invalid email or password.")
    return render(request, 'my_app/login.html')



def signup_view(request):
    if request.method == 'POST':
        # Fetch form data (removed 'username' and adjusted fields as per your student model)
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        uga_id = request.POST.get('uga_id')  # New field for student info
        class_level = request.POST.get('class_level')  # New field for student info
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')  # New field for student info
        is_english_first_language = request.POST.get('is_english_first_language')  # New field for student info
        science_experience = request.POST.get('science_experience')  # New field for student info

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        # Create a new user (without username)
        try:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()  # Save the user to the database

            # Create a corresponding Student entry
            student = Student.objects.create(
                user=user,
                uga_id=uga_id,
                first_name=first_name,
                last_name=last_name,
                class_level=class_level,
                gender=gender,
                is_english_first_language=is_english_first_language,
                science_experience=science_experience
            )

        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect('signup')

        # Authenticate the user after creating the user and student entry
        user = authenticate(request, username=email, password=password)  # Authenticate with email

        if user is not None:
            login(request, user)  # Log in the user after authentication
            messages.success(request, "Account created and logged in successfully!")
            return redirect('home')  # Redirect to the home page
        else:
            messages.error(request, "Authentication failed!")
            return redirect('signup')

    return render(request, 'my_app/signup.html')  # Render the signup page



def success_view(request):
    return render(request, 'my_app/success.html')



@login_required
def home_view(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        return render(request, 'my_app/home.html', {'username': request.user.student.first_name})
    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')



@login_required
def test_view(request, topic_id, subtopic_id):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        topic = get_object_or_404(Topic, topic_id=topic_id)
        subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

        # Fetch related module
        module = VideoModule.objects.filter(topic=topic).first()
        if not module:
            return HttpResponse("No associated module found for this topic.", status=400)

        # Fetch the student's progress for this subtopic (record must already exist)
        student_progress = Progress.objects.filter(
            student=student,
            current_subtopic=subtopic
        ).first()

        if not student_progress:
            return HttpResponse("Progress record not found. Ensure progress is created in the module view.", status=400)

        # Determine if video link should be loaded
        load_video_link = not student_progress.video_watched

        # Determine assigned value based on video_watched and score_before
        if student_progress.video_watched and student_progress.score_before is not None:
            assigned_value = 1
        else:
            assigned_value = 0

        # print("Assigned Value - ", assigned_value)

        questions = Question.objects.filter(topic=topic, subtopic=subtopic, assigned_at=assigned_value)

        context = {
            'topic': topic,
            'subtopic': subtopic,
            'questions': questions,
            'username': request.user.student.first_name,
            'assigned_video': student_progress.video_watched,
            'load_video_link': load_video_link,  # Include this flag in the context
        }

        return render(request, 'my_app/test.html', context)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required
def submit_test(request, topic_id, subtopic_id):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        if request.method == "POST":
            print("Form Submitted: ", request.POST)  # Debugging line

            if not request.POST:
                print("No data received in POST request.")
                return JsonResponse({"error": "No data received"}, status=400)

            try:
                topic = get_object_or_404(Topic, topic_id=topic_id)
                subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

                # Create an assessment entry
                assessment = Assessment.objects.create(
                    student=student,
                    topic=topic,
                    subtopic=subtopic,
                    date_taken=timezone.now()
                )

                correct_count = 0
                total_questions = 0
                assigned_at_0_count = 0
                assigned_at_1_count = 0

                question_ids_list = []
                correctness_list = []

                # print(BASE_DIR)
                TCE_Misunderstanding_path = os.path.join(BASE_DIR, 'my_app', 'ML', 'TCE_Misunderstanding.xlsx')

                # print(BASE_DIR)
                # print("Excel file path - ", TCE_Misunderstanding_path)

                tce_misunderstanding = pd.read_excel(TCE_Misunderstanding_path)
                knowledge_n = tce_misunderstanding.shape[1] - 1


                for key, value in request.POST.items():
                    if key.startswith("question_"):
                        question_id = key.split("_")[1]
                        question = get_object_or_404(Question, pk=question_id)
                        selected_option = get_object_or_404(Option, pk=value)

                        # Save response
                        AssessmentResponse.objects.create(
                            assessment=assessment,
                            question=question,
                            selected_option=selected_option
                        )
                        # if question.question_id - 39 >= 1 and question.question_id - 39 <= 1:
                        #     question.question_id = question.question_id - 39
                        # else:
                        #     question.question_id = (question.question_id - 39) / 2
                        # # Track question ID
                        # print("Question ID - ", question.question_id)
                        # if question.assigned_at == 0:
                        question_ids_list.append(question.question_id - 39)
                            # print("Question ID - ", question.question_id)
                        # else:
                            # print(f"Skipping question ID {question.question_id} as assigned_at = {question.assigned_at}")
                        # Check correctness
                        if selected_option.is_correct:
                            correct_count += 1
                            correctness_list.append(1)
                        else:
                            correctness_list.append(0)

                        total_questions += 1

                        # Track assigned_at values
                        if question.assigned_at == 0:
                            assigned_at_0_count += 1
                        elif question.assigned_at == 1:
                            assigned_at_1_count += 1

                # Calculate score
                print("correct_count", correct_count)
                print("total_questions", total_questions)
                score = (correct_count / total_questions) * 100 if total_questions > 0 else 0

                assessment.score = score
                assessment.save()

                answers_df = pd.DataFrame({
                    "question_id": question_ids_list,
                    "correct": correctness_list
                })

                print(answers_df)
                model_path = os.path.join(BASE_DIR, 'my_app', 'ML', 'ncdm_model.pth')
                num_questions = answers_df.shape[0]
                device = "cpu"

                model = load_model(model_path, knowledge_n, num_questions, 1, device)

                misconception_matrix = tce_misunderstanding
                print(question_ids_list)

                weak_knowledge_indices = set()

                for que in question_ids_list:
                    try:
                        # Fetch the knowledge embedding for this specific question
                        item_id = f"Item_{que}"  # construct the matching string

                        question_row = misconception_matrix[misconception_matrix['item_id'] == item_id]


                        if question_row.empty:
                            print(f"Question ID {que} not found in misunderstanding matrix.")
                            continue

                        # Extract the knowledge vector from the row (skipping question_id column)
                        knowledge_vector = question_row.iloc[0, 1:].to_numpy(dtype=float).reshape(1, -1)

                        # Predict using the model
                        prediction, proficiency_vector  = predict(model, student.student_id, int(que), knowledge_vector, device)

                        print(f"\nQuestion ID: Q{que}")
                        print(f"Prediction: {prediction:.4f}")
                        print(f"Proficiency Vector: {proficiency_vector}")

                        knowledge_vector_np = np.array(knowledge_vector).flatten()

                        active_knowledge_indices = np.where(knowledge_vector_np == 1)[0]

                        selected_proficiencies = proficiency_vector[active_knowledge_indices]

                        # If answer is correct do we need to show him the video
                        for idx in active_knowledge_indices:
                            prof_value = proficiency_vector[idx]

                            if prof_value > 0.6:
                                weak_knowledge_indices.add(idx)
                                print(f"High misconception likelihood: prof={prof_value:.4f} → Added idx {idx + 1 } from Q{que}")

                            elif 0.4 <= prof_value <= 0.6:
                                if correctness_list[question_ids_list.index(int(que))] == 0:  # Student answered incorrectly
                                    weak_knowledge_indices.add(idx)
                                    print(
                                        f"Moderate prof + incorrect answer: prof={prof_value:.4f} → Added idx {idx + 1 } from Q{que}")
                                else:
                                    print(
                                        f"Moderate prof + correct answer: prof={prof_value:.4f} → Not Added idx {idx + 1 } from Q{que}")
                            elif prediction < 0.7:
                                weak_knowledge_indices.add(idx)
                                # print(f"Low prediction ({prediction:.4f}) → Added idx {idx + 1 } from Q{que}")

                            elif prof_value < 0.48:
                                print(
                                    f"Low misconception probability (prof={prof_value:.4f}) → Skipped idx {idx + 1 } for Q{que}")

                            else:
                                print(f"No condition met for prof={prof_value:.4f}, idx {idx + 1 }, Q{que}")

                    except Exception as e:
                        print(f"Prediction error for Q{que}: {e}")

                weak_knowledge_indices = sorted([int(idx) + 1 for idx in weak_knowledge_indices])

                print("Final Weak Knowledge Indices:", weak_knowledge_indices)

                try:
                    misconception_videos = VideoModule.objects.filter(subtopic=subtopic)

                    print(" misconception_videos :", misconception_videos)


                    for video in misconception_videos:
                        if video.subtopic == subtopic:
                            try:
                                # Assuming misconceptions are stored as comma-separated values in a CharField
                                video_misconceptions = [
                                    int(m.strip()) for m in video.misconceptions.split(',') if m.strip().isdigit()
                                ]

                                # Get intersection between video misconceptions and weak knowledge indices
                                matched_misconceptions = list(set(video_misconceptions) & set(weak_knowledge_indices))
                                print("matched_misconceptions - ", matched_misconceptions)

                                if matched_misconceptions:
                                    print(f"\n[Video Match] Video: '{video.title}' (ID: {video.video_module_id})")
                                    print(f"  → Related to misconceptions: {matched_misconceptions}")

                                    # Create a VideoProgress record only once for this video
                                    obj, created = VideoProgress.objects.get_or_create(
                                        student=student,
                                        video=video,
                                        subtopic=subtopic,
                                        defaults={"watched": False}
                                    )
                                    if created:
                                        print("  → VideoProgress created.")
                                    else:
                                        print("  → VideoProgress already exists. Skipping creation.")

                            except Exception as inner_e:
                                print(f"Error processing video ID {video.video_module_id if video else 'Unknown'}: {inner_e}")

                            else:
                                print("No Video for the given misconceptions found.")

                except Exception as e:
                    print("Error while assigning videos based on misconceptions:", e)

                # Update progress model
                progress = Progress.objects.filter(student=student, current_subtopic=subtopic).first()
                if progress:
                    if assigned_at_0_count > 0:
                        progress.score_before = score
                        progress.completion_status = "In Progress"
                    if assigned_at_1_count > 0:
                        progress.score_after = score
                        progress.completion_status = "Completed"

                    progress.save()

                # Redirect to the test results page
                return redirect('test_results', topic_id=topic_id, subtopic_id=subtopic_id)

            except Exception as e:
                print("Error:", e)
                return JsonResponse({"error": str(e)}, status=400)

        return redirect("modules")  # Redirect if accessed incorrectly

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name



@login_required
def modules_view(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        # return render(request, 'my_app/home.html', {'username': request.user.student.first_name})
        topics = Topic.objects.all()
        topic_data = []

        for topic in topics:
            # Get all completed subtopics for this student and topic
            completed_subtopics = list(Progress.objects.filter(
                student=student,
                current_topic=topic,
                completion_status='Completed'
            ).values_list('current_subtopic__subtopic_name', flat=True))

            # Get the latest progress for this topic
            progress = Progress.objects.filter(student=student, current_topic=topic).order_by('-last_accessed').first()

            if progress:
                current_subtopic = progress.current_subtopic

                # Check if the current subtopic is completed before creating progress for the next one
                if progress.completion_status == 'Completed':
                    next_subtopic = Subtopic.objects.filter(
                        topic=topic,
                        subtopic_order_number__gt=current_subtopic.subtopic_order_number
                    ).order_by('subtopic_order_number').first() if current_subtopic else None

                    if next_subtopic:
                        next_progress = Progress.objects.filter(
                            student=student,
                            current_topic=topic,
                            current_subtopic=next_subtopic
                        ).first()

                        if not next_progress:
                            # Create progress for the next subtopic
                            new_progress = Progress.objects.create(
                                student=student,
                                current_topic=topic,
                                current_subtopic=next_subtopic,
                                next_subtopic=Subtopic.objects.filter(
                                    topic=topic,
                                    subtopic_order_number__gt=next_subtopic.subtopic_order_number
                                ).order_by('subtopic_order_number').first(),
                                module=VideoModule.objects.filter(subtopic=current_subtopic).first(),
                                completion_status='not_started',
                                video_watched=False
                            )
                            progress = new_progress

                        # Add to topic_data (added completed_subtopics)
                        topic_data.append({
                            'topic': topic,
                            'subtopic': progress.current_subtopic,
                            'completed_subtopics': completed_subtopics
                        })

                    else:
                        progress.completion_status = 'Completed'
                        progress.save()

                        # Add to topic_data (added completed_subtopics)
                        topic_data.append({
                            'topic': topic,
                            'subtopic': None,
                            'completed_subtopics': completed_subtopics
                        })

                else:
                    # If current subtopic is not complete, do not create next subtopic progress
                    topic_data.append({
                        'topic': topic,
                        'subtopic': progress.current_subtopic,
                        'completed_subtopics': completed_subtopics
                    })

            else:
                # If no progress exists, start from the first subtopic
                first_subtopic = Subtopic.objects.filter(topic=topic).order_by('subtopic_order_number').first()
                if first_subtopic:
                    progress = Progress.objects.create(
                        student=student,
                        current_topic=topic,
                        current_subtopic=first_subtopic,
                        next_subtopic=Subtopic.objects.filter(
                            topic=topic,
                            subtopic_order_number__gt=first_subtopic.subtopic_order_number
                        ).order_by('subtopic_order_number').first(),
                        module=VideoModule.objects.filter(topic=topic).first(),
                        completion_status='not_started'
                    )


                topic_data.append({
                    'topic': topic,
                    'subtopic': progress.current_subtopic if progress else None,
                    'completed_subtopics': completed_subtopics
                })

        context = {
            'topic_data': topic_data,
            'username': request.user.student.first_name
        }
        # print("Context - ", context)  # Debug Output

        return render(request, 'my_app/modules.html', context)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required
def test_results(request, topic_id, subtopic_id):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        try:
            topic = get_object_or_404(Topic, topic_id=topic_id)
            subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

            assessment = Assessment.objects.filter(student=student, topic=topic).order_by("-date_taken").first()
            if not assessment:
                return JsonResponse({"error": "No assessment data found for this topic."}, status=404)

            # Fetch responses for the assessment
            responses = AssessmentResponse.objects.filter(assessment=assessment)
            score = assessment.score

            # Fetch video modules from VideoProgress instead of VideoModule directly
            # print(subtopic)
            video_progress_entries = VideoProgress.objects.filter(student=student, subtopic=subtopic)
            # print("Video - test results - ", video_progress_entries)

            video_data = []
            video_url = None
            progress = Progress.objects.filter(student=student, current_subtopic=subtopic).first()
            # print("Progress - ", progress)

            if not video_progress_entries.exists() and progress:
                progress.video_watched = True
                progress.save()

            for entry in video_progress_entries:
                if not entry.watched:
                    video_module = entry.video
                    video_url = video_module.url if video_module and progress and not progress.score_after else None
                    # print("Video URL - ", video_url)

                    if video_url:
                        if "drive.google.com/file/d/" in video_url:
                            file_id = video_url.split('/d/')[1].split('/')[0]
                            video_url = f"https://drive.google.com/file/d/{file_id}/preview"

                        video_data.append({
                            "id": video_module.video_module_id,
                            "title": video_module.title,
                            "url": video_url
                        })

            context = {
                "student_name": f"{student.first_name} {student.last_name}",
                "topic": topic,
                "subtopic": subtopic,
                "score": score,
                "date_taken": assessment.date_taken,
                "responses": responses,
                "video_data": video_data,
                "video_url": video_url,
                "student_id": student.student_id,
                "score_after": progress.score_after if progress else None,
            }

            return render(request, "my_app/test_results.html", context)

        except Exception as e:
            print("Error in test_results:", e)
            return JsonResponse({"error": str(e)}, status=400)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required
def learning_video(request, topic_id, subtopic_id):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        try:
            # print(f"Received topic_id: {topic_id}, subtopic_id: {subtopic_id}")

            student = get_object_or_404(Student, user=request.user)
            topic = get_object_or_404(Topic, topic_id=topic_id)
            subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

            # Fetch videos linked to the subtopic
            video_progress_entries = VideoProgress.objects.filter(student=student, subtopic=subtopic)
            # print("video_progress_entries - ", video_progress_entries)
            video_data = []
            for entry in video_progress_entries:
                video = entry.video
                video_url = video.url

                # print("Inside For Loop")

                if "drive.google.com/file/d/" in video_url:
                    file_id = video_url.split('/d/')[1].split('/')[0]
                    video_url = f"https://drive.google.com/file/d/{file_id}/preview"

                video_data.append({
                    'id': video.video_module_id,
                    'title': video.title,
                    'url': video_url
                })

            # print("video_data - ", video_data)

            context = {
                "topic": topic,
                "subtopic": subtopic,
                "video_data": video_data,
                "subtopic_id": subtopic_id,
                "student_id": student.student_id,
            }

            return render(request, "my_app/learning_video.html", context)

        except Exception as e:
            print("Error in learning_video:", e)
            return JsonResponse({"error": str(e)}, status=400)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name



@login_required
def video_module_view(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
    # Fetch all VideoModules
        video_modules = VideoModule.objects.all()

        context = {
            'video_modules': video_modules
        }

        return render(request, 'my_app/learning_video.html', context)
    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required
def profile_update_view(request):
    student = get_object_or_404(Student, user=request.user)  # Get the student object based on the logged-in user

    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        class_level = request.POST.get('class_level')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate that class_level is provided
        if not class_level:
            messages.error(request, "Class level cannot be empty.")
            return redirect('profile_update')

        # Check if the passwords match
        if password:
            if password != confirm_password:
                messages.error(request, "Passwords do not match.")
                return redirect('profile_update')

            # If password is provided and confirmed, hash and save it
            request.user.set_password(password)
            request.user.save()  # Save the updated user password

            # Since the password has been changed, the user will need to log in again
            messages.success(request, "Your password has been updated. Please log in again.")
            return redirect('login')  # Redirect to the login page after password change

        # If password is not changed, proceed with updating other fields
        student.first_name = first_name
        student.last_name = last_name
        student.class_level = class_level
        student.save()  # Save updated student info

        messages.success(request, "Your profile has been updated successfully.")
        return redirect('home')  # Redirect to the home page

    return render(request, 'my_app/profile_update.html', {'student': student})


def student_assignments_view(request):

    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        progress_data = Progress.objects.filter(student=student).select_related(
            'current_subtopic__topic'
        ).order_by('-last_accessed')

        grouped_data = defaultdict(lambda: {'subtopics': [], 'before': [], 'after': []})
        sorted_progress_data = sorted(progress_data, key=lambda p: p.progress_id)  # or p.progress_id if that's the actual attribute name

        for p in sorted_progress_data:
            if p.current_subtopic:
                topic = p.current_subtopic.topic.topic_name
                grouped_data[topic]['subtopics'].append(p.current_subtopic.subtopic_name)
                grouped_data[topic]['before'].append(float(p.score_before) if p.score_before is not None else 'null')
                grouped_data[topic]['after'].append(float(p.score_after) if p.score_after is not None else 'null')

        context = {
            'progress_data': sorted_progress_data,
            'username': student.first_name,
            'grouped_chart_data': dict(grouped_data),
        }

        return render(request, 'my_app/student_assignments.html', context)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name

@csrf_exempt
@login_required
def update_video_progress(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        if request.method == 'POST':
            # Parse the incoming data (subtopic ID, student ID)
            data = json.loads(request.body.decode('utf-8'))
            subtopic_id = data.get('subtopic_id')
            student_id = data.get('student_id')

            try:
                # Fetch the subtopic and associated topic from the database
                subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id)
                topic = subtopic.topic  # Access the related topic

                # Update or create the progress entry for the student and subtopic
                progress, created = Progress.objects.update_or_create(
                    student_id=student_id,
                    current_subtopic_id=subtopic_id,  # Update with correct field
                    defaults={'video_watched': True}
                )

                # Return a JSON response with the topic and subtopic names to facilitate the redirect
                return JsonResponse({
                    'status': 'success',
                    'message': 'Progress updated.',
                    'topic_name': topic.topic_name,  # Ensure you include the topic name
                    'subtopic_name': subtopic.subtopic_name  # Include the subtopic name
                })

            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required
def complete_video(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        print("Inside the complete_video")
        if request.method == 'POST':
            try:
                # Parse the JSON request data
                data = json.loads(request.body)
                video_id = data.get('video_id')
                subtopic_id = data.get('subtopic_id')

                # Get the student object from the logged-in user
                student = get_object_or_404(Student, user=request.user)

                # Get the subtopic and video
                subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id)
                video = get_object_or_404(VideoModule, video_module_id=video_id, subtopic=subtopic)

                # Try to get the VideoProgress entry; raise an exception if not found
                try:
                    video_progress = VideoProgress.objects.get(
                        student=student, video=video, subtopic=subtopic
                    )
                except VideoProgress.DoesNotExist:
                    raise Exception(f"VideoProgress entry not found for student {student.student_id}, video {video.video_module_id}, subtopic {subtopic.subtopic_id}")

                print(f"DEBUG: VideoProgress entry found for student {student.student_id}, video {video.video_module_id}, subtopic {subtopic.subtopic_id}")
                # print(video_progress)

                # If the video hasn't been watched already, mark it as watched
                if not video_progress.watched:
                    # print("inside if")
                    video_progress.watched = True
                    video_progress.watched_at = timezone.now()
                    video_progress.save()

                    # Check if all videos for this subtopic are watched
                    total_videos = VideoProgress.objects.filter(subtopic=subtopic, student=student).count()
                    # print(f"DEBUG: Total videos for subtopic {subtopic_id}: {total_videos}")
                    watched_videos = VideoProgress.objects.filter(
                        student=student, subtopic=subtopic, watched=True
                    ).count()
                    # print(f"DEBUG: Watched videos for subtopic {subtopic_id}: {watched_videos}")

                    if watched_videos == total_videos:
                        progress = student.progress_set.filter(current_subtopic=subtopic).first()
                        if progress:
                            progress.video_watched = True
                            progress.save()
                            print(f"DEBUG: All videos watched for subtopic {subtopic_id}. Progress updated.")
                        else:
                            print(f"DEBUG: No progress record found for subtopic {subtopic_id} for student {student}.")

                    return JsonResponse({"success": True, "message": "Video marked as watched"})
                else:
                    return JsonResponse({"success": False, "message": "Video already watched"})

            except Exception as e:
                print(f"Error in complete_video: {e}")
                return JsonResponse({"success": False, "message": str(e)}, status=500)
        else:
            return JsonResponse({"success": False, "message": "Invalid request method"}, status=400)

    messages.error(request, "You are not authorized to access the normal test section.")
    return redirect('experiment_home')  # Replace with appropriate view name


@login_required()
def simulation_view(request):
    # Define the path to the HTML file
    simulation_path = os.path.join(settings.BASE_DIR,
                                   'my_app/Simulations/System Design/states-of-matter-basics_en.html')

    # Check if the file exists
    if os.path.exists(simulation_path):
        # Read the file content and return as an HttpResponse
        with open(simulation_path, 'r', encoding='utf-8') as f:
            simulation_content = f.read()
        return HttpResponse(simulation_content)
    else:
        return HttpResponse("Simulation file not found.", status=404)


@login_required
def experiment_home(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        messages.error(request, "You are not authorized to take the experimental test.")
        return redirect('home')  # or some other appropriate page
    
    context = {
        "username": student.first_name
    }
    return render(request, 'my_app/experiment_home.html',context)



@login_required()
def display_experiment_test(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        messages.error(request, "You are not authorized to take the experimental test.")
        return redirect('home')  # or some other appropriate page
    # Fetch questions assigned at '0' (Before Assignment) or '1' (After Assignment)
    questions = Question.objects.filter(assigned_at=0)  # Change the filter if needed

    # It is for Questions
    question_data = []  

    for question in questions:
        # Fetch the options for each question
        options = Option.objects.filter(question=question)
        question_data.append({
            "question": question,
            "options": options
        })

    # print(question_data)
    context = {
        'question_data': question_data,
        "username": student.first_name
    }

    # Pass the question and options data to the template
    return render(request, 'my_app/experiment_test.html', context)


@login_required()
def submit_experimental_test(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        messages.error(request, "You are not authorized to take the experimental test.")
        return redirect('home')  # or some other appropriate page
    questions = Question.objects.filter(assigned_at=0)

    total_score = 0
    total_questions = 0
    response_data = []  # To collect data per question

    for question in questions:
        selected_option_id = request.POST.get(f'question_{question.pk}')
        selected_option = None
        is_correct = False

        if selected_option_id:
            selected_option = Option.objects.get(pk=selected_option_id)
            is_correct = selected_option.is_correct
            if is_correct:
                total_score += 1

        total_questions += 1

        response_data.append({
            'question_text': question.question_text,
            'selected_option': selected_option.option_text if selected_option else "No Answer",
            'is_correct': is_correct
        })

    score_percentage = (total_score / total_questions) * 100 if total_questions > 0 else 0
    # print(f"DEBUG: Total score: {total_score}, Total questions: {total_questions}, Score percentage: {score_percentage}")

    ExperimentAssessmentScore.objects.create(
        student=student,
        score=score_percentage
    )

    # Store data in session
    request.session['experiment_score'] = round(score_percentage, 2)
    request.session['experiment_responses'] = response_data
    request.session['student_name'] = request.user.get_full_name() or request.user.username

    messages.success(request, f"Test submitted successfully! Score: {total_score}/{total_questions}")

    return redirect('experiment_test_results')


@login_required
def experiment_test_results(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        messages.error(request, "You are not authorized to take the experimental test.")
        return redirect('home')  # or some other appropriate page
    context = {
        "username": student.first_name,
        'score': request.session.get('experiment_score'),
        'responses': request.session.get('experiment_responses', []),
        'student_name': request.session.get('student_name', request.user.username),
    }
    return render(request, 'my_app/experiment_test_results.html', context)


@login_required
def all_learning_videos(request):
    student = get_object_or_404(Student, user=request.user)
    if not student.can_take_experimental_test:
        messages.error(request, "You are not authorized to take the experimental test.")
        return redirect('home')  # or some other appropriate page
    try:
        # Fetch all videos from VideoModule
        videos = VideoModule.objects.all()
        # print("videos - ", videos)

        video_data_grouped = []

        for video in videos:
            subtopic = video.subtopic
            topic = subtopic.topic
            video_url = video.url

            if "drive.google.com/file/d/" in video_url:
                file_id = video_url.split('/d/')[1].split('/')[0]
                video_url = f"https://drive.google.com/file/d/{file_id}/preview"

            video_data_grouped.append({
                "username": student.first_name,
                "topic_name": topic.topic_name,
                "subtopic_name": subtopic.subtopic_name,
                "video_title": video.title,
                "video_url": video_url,
                "video_id": video.video_module_id,
                "subtopic_id": subtopic.subtopic_id
            })

        # print("video_data_grouped - ", video_data_grouped)
        context = {
            "video_data_grouped": video_data_grouped
        }
        return render(request, "my_app/all_learning_videos.html", context)

    except Exception as e:
        print("Error in all_learning_videos:", e)
        return JsonResponse({"error": str(e)}, status=400)



# Load embeddings and metadata only once
# model = SentenceTransformer("all-MiniLM-L6-v2")
# index = faiss.read_index("video_index.faiss")

# with open("video_metadata.json", "r") as f:
#     video_data = json.load(f)



HF_API_KEY = os.environ.get("HF_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

@csrf_exempt
def phi3_chat(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Invalid request method."}, status=405)

    try:
        print("RAW BODY:", request.body)
        print("CONTENT TYPE:", request.META.get("CONTENT_TYPE"))
        data = json.loads(request.body.decode('utf-8'))
        user_input = data.get('message', '').strip()
        selected_video_title = data.get('video_title', '').strip()

        if not user_input or not selected_video_title:
            return JsonResponse({"response": "Message and video title are required."}, status=400)

        # Load resources
        model, faiss_index, video_data = get_chatbot_resources()

        # Find the selected video by title
        matched_video = next((v for v in video_data if v.get('title') == selected_video_title), None)
        if not matched_video:
            return JsonResponse({"response": "Selected video not found."}, status=404)

        title = matched_video.get('title', 'Untitled')
        description = matched_video.get('description', 'No description available.')

        # Create prompt
        prompt = f"""Student is watching this video:

Title: {title}
Description: {description}

Student asks: {user_input}
Answer in approximately 300 to 400 words:"""

        # Prepare conversational payload
        payload = {
            "inputs": prompt
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        print("HF API status:", response.status_code)
        print("HF API content:", response.content)
        try:
            result = response.json()
        except Exception as e:
            print("HF API JSONDecodeError:", str(e))
            return JsonResponse({"response": "HF API did not return valid JSON. Status: {} Content: {}".format(response.status_code, response.content.decode(errors='replace'))}, status=500)

        # Error handling for API
        if isinstance(result, dict) and "error" in result:
            return JsonResponse({"response": f"HF API error: {result['error']}"}, status=500)

        # Handle the list response with generated_text
        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            full_response = result[0]["generated_text"]
            # Remove the prompt from the start to get only the answer
            if full_response.startswith(prompt):
                reply = full_response[len(prompt):].lstrip("\n")
            else:
                reply = full_response
        else:
            reply = "No response generated."

        return JsonResponse({"response": reply})

    except json.JSONDecodeError as e:
        print("JSONDecodeError:", str(e))
        return JsonResponse({"response": "Invalid JSON format."}, status=400)
    except Exception as e:
        print("General Exception:", str(e))
        return JsonResponse({"response": f"Server error: {str(e)}"}, status=500)
