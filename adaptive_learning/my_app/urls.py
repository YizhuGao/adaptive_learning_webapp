# my_app/urls.py
from django.urls import path
from . import views
from .views import profile_update_view, student_assignments_view, test_view, submit_test, \
    learning_video, test_results, update_video_progress

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'), 
    path('modules/', views.modules_view, name='modules'),
    path('test/<str:topic_name>/<str:subtopic_name>/', test_view, name='test'),
    path('test-results/<str:topic_name>/<str:subtopic_name>/', test_results, name='test_results'),
    path('submit-test/<str:topic_name>/<str:subtopic_name>/', submit_test, name='submit_test'),
    path('learning-video/<str:topic_name>/<str:subtopic_name>/', learning_video, name='learning_video'),
    path('video-modules/', views.video_module_view, name='video_modules'),
    path("profile/update/", profile_update_view, name="profile_update"),
    path('profile/assignments/', student_assignments_view, name='student_assignments'),
    path('update-progress/', update_video_progress, name='update_progress'),
]
