# my_app/urls.py
from django.urls import path
from . import views
from .views import profile_update_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'), 
    path('modules/', views.modules_view, name='modules'),  # Modules page
    path('test/<str:topic>/', views.test_view, name='test'),
    path('submit-test/<str:topic>/', views.submit_test, name='submit_test'),
    path('video-modules/', views.video_module_view, name='video_modules'),
    path("profile/update/", profile_update_view, name="profile_update"),
    # path('test_results/<str:topic>/', test_results, name='test_results'),  # Ensure this exists
    # path('profile/', views.profile_view, name='profile'),
    # path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    # path('test-scores/', views.test_scores_view, name='test_scores'),  # New URL pattern
    # path('assessment-questions/<int:assessment_id>/', views.assessment_questions_view, name='assessment_questions'),  # New URL pattern
]
