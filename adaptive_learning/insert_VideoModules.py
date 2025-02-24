from my_app.models import VideoModule, Topic, Subtopic
from django.db import transaction

with transaction.atomic():
    topic_obj, created = Topic.objects.get_or_create(topic_name="Thermodynamics")
    subtopic_obj, created = Subtopic.objects.get_or_create(subtopic_name="Nature of temperature", topic=topic_obj)
    video_module = VideoModule.objects.create(
        title="Nature of Temperature",
        url="https://www.youtube.com/watch?v=96k7_7RjCpg",
        description="This video explains the concept of temperature and its significance in the field of thermodynamics.",
        topic=topic_obj,
        subtopic=subtopic_obj,
        level="Beginner"
    )
    print(f"VideoModule '{video_module.title}' added successfully!")
