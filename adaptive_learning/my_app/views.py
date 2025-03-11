import os
from datetime import timezone

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.utils import timezone, timesince
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Assessment, Question, Student, AssessmentResponse, Option, VideoModule, Subtopic, Progress, Topic, \
    VideoProgress
import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'my_app/index.html')


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

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
    return render(request, 'my_app/home.html', {'username': request.user.username})



@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')



@login_required
def test_view(request, topic_id, subtopic_id):
    student = get_object_or_404(Student, user=request.user)

    # Fetch Topic and Subtopic
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

    questions = Question.objects.filter(topic=topic, assigned_at=assigned_value, subtopic=subtopic)

    context = {
        'topic': topic,
        'subtopic': subtopic,
        'questions': questions,
        'username': request.user.username,
        'assigned_video': student_progress.video_watched,
        'load_video_link': load_video_link,  # Include this flag in the context
    }

    return render(request, 'my_app/test.html', context)




@login_required
def submit_test(request, topic_id, subtopic_id):
    if request.method == "POST":
        print("Form Submitted: ", request.POST)  # Debugging line

        if not request.POST:
            print("No data received in POST request.")
            return JsonResponse({"error": "No data received"}, status=400)

        try:
            student = get_object_or_404(Student, user=request.user)
            topic = get_object_or_404(Topic, topic_id=topic_id)
            subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

            # Create an assessment entry
            assessment = Assessment.objects.create(
                student=student,
                topic=topic,
                date_taken=timezone.now()
            )

            correct_count = 0
            total_questions = 0
            assigned_at_0_count = 0
            assigned_at_1_count = 0

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

                    # Check correctness
                    if selected_option.is_correct:
                        correct_count += 1
                    total_questions += 1

                    # Track assigned_at values
                    if question.assigned_at == 0:
                        assigned_at_0_count += 1
                    elif question.assigned_at == 1:
                        assigned_at_1_count += 1

            # Calculate score
            score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
            assessment.score = score
            assessment.save()

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


@login_required
def modules_view(request):
    student = get_object_or_404(Student, user=request.user)
    topics = Topic.objects.all()
    topic_data = []

    for topic in topics:
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
                    # Check if progress already exists for the next subtopic
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
                        progress = new_progress  # Update reference to latest progress

                    topic_data.append({'topic': topic, 'subtopic': progress.current_subtopic})

                    # Insert records for each video in the next subtopic
                    video_modules = VideoModule.objects.filter(topic=topic, subtopic=next_subtopic)
                    for video in video_modules:
                        VideoProgress.objects.get_or_create(
                            student=student,
                            subtopic=next_subtopic,
                            video=video,
                            defaults={'watched': False, 'watched_at': None}
                        )

                else:
                    # If no next subtopic, mark topic as completed
                    progress.completion_status = 'Completed'
                    progress.save()

            else:
                # If current subtopic is not complete, do not create next subtopic progress
                topic_data.append({'topic': topic, 'subtopic': progress.current_subtopic})

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

                # Insert VideoProgress records for videos in the first subtopic
                video_modules = VideoModule.objects.filter(topic=topic, subtopic=first_subtopic)
                for video in video_modules:
                    VideoProgress.objects.get_or_create(
                        student=student,
                        subtopic=first_subtopic,
                        video=video,
                        defaults={'watched': False, 'watched_at': None}
                    )

            topic_data.append({'topic': topic, 'subtopic': progress.current_subtopic})

    context = {
        'topic_data': topic_data,
        'username': request.user.username,
    }

    return render(request, 'my_app/modules.html', context)


@login_required
def test_results(request, topic_id, subtopic_id):
    try:
        # Get student details
        student = get_object_or_404(Student, user=request.user)

        # Get topic and subtopic details
        topic = get_object_or_404(Topic, topic_id=topic_id)
        subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

        # Fetch the latest assessment for the student on this topic
        assessment = Assessment.objects.filter(student=student, topic=topic).order_by("-date_taken").first()
        if not assessment:
            return JsonResponse({"error": "No assessment data found for this topic."}, status=404)

        # Fetch responses for the assessment
        responses = AssessmentResponse.objects.filter(assessment=assessment)

        # Get the score
        score = assessment.score

        # Get the video module (if available)
        video_module = VideoModule.objects.filter(subtopic=subtopic).first()
        print("Video Module (Subtopic):", video_module)

        if not video_module:
            video_module = VideoModule.objects.filter(topic=topic).first()  # Fallback to topic-level video
            print("Video Module (Topic):", video_module)

        # Get the progress for the student and subtopic
        progress = Progress.objects.filter(student=student, current_subtopic=subtopic).first()

        # Get video URL with the condition
        video_url = video_module.url if video_module and progress and not progress.score_after else None
        if video_url:
            if "youtube.com/watch" in video_url:
                video_url = video_url.replace("watch?v=", "embed/")
        print("Video URL:", video_url)

        # Prepare context data for the template
        context = {
            "student_name": f"{student.first_name} {student.last_name}",
            "topic": topic,
            "subtopic": subtopic,
            "score": score,
            "date_taken": assessment.date_taken,
            "responses": responses,
            "video_url": video_url,
            "student_id": student.student_id,  # Add student_id here
        }

        return render(request, "my_app/test_results.html", context)

    except Exception as e:
        print("Error in test_results:", e)
        return JsonResponse({"error": str(e)}, status=400)


@login_required
def learning_video(request, topic_id, subtopic_id):
    try:
        print(f"Received topic_id: {topic_id}, subtopic_id: {subtopic_id}")

        # Get the logged-in student
        student = get_object_or_404(Student, user=request.user)

        # Get topic and subtopic
        topic = get_object_or_404(Topic, topic_id=topic_id)
        subtopic = get_object_or_404(Subtopic, subtopic_id=subtopic_id, topic=topic)

        # Fetch videos linked to the subtopic
        videos = VideoModule.objects.filter(subtopic=subtopic)

        if not videos.exists():
            print("No videos found for this subtopic.")

        video_data = []
        for video in videos:
            video_url = video.url

            # Convert Google Drive link to embeddable format
            if "drive.google.com/file/d/" in video_url:
                file_id = video_url.split('/d/')[1].split('/')[0]
                video_url = f"https://drive.google.com/file/d/{file_id}/preview"

            video_data.append({
                'id': video.video_module_id,
                'title': video.title,
                'url': video_url
            })

        # Pass student.id to the context
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



@login_required
def video_module_view(request):
    # Fetch all VideoModules
    video_modules = VideoModule.objects.all()

    context = {
        'video_modules': video_modules
    }

    return render(request, 'my_app/learning_video.html', context)


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


@login_required
def student_assignments_view(request):
    student = get_object_or_404(Student, user=request.user)
    assignments = Assessment.objects.filter(student=student).order_by('-date_taken')  # Fetch assignments

    context = {
        'assignments': assignments,
        'username': request.user.username
    }
    return render(request, 'my_app/student_assignments.html', context)




@csrf_exempt
@login_required
def update_video_progress(request):
    if request.method == 'POST':
        # Parse the incoming data (subtopic ID, student ID)
        data = json.loads(request.body)
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



@login_required
def complete_video(request):
    print("Inside the complete_video")
    if request.method == 'POST':
        try:
            # Parse the JSON request data
            data = json.loads(request.body)
            video_id = data.get('video_id')
            subtopic_id = data.get('subtopic_id')

            print(f"DEBUG: Received Subtopic ID: {subtopic_id}, Video ID: {video_id}")

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
                raise Exception(f"VideoProgress entry not found for student {student.id}, video {video.id}, subtopic {subtopic.id}")

            # If the video hasn't been watched already, mark it as watched
            if not video_progress.watched:
                video_progress.watched = True
                video_progress.watched_at = timezone.now()
                video_progress.save()

                # Check if all videos for this subtopic are watched
                total_videos = VideoModule.objects.filter(subtopic=subtopic).count()
                watched_videos = VideoProgress.objects.filter(
                    student=student, subtopic=subtopic, watched=True
                ).count()

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
