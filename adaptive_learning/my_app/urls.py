# my_app/urls.py
from django.urls import path
from . import views
from .views import profile_update_view, student_assignments_view, test_view, submit_test, \
    learning_video, test_results, update_video_progress, simulation_view

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'), 
    path('modules/', views.modules_view, name='modules'),
    path('test/<int:topic_id>/<int:subtopic_id>/', test_view, name='test'),
    path('test-results/<int:topic_id>/<int:subtopic_id>/', test_results, name='test_results'),
    path('submit-test/<int:topic_id>/<int:subtopic_id>/', submit_test, name='submit_test'),
    path('learning-video/<int:topic_id>/<int:subtopic_id>/', learning_video, name='learning_video'),
    path("complete-video/", views.complete_video, name="complete_video"),
    path('video-modules/', views.video_module_view, name='video_modules'),
    path("profile/update/", profile_update_view, name="profile_update"),
    path('profile/assignments/', student_assignments_view, name='student_assignments'),
    path('update-progress/', update_video_progress, name='update_progress'),
    path('simulation/', simulation_view, name='simulation'),
    path('experimental/', views.display_experiment_test, name='experimental'),
    path('submit_experimental_test/', views.submit_experimental_test, name='submit_experimental_test'),
    path('experiment-results/', views.experiment_test_results, name='experiment_test_results'),
    path('all_videos/', views.all_learning_videos, name='all_learning_videos'),
    path('experiment-home/', views.experiment_home, name='experiment_home'),
    path('api/phi3-chat/', views.phi3_chat, name='phi3_chat'),
    path('create-superuser/', views.create_superuser_view),
]
