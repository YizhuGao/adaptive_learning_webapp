from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def login_view(request):
    return render(request, 'my_app/login.html')


def signup_view(request):
    return render(request, 'my_app/signup.html')

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