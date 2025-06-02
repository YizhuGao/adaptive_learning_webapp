import os
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adaptive_learning.settings")
django.setup()

from my_app.models import Question, Option, Topic, Subtopic

Option.objects.all().delete()
Question.objects.all().delete()

questions_data = [
    {
        "question_text": "What is the most likely temperature of ice-cubes stored in a refrigerator's freezer compartment?", #question 1
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
        "subtopic_order_number": 4,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("−10 °C", True),
            ("0 °C", False),
            ("5 °C", False),
            ("It depends on the size of the ice-cubes.", False),
        ],
    },
    {
        "question_text": "Ken takes six ice-cubes from the freezer and puts four of them into a glass of water. What is the most likely temperature of the water at this stage?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 2
        "subtopic_order_number": 4,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("−10 °C", False),
            ("0 °C", True),
            ("5 °C", False),
            ("10 °C", False),
        ],
    },
    {
        "question_text": "When an ice-cube melts, what is the expected temperature change of the ice-cube?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 3
        "subtopic_order_number": 4,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("It stays the same.", True),
            ("It increases significantly.", False),
            ("It decreases significantly.", False),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "If a person steps into a pool of water at 10 °C, what would be the most likely result in terms of heat transfer?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 4
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Heat will flow from the body into the water.", True),
            ("Heat will flow from the water into the body.", False),
            ("There will be no heat transfer.", False),
            ("The body will remain at the same temperature.", False),
        ],
    },
    {
        "question_text": "If the temperature of water reaches 0 °C, it will begin to freeze. What happens to the temperature as it transitions from liquid to solid?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 5
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("The temperature decreases further.", False),
            ("The temperature stays constant.", True),
            ("The temperature increases.", False),
            ("The temperature fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the primary reason why ice is less dense than water?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 6
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Ice molecules are more spread out in the solid form.", True),
            ("Water molecules are more tightly packed in the solid form.", False),
            ("Ice molecules are heavier than water molecules.", False),
            ("Water expands when it freezes.", False),
        ],
    },
    {
        "question_text": "What is the state of matter for water at room temperature (25 °C)?", #question 7
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Solid", False),
            ("Liquid", True),
            ("Gas", False),
            ("Plasma", False),
        ],
    },
    {
        "question_text": "What is the freezing point of water at standard atmospheric pressure?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 8
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("0 °C", True),
            ("100 °C", False),
            ("32 °F", True),
            ("−32 °C", False),
        ],
    },
    {
        "question_text": "How does the density of water change as it freezes?", #question 9
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the boiling point of water at standard atmospheric pressure?", #question 10
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("100 °C", True),
            ("212 °F", True),
            ("32 °C", False),
            ("0 °C", False),
        ],
    },
    {
        "question_text": "At which temperature does water boil at standard atmospheric pressure?", #question 11
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
"subtopic_order_number": 4,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("100 °C", True),
            ("32 °C", False),
            ("0 °C", False),
            ("212 °C", False),
        ],
    },
    {
        "question_text": "What happens to the volume of water when it freezes?", #question 12
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", True),
            ("It decreases.", False),
            ("It stays the same.", False),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "How does the water temperature affect its ability to dissolve substances?", #question 13
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Hot water dissolves substances more quickly.", True),
            ("Cold water dissolves substances more quickly.", False),
            ("Temperature has no effect on solubility.", False),
            ("Hot water does not dissolve substances at all.", False),
        ],
    },
    {
        "question_text": "When water evaporates, what happens to its temperature?", #question 14
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material",
"subtopic_order_number": 3,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the name of the process where water changes from a gas to a liquid?", #question 15
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Condensation", True),
            ("Evaporation", False),
            ("Freezing", False),
            ("Sublimation", False),
        ],
    },
    {
        "question_text": "What is the energy required to change the temperature of a substance?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material", #question 16
        "assigned_at": 0,
        "subtopic_order_number": 3,
        "difficulty_level": "Intermediate",
        "options": [
            ("Specific heat capacity", True),
            ("Latent heat", False),
            ("Enthalpy", False),
            ("Thermal conductivity", False),
        ],
    },
    {
        "question_text": "What is the difference between boiling and evaporation?", #question 17
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Boiling occurs only at the surface.", False),
            ("Evaporation is a slower process than boiling.", True),
            ("Boiling occurs at any temperature.", False),
            ("Evaporation does not involve temperature changes.", False),
        ],
    },
    {
        "question_text": "What is the term for the amount of heat required to convert a substance from a solid to a liquid?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change", #question 18
"subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Latent heat of fusion", True),
            ("Latent heat of vaporization", False),
            ("Specific heat", False),
            ("Sublimation heat", False),
        ],
    },
    {
        "question_text": "What is the name of the process where a substance changes directly from a solid to a gas?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 19
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Sublimation", True),
            ("Melting", False),
            ("Freezing", False),
            ("Condensation", False),
        ],
    },
    {
        "question_text": "What happens to the water temperature when ice is added?", #question 20
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the term used for the heat required to change a liquid to a gas?", #question 21
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Latent heat of vaporization", True),
            ("Latent heat of fusion", False),
            ("Specific heat", False),
            ("Heat of reaction", False),
        ],
    },
    {
        "question_text": "What is the unit of heat?", #question 22
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Joule", True),
            ("Kelvin", False),
            ("Newton", False),
            ("Celsius", False),
        ],
    },
    {
        "question_text": "Which of the following gases is most commonly used for refrigeration?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 23
        "subtopic_order_number": 3,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Carbon dioxide", False),
            ("Freon", True),
            ("Nitrogen", False),
            ("Oxygen", False),
        ],
    },
    {
        "question_text": "Which of the following gases is used to pressurize soft drinks?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 0, #question 24
        "difficulty_level": "Beginner",
        "options": [
            ("Oxygen", False),
            ("Carbon dioxide", True),
            ("Nitrogen", False),
            ("Helium", False),
        ],
    },
    {
        "question_text": "What is the process of transferring heat through direct contact?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature", #question 25
"subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Conduction", True),
            ("Convection", False),
            ("Radiation", False),
            ("Insulation", False),
        ],
    },
    {
        "question_text": "What is the term for the energy required to raise the temperature of a substance?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Specific heat", True), #question 26
            ("Latent heat", False),
            ("Thermal conductivity", False),
            ("Heat capacity", False),
        ],
    },



    {
        "question_text": "What is the most likely temperature of ice-cubes stored in a refrigerator's freezer compartment?", #question 1
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
        "subtopic_order_number": 4,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("−10 °C", True),
            ("0 °C", False),
            ("5 °C", False),
            ("It depends on the size of the ice-cubes.", False),
        ],
    },
    {
        "question_text": "Ken takes six ice-cubes from the freezer and puts four of them into a glass of water. What is the most likely temperature of the water at this stage?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 2
        "subtopic_order_number": 4,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("−10 °C", False),
            ("0 °C", True),
            ("5 °C", False),
            ("10 °C", False),
        ],
    },
    {
        "question_text": "When an ice-cube melts, what is the expected temperature change of the ice-cube?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 3
        "subtopic_order_number": 4,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("It stays the same.", True),
            ("It increases significantly.", False),
            ("It decreases significantly.", False),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "If a person steps into a pool of water at 10 °C, what would be the most likely result in terms of heat transfer?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 4
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Heat will flow from the body into the water.", True),
            ("Heat will flow from the water into the body.", False),
            ("There will be no heat transfer.", False),
            ("The body will remain at the same temperature.", False),
        ],
    },
    {
        "question_text": "If the temperature of water reaches 0 °C, it will begin to freeze. What happens to the temperature as it transitions from liquid to solid?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 5
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("The temperature decreases further.", False),
            ("The temperature stays constant.", True),
            ("The temperature increases.", False),
            ("The temperature fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the primary reason why ice is less dense than water?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 6
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Ice molecules are more spread out in the solid form.", True),
            ("Water molecules are more tightly packed in the solid form.", False),
            ("Ice molecules are heavier than water molecules.", False),
            ("Water expands when it freezes.", False),
        ],
    },
    {
        "question_text": "What is the state of matter for water at room temperature (25 °C)?", #question 7
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Solid", False),
            ("Liquid", True),
            ("Gas", False),
            ("Plasma", False),
        ],
    },
    {
        "question_text": "What is the freezing point of water at standard atmospheric pressure?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 8
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("0 °C", True),
            ("100 °C", False),
            ("32 °F", True),
            ("−32 °C", False),
        ],
    },
    {
        "question_text": "How does the density of water change as it freezes?", #question 9
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the boiling point of water at standard atmospheric pressure?", #question 10
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("100 °C", True),
            ("212 °F", True),
            ("32 °C", False),
            ("0 °C", False),
        ],
    },
    {
        "question_text": "At which temperature does water boil at standard atmospheric pressure?", #question 11
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
"subtopic_order_number": 4,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("100 °C", True),
            ("32 °C", False),
            ("0 °C", False),
            ("212 °C", False),
        ],
    },
    {
        "question_text": "What happens to the volume of water when it freezes?", #question 12
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", True),
            ("It decreases.", False),
            ("It stays the same.", False),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "How does the water temperature affect its ability to dissolve substances?", #question 13
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Hot water dissolves substances more quickly.", True),
            ("Cold water dissolves substances more quickly.", False),
            ("Temperature has no effect on solubility.", False),
            ("Hot water does not dissolve substances at all.", False),
        ],
    },
    {
        "question_text": "When water evaporates, what happens to its temperature?", #question 14
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material",
"subtopic_order_number": 3,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the name of the process where water changes from a gas to a liquid?", #question 15
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Condensation", True),
            ("Evaporation", False),
            ("Freezing", False),
            ("Sublimation", False),
        ],
    },
    {
        "question_text": "What is the energy required to change the temperature of a substance?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material", #question 16
        "assigned_at": 1,
        "subtopic_order_number": 3,
        "difficulty_level": "Intermediate",
        "options": [
            ("Specific heat capacity", True),
            ("Latent heat", False),
            ("Enthalpy", False),
            ("Thermal conductivity", False),
        ],
    },
    {
        "question_text": "What is the difference between boiling and evaporation?", #question 17
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Boiling occurs only at the surface.", False),
            ("Evaporation is a slower process than boiling.", True),
            ("Boiling occurs at any temperature.", False),
            ("Evaporation does not involve temperature changes.", False),
        ],
    },
    {
        "question_text": "What is the term for the amount of heat required to convert a substance from a solid to a liquid?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change", #question 18
"subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Latent heat of fusion", True),
            ("Latent heat of vaporization", False),
            ("Specific heat", False),
            ("Sublimation heat", False),
        ],
    },
    {
        "question_text": "What is the name of the process where a substance changes directly from a solid to a gas?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 19
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Sublimation", True),
            ("Melting", False),
            ("Freezing", False),
            ("Condensation", False),
        ],
    },
    {
        "question_text": "What happens to the water temperature when ice is added?", #question 20
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature",
"subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("It increases.", False),
            ("It stays the same.", False),
            ("It decreases.", True),
            ("It fluctuates.", False),
        ],
    },
    {
        "question_text": "What is the term used for the heat required to change a liquid to a gas?", #question 21
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
"subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Latent heat of vaporization", True),
            ("Latent heat of fusion", False),
            ("Specific heat", False),
            ("Heat of reaction", False),
        ],
    },
    {
        "question_text": "What is the unit of heat?", #question 22
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
"subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Joule", True),
            ("Kelvin", False),
            ("Newton", False),
            ("Celsius", False),
        ],
    },
    {
        "question_text": "Which of the following gases is most commonly used for refrigeration?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 23
        "subtopic_order_number": 3,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Carbon dioxide", False),
            ("Freon", True),
            ("Nitrogen", False),
            ("Oxygen", False),
        ],
    },
    {
        "question_text": "Which of the following gases is used to pressurize soft drinks?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 1, #question 24
        "difficulty_level": "Beginner",
        "options": [
            ("Oxygen", False),
            ("Carbon dioxide", True),
            ("Nitrogen", False),
            ("Helium", False),
        ],
    },
    {
        "question_text": "What is the process of transferring heat through direct contact?",
        "topic": "Thermodynamics",
"topic_order": 1,
        "subtopic": "Nature of temperature", #question 25
"subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Conduction", True),
            ("Convection", False),
            ("Radiation", False),
            ("Insulation", False),
        ],
    },
    {
        "question_text": "What is the term for the energy required to raise the temperature of a substance?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Specific heat", True), #question 26
            ("Latent heat", False),
            ("Thermal conductivity", False),
            ("Heat capacity", False),
        ],
    },
]

