from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uga_id = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_level = models.CharField(max_length=50, choices=[
        ('5th Grade', '5th Grade'),
        ('6th Grade', '6th Grade'),
        ('7th Grade', '7th Grade'),
        ('8th Grade', '8th Grade'),
        ('9th Grade', '9th Grade'),
        ('10th Grade', '10th Grade'),
        ('11th Grade', '11th Grade'),
        ('12th Grade', '12th Grade'),
        ('College Undergraduate', 'College Undergraduate'),
        ('Other', 'Other'),
    ])
    date_joined = models.DateTimeField(auto_now_add=True)
    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('non_binary', 'Non Binary'),
        ('prefer_not_to_answer', 'Prefer Not to Answer')
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True, null=True)
    ENGLISH_FIRST_LANGUAGE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    is_english_first_language = models.CharField(max_length=3, choices=ENGLISH_FIRST_LANGUAGE_CHOICES, blank=True,
                                                 null=True)

    SCIENCE_EXPERIENCE_CHOICES = [
        ('A_grades', 'Science is one of my best subjects and I usually make A\'s in that class.'),
        ('ok_grades', 'Science is OK, my grades are alright, but it is not my favorite subject.'),
        ('find_difficult',
         'I find science very difficult, I do the best I can, but would like to earn better grades than I do.')
    ]
    science_experience = models.CharField(max_length=100, choices=SCIENCE_EXPERIENCE_CHOICES, blank=True, null=True)

    RACE_CHOICES = [
        ('white', 'White'),
        ('hispanic', 'Hispanic, Latino, or Spanish origin'),
        ('black', 'Black or African American'),
        ('asian', 'Asian'),
        ('american_indian', 'American Indian or Alaska Native'),
        ('middle_eastern', 'Middle Eastern or North African'),
        ('native_hawaiian', 'Native Hawaiian or Other Pacific Islander'),
        ('other_race', 'Some other race, ethnicity, or origin'),
        ('prefer_not_to_answer', 'Prefer not to answer')
    ]
    race = models.ManyToManyField('Race', blank=True)
    can_take_experimental_test = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Race(models.Model):
    race_type = models.CharField(max_length=50, choices=Student.RACE_CHOICES)

    def __str__(self):
        return self.race_type

class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=30)
    topic_order = models.IntegerField()

    def __str__(self):
        return self.topic_name

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, related_name="subtopics", on_delete=models.CASCADE)
    subtopic_id = models.AutoField(primary_key=True)
    subtopic_name = models.CharField(max_length=255)
    subtopic_order_number = models.IntegerField()

    def __str__(self):
        return self.subtopic_name

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    topic = models.ForeignKey(Topic, related_name="questions", on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, related_name="questions", on_delete=models.CASCADE)
    assigned_at = models.IntegerField(choices=[(0, 'Before Assignment'), (1, 'After Assignment')], default=0)
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
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.option_text} (Correct: {self.is_correct})"

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="student_id")
    date_taken = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    topic = models.ForeignKey(Topic, related_name="assessments", on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, related_name="assessments", on_delete=models.CASCADE)
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
        return f"Response by {self.assessment} for {self.question}"

class VideoModule(models.Model):
    video_module_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    topic = models.ForeignKey(Topic, related_name="video_modules", on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, related_name="video_modules", on_delete=models.CASCADE, null=True, blank=True)
    level = models.CharField(max_length=15)
    students = models.ManyToManyField(Student, through='Recommendation')
    misconceptions = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated list of related misconception numbers like 'm1,m2,m5'"
    )


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
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="student_id")
    module = models.ForeignKey(VideoModule, on_delete=models.CASCADE)
    completion_status = models.CharField(max_length=15, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ])
    current_topic = models.ForeignKey(Topic, related_name="current_topics", null=True, blank=True, on_delete=models.SET_NULL)
    next_topic = models.ForeignKey(Topic, related_name="next_topics", null=True, blank=True, on_delete=models.SET_NULL)
    current_subtopic = models.ForeignKey(Subtopic, related_name="current_subtopics", null=True, blank=True, on_delete=models.SET_NULL)
    next_subtopic = models.ForeignKey(Subtopic, related_name="next_subtopics", null=True, blank=True, on_delete=models.SET_NULL)
    last_accessed = models.DateTimeField(auto_now=True)
    score_before = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    score_after = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    video_watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'module', 'current_subtopic')  # Ensure this combination is unique

    def __str__(self):
        return f"Progress of {self.student} in {self.module}"



class VideoProgress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    video = models.ForeignKey(VideoModule, on_delete=models.CASCADE)
    watched = models.BooleanField(default=False)
    watched_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('student', 'video')  # Ensure one entry per student-video


class ExperimentAssessmentScore(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, to_field="student_id")
    taken_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.student.user.username} - Score: {self.score} - Taken at: {self.taken_at}"