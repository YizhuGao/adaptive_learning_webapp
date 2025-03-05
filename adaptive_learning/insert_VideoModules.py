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
        "url": "https://outlookuga-my.sharepoint.com/personal/yg94225_uga_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Fyg94225%5Fuga%5Fedu%2FDocuments%2FGrant%2F2024%20UGA%20Learning%20Technologies%20Grant%2FThermal%20Topic%2FLearning%20Videos%2FThermal%20Learning%20Videos%2FMisconception%2015%20the%20conductivity%20of%20temperature%2FMisconception%2015%20the%20conductivity%20of%20temperature%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E3b842d6d%2D65c8%2D43c3%2Db5de%2D9a6231db1b27",
        "description": "Understanding different methods used to measure temperature.",
        "level": "Beginner",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Nature of temperature",
    },
    {
        "title": "Water and oil",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%2018%20water%20and%20oil/Misconception%2018%20water%20and%20oil.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=VwvaRW",
        "description": "Understanding different methods used to measure temperature.",
        "level": "Beginner",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Nature of temperature",
    },
    {
        "title": "Temperature",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%204%20Temperature/Misconception%204%20Temperature.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Z01bLR",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Cold and hot water to environment temperature",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%2013-cold%20and%20hot%20water%20to%20environment%20temperature/Misconception%2013-cold%20and%20hot%20water%20to%20environment%20temperature.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=Gc3JG7",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Diffusion",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception3%20Diffusion/Misconception3%20Diffusion.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=AnLAXE",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and temperature change",
    },
    {
        "title": "Ice",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%207-ice/Misconception%207-ice.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=PxCwcn",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Heat transfer and material",
    },
    {
        "title": "Melted ice",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%209%2012%2020%2021%20melted%20ice/Misconception%209%2012%2020%2021%20melted%20ice.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=wy43E4",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Fusion/melting point and freezing point",
    },
    {
        "title": "Metal in cold and hot water",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%2012%2013%2017%2018-%20mental%20with%20cold%20and%20hot%20water/Misconception%2012%2013%2017%2018-%20mental%20with%20cold%20and%20hot%20water.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=ij8uva",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Fusion/melting point and freezing point",
    },
    {
        "title": "Boiled Water",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%205%209%2019%2022%20Boiled%20water/M5%209%2019%2022%20Boiled%20Water.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=nakOWy",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Boiling point, Liquifaction, Vaporation",
    },
    {
        "title": "Cold and hot water",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%208%20cold%20and%20hot%20water/Misconception%208%20cold%20and%20hot%20water.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=5jbJxc",
        "description": "Exploring how temperature relates to heat energy transfer.",
        "level": "Intermediate",
        "topic_name": "Thermodynamics",
        "subtopic_name": "Boiling point, Liquifaction, Vaporation",
    },
    {
        "title": "Vaportation",
        "url": "https://outlookuga-my.sharepoint.com/:v:/r/personal/yg94225_uga_edu/Documents/Grant/2024%20UGA%20Learning%20Technologies%20Grant/Thermal%20Topic/Learning%20Videos/Thermal%20Learning%20Videos/Misconception%2023%20vaportation/Misconception%2023%20vaportation.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=cBUv49",
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
