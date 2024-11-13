# my_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This will serve the home page
    path('login/', views.login_view, name='login'),  # For login.html
    path('signup/', views.signup_view, name='signup'), # For Sigunp.html
]