from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Assessment, Question


def index(request):
    return render(request, 'my_app/index.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')  # Redirect to success.html after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Error during login. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'my_app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')  # Reload the signup page

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        messages.success(request, f"Account created successfully for {username}!")
        return redirect('home')  # Redirect to success.html after signup
    return render(request, 'my_app/signup.html')

def success_view(request):
    return render(request, 'my_app/success.html')

@login_required
def home_view(request):
    return render(request, 'my_app/home.html', {'username': request.user.username})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

@login_required
def modules_view(request):
    # Fetch all unique assessment topics
    topics = Assessment.objects.values_list('topic', flat=True).distinct()
    return render(request, 'my_app/modules.html', {'topics': topics})

@login_required
def test_view(request, topic):
    # Fetch all questions related to the selected topic
    questions = Question.objects.filter(topic=topic)
    return render(request, 'my_app/test.html', {'topic': topic, 'questions': questions})
# @login_required
# def test_scores_view(request):
#     # Get all assessments for the logged-in user
#     assessments = Assessment.objects.filter(student__user=request.user).order_by('-date_taken')

#     # Render the results in the template
#     return render(request, 'my_app/test_scores.html', {'assessments': assessments})


# @login_required
# def assessment_questions_view(request, assessment_id):
#     # Get the assessment by id, or return 404 if not found
#     assessment = get_object_or_404(Assessment, pk=assessment_id, student__user=request.user)

#     # Get the questions related to this assessment
#     questions = assessment.questions.all()

#     # Render the results in the template
#     return render(request, 'my_app/assessment_questions.html', {'assessment': assessment, 'questions': questions})





# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index.html')  # Redirect to home or any other page after successful signup
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})