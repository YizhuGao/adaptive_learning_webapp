from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uga_id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_level = models.CharField(max_length=10, choices=[
        ('9th Grade', '9th Grade'),
        ('10th Grade', '10th Grade'),
        ('11th Grade', '11th Grade'),
        ('12th Grade', '12th Grade'),
    ])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.uga_id})"

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    topic = models.CharField(max_length=30, choices=[
        ('Mathematics', 'Mathematics'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('Thermodynamics', 'Thermodynamics'),  # Added based on your data
    ])
    subtopic = models.CharField(max_length=255, null=True, blank=True)  # Subtopic of the question
    assigned_at = models.IntegerField(choices=[(0, 'Before Assignment'), (1, 'After Assignment')], default=0)  # Flag for before or after assignment
    difficulty_level = models.CharField(max_length=15, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ])

    def __str__(self):
        return self.question_text

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    option_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  # Marks the correct answer

    def __str__(self):
        return f"{self.option_text} (Correct: {self.is_correct})"

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_taken = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    topic = models.CharField(max_length=30)
    level = models.CharField(max_length=15)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"Assessment for {self.student} on {self.date_taken}"

class AssessmentResponse(models.Model):
    response_id = models.AutoField(primary_key=True)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Response by {self.assessment.student} for {self.question}"

class VideoModule(models.Model):
    video_module_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    topic = models.CharField(max_length=30)
    subtopic = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=15)
    students = models.ManyToManyField(Student, through='Recommendation')

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    recommendation_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(VideoModule, on_delete=models.CASCADE)
    recommendation_date = models.DateTimeField(auto_now_add=True)
    confidence_score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Recommendation for {self.student} to watch {self.module}"

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(VideoModule, on_delete=models.CASCADE)
    completion_status = models.CharField(max_length=15, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ])
    last_accessed = models.DateTimeField(auto_now=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Progress of {self.student} in {self.module}"