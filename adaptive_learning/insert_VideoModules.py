# You can run this script from Django shell or as part of a migration

from my_app.models import VideoModule  # Ensure you're importing the model from the correct app
from django.db import transaction

# Use a transaction to ensure atomicity
with transaction.atomic():
    video_module = VideoModule.objects.create(
        title="Nature of Temperature",
        url="https://www.youtube.com/watch?v=96k7_7RjCpg",
        description="This video explains the concept of temperature and its significance in the field of thermodynamics.",
        topic="Thermodynamics",
        subtopic="Nature of temperature",
        level="Beginner"  # Assuming level is 'Beginner', change as per your need
    )
    print(f"VideoModule '{video_module.title}' added successfully!")