# for question_data in questions_data:
#     question = Question.objects.create(
#         question_text=question_data["question_text"],
#         topic=question_data["topic"],
#         subtopic=question_data["subtopic"],
#         assigned_at=question_data["assigned_at"],
#         difficulty_level=question_data["difficulty_level"],
#     )
#     for option_text, is_correct in question_data["options"]:
#         Option.objects.create(
#             question=question, option_text=option_text, is_correct=is_correct
#         )

for question_data in questions_data:
    if "topic_order" in question_data:
        topic_obj, _ = Topic.objects.get_or_create(topic_order=question_data["topic_order"], defaults={"topic_name": question_data["topic"]})
    else:
        topic_obj, _ = Topic.objects.get_or_create(topic_name=question_data["topic"])
    if "subtopic_order_number" in question_data:
        subtopic_obj, _ = Subtopic.objects.get_or_create(subtopic_order_number=question_data["subtopic_order_number"], defaults={"subtopic_name": question_data["subtopic"], "topic": topic_obj})
    else:
        subtopic_obj, _ = Subtopic.objects.get_or_create(subtopic_name=question_data["subtopic"], topic=topic_obj)
    question = Question.objects.create(
        question_text=question_data["question_text"],
        topic=topic_obj,
        subtopic=subtopic_obj,
        assigned_at=question_data["assigned_at"],
        difficulty_level=question_data["difficulty_level"],
    )
    print(f"Inserted Question ID: {question.question_id}, Text: {question.question_text}")
    for option_text, is_correct in question_data["options"]:
        Option.objects.create(
            question=question,
            option_text=option_text,
            is_correct=is_correct
        )
