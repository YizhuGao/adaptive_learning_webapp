# from my_app.models import VideoModule, Topic, Subtopic
# from django.db import transaction
#
# with transaction.atomic():
#     topic_obj, created = Topic.objects.get_or_create(topic_name="Thermodynamics")
#     subtopic_obj, created = Subtopic.objects.get_or_create(subtopic_name="Nature of temperature", topic=topic_obj)
#     video_module = VideoModule.objects.create(
#         title="Nature of Temperature",
#         url="https://www.youtube.com/watch?v=96k7_7RjCpg",
#         description="This video explains the concept of temperature and its significance in the field of thermodynamics.",
#         topic=topic_obj,
#         subtopic=subtopic_obj,
#         level="Beginner"
#     )
#     print(f"VideoModule '{video_module.title}' added successfully!")
from my_app.models import VideoModule, Topic, Subtopic
from django.db import transaction

# Delete existing VideoModules (leave Topics and Subtopics intact)
VideoModule.objects.all().delete()

# Data for new videos to be inserted
videos_data = [
    # {
    #     "title": "Nature of Temperature - Introduction",
    #     "url": "https://www.youtube.com/watch?v=96k7_7RjCpg",
    #     "description": "Introduction to the concept of temperature and its significance in thermodynamics.",
    #     "level": "Beginner",
    #     "topic_name": "Thermodynamics",
    #     "subtopic_name": "Nature of Temperature",
    # },
    {
        "title": "The conductivity of temperature",
        "url": "https://drive.google.com/file/d/1PuvHLyXVm_zTs0JnhltWQOr3xQWnUrx2/view?usp=sharing&t=5",
        "description": "Understanding different methods used to measure temperature.",
        "level": "Beginner",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Nature of temperature",
    },
    {
        "title": "Water and oil",
        "url": "https://drive.google.com/file/d/1S8U3vBoJW0jfPV5COUEUih08JdSbMUh6/view?usp=sharing",
        "description": "Understanding different methods used to measure temperature.",
        "level": "Beginner",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Nature of temperature",
    },
    {
        "title": "Temperature",
        "url": "https://drive.google.com/file/d/1LizRx2eG5PTeFijjTkBUlUhnie8AF00a/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Cold and hot water to environment temperature",
        "url": "https://drive.google.com/file/d/18W1I-ZywPaamQ4Snn5FTGW25zumBOHgT/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Diffusion",
        "url": "https://drive.google.com/file/d/1JFU39GuGd-8yPd8xh1bZvD5yc6IVSabE/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Ice",
        "url": "https://drive.google.com/file/d/1novvBfJJozY3qUhklDiF6o5uk6Fhh7FA/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and material",
    },
    {
        "title": "Melted ice",
        "url": "https://drive.google.com/file/d/188pul86g6ibo42BVu5DPf6jp40SmusyM/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Fusion/melting point and freezing point",
    },
    {
        "title": "Metal in cold and hot water",
        "url": "https://drive.google.com/file/d/1LF91sc5gXto1taib3J_eHDXXPWmwk8V9/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Fusion/melting point and freezing point",
    },
    {
        "title": "Boiled Water",
        "url": "https://drive.google.com/file/d/1CF0mejUwK9gWLrPUwDvuitwT9sI77TAv/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Boiling point, Liquifaction, Vaporation",
    },
    {
        "title": "Cold and hot water",
        "url": "https://drive.google.com/file/d/18pE3I4WUkfoNiIAniM24ySczuSLsQjrh/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Boiling point, Liquifaction, Vaporation",
    },
    {
        "title": "Vaportation",
        "url": "https://drive.google.com/file/d/11tPM8yK4Lfs8ukfa92bt5b5BCxBnYWm-/view?usp=sharing",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Boiling point, Liquifaction, Vaporation",
    }
]

# Insert new data into the models
with transaction.atomic():
    for video in videos_data:
        topic_obj, created = Topic.objects.get_or_create(topic_name=video["topic_name"])
        subtopic_obj, created = Subtopic.objects.get_or_create(subtopic_name=video["subtopic_name"], topic=topic_obj)
        video_module = VideoModule.objects.create(
            title=video["title"],
            url=video["url"],
            description=video["description"],
            topic=topic_obj,
            subtopic=subtopic_obj,
            level=video["level"],
        )
        print(f"VideoModule '{video_module.title}' added successfully!")
