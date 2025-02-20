from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, logger
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.timezone import now
from .models import Assessment, Question, Student, AssessmentResponse, Option, VideoModule
from django.urls import reverse
import logging
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'my_app/index.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Manually authenticate user
            print(f"Attempting to authenticate user: {username}")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Authentication successful: {user.username}")
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')  # Redirect to success page after login
            else:
                print("Authentication failed")
                messages.error(request, "Invalid username or password.")
        else:
            print("Form is not valid!")
            print(form.errors)  # Print form errors
            messages.error(request, "Error during login. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'my_app/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        uga_id = request.POST.get('uga_id')  # New field for student info
        class_level = request.POST.get('class_level')  # New field for student info
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('signup')

        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()  # Save the user to the database

            # Create a corresponding Student entry
            student = Student.objects.create(
                user=user,
                uga_id=uga_id,
                first_name=first_name,
                last_name=last_name,
                class_level=class_level
            )

        except Exception as e:
            messages.error(request, f"Error creating user: {e}")
            return redirect('signup')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
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
def modules_view(request):
    # Fetch all unique assessment topics
    topics = Question.objects.values_list('topic', flat=True).distinct()
    return render(request, 'my_app/modules.html', {'topics': topics, 'username': request.user.username})


@login_required
def test_view(request, topic):
    # Fetch the questions based on the topic
    questions = Question.objects.filter(topic=topic, assigned_at=0)

    context = {
        'topic': topic,
        'questions': questions,
        'username': request.user.username
    }

    return render(request, 'my_app/test.html', context)


@login_required
def submit_test(request, topic):
    if request.method == "POST":
        print("Form Submitted: ", request.POST)  # Debugging line

        if not request.POST:
            print("No data received in POST request.")
            return JsonResponse({"error": "No data received"}, status=400)

        try:
            # Check if the user is logged in and has a student profile
            student = get_object_or_404(Student, user=request.user)
            print(f"Student Found: {student}")

            # Create an assessment entry
            assessment = Assessment.objects.create(
                student=student,
                topic=topic,
                date_taken=now()
            )
            print(f"Assessment Created: {assessment}")

            correct_count = 0
            total_questions = 0

            # Process submitted answers
            for key, value in request.POST.items():
                if key.startswith("question_"):
                    # Extract question ID and check if value is not empty
                    question_id = key.split("_")[1]
                    print(f"Processing Question ID: {question_id}, Selected Option ID: {value}")

                    if value:  # Ensure a value is selected for each question
                        question = get_object_or_404(Question, pk=question_id)
                        selected_option = get_object_or_404(Option, pk=value)

                        # Save response
                        AssessmentResponse.objects.create(
                            assessment=assessment,
                            question=question,
                            selected_option=selected_option
                        )
                        print(f"Response Saved: Question {question_id}, Option {value}")

                        # Check correctness
                        if selected_option.is_correct:
                            correct_count += 1
                        total_questions += 1

            # Calculate and update score
            score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
            assessment.score = score
            assessment.save()
            print(f"Final Score: {score}")

            # Now, instead of directly rendering, we pass the data to the result template
            context = {
                'student_name': student.first_name + ' ' + student.last_name,
                'topic': topic,
                'score': score,
                'date_taken': assessment.date_taken,
                'responses': AssessmentResponse.objects.filter(assessment=assessment)
            }

            print("Rendering test_results with context")
            print(f"Context:" , context)
            return render(request, "my_app/test_results.html", context)

        except Exception as e:
            print("Error:", e)
            return JsonResponse({"error": str(e)}, status=400)

    return redirect("modules")  # Redirect if accessed incorrectly


@login_required
def video_module_view(request):
    # Fetch all VideoModules
    video_modules = VideoModule.objects.all()

    context = {
        'video_modules': video_modules
    }

    return render(request, 'my_app/video_modules.html', context)


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