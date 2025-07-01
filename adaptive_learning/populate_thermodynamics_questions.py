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
        "question_text": "What is the most likely temperature of ice-cubes stored in a refrigerator’s freezer compartment?", #question 1
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
        "question_text": "Ken takes six ice-cubes from the freezer and puts four of them into a glass of water. He leaves two on the bench-top. He stirs and stirs until the ice-cubes are much smaller and have stopped melting. What is the most likely temperature of the water at this stage?",
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
        "question_text": "The ice-cubes Ken left on the bench-top have almost melted and are lying in a puddle of water. What is the most likely temperature of these smaller ice-cubes?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 3
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
        "question_text": "On the stove is a kettle full of water. The water has started to boil rapidly. The most likely temperature of the water 1s about:",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 4
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("None of the above answers could be right.", False)
        ],
    },
    {
        "question_text": "Five minutes later, the water in the kettle is still boiling. The most likely temperature of the water now is about:",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 5
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("120 °C", False)
        ],
    },
    {
        "question_text": "What do you think is the temperature of the steam above the boiling water in the kettle?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 6
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("120 °C", False)
        ],
    },
    {
        "question_text": "Lee takes two cups of water at 40°C and mixes them with one cup of water at 10°C. What is the most likely temperature of the mixture?", #question 7
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("20 °C", False),
            ("25 °C", False),
            ("30 °C", True),
            ("50 °C", False)
        ],
    },
    {
        "question_text": "Jim believes he must use boiling water to make a cup of tea. He tells his friends: “I couldn’t make tea if I was camping on a high mountain because water doesn’t boil at high altitudes.” Who do you agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 8
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Joy says: “Yes it does, but the boiling water is just not as hot as it is here.”", True),
            ("Tay says: “That’s not true. Water always boils at the same temperature.”", False),
            ("Lou says: “The boiling point of the water decreases, but the water itself is still at 100 degrees.”", False),
            ("Mai says: “I agree with Jim. The water never gets to its boiling point.”", False),
        ],
    },
    {
        "question_text": "Sam takes a can of cola and a plastic bottle of cola from the refrigerator, where they have been overnight. He quickly puts a thermometer in the cola in the can. The temperature is 7°C. What are the most likely temperatures of the plastic bottle and cola it holds?", #question 9
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("They are both less than 7 °C", False),
            ("They are both equal to 7 °C", True),
            ("They are both greater than 7 °C", False),
            ("The cola is at 7 °C but the bottle is greater than 7 °C", False),
            ("It depends on the amount of cola and/or the size of the bottle.", False),
        ],
    },
    {
        "question_text": "A few minutes later, Ned picks up the cola can and then tells everyone that the bench top underneath it feels colder than the rest of the bench. Whose explanation do you think is best?", #question 10
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Jon says: “The cold has been transferred from the cola to the bench.”", False),
            ("Rob says: “There is no energy left in the bench beneath the can.”", False),
            ("Sue says: “Some heat has been transferred from the bench to the cola.”", True),
            ("Eli says: “The can causes heat beneath the can to move away through the bench-top.”", False),
        ],
    },
    {
        "question_text": "Pam asks one group of friends: “If I put 100 grams of ice at 0°C and 100 grams of water at 0°C into a freezer, which one will eventually lose the greatest amount of heat?\n\na) Cat says: “The 100 grams of ice.”\nb) Ben says: “The 100 grams of water.”\nc) Nic says: “Neither because they both contain the same amount of heat.”\nd) Mat says: “There’s no answer, because ice doesn’t contain any heat.”\ne) Jed says: “There’s no answer, because you can’t get water at 0°C.”\n\nWhich of her friends do you most agree with?", #question 11
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
        "subtopic_order_number": 4,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Cat says: “The 100 grams of ice.”", False),
            ("Ben says: “The 100 grams of water.”", True),
            ("Nic says: “Neither because they both contain the same amount of heat.”", False),
            ("Mat says: “There’s no answer, because ice doesn’t contain any heat.”", False),
            ("Jed says: “There’s no answer, because you can’t get water at 0°C.”", False)
        ],
    },
    {
        "question_text": "Mel is boiling water in a saucepan on the stovetop. What do you think is in the bubbles that form in the boiling water? Mostly:", #question 12
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Air", False),
            ("Oxygen and hydrogen gas", False),
            ("Water vapour", True),
            ("There’s nothing in the bubbles.", False)
        ],
    },
    {
        "question_text": "After cooking some eggs in the boiling water, Mel cools the eggs by putting them into a bowl of cold water. Which of the following explains the cooling process?", #question 13
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Temperature is transferred from the eggs to the water.", False),
            ("Cold moves from the water into the eggs.", False),
            ("Hot objects naturally cool down.", False),
            ("Energy is transferred from the eggs to the water.", True)
        ],
    },
    {
        "question_text": "Jan announces that she does not like sitting on the metal chairs in the room because “they are colder than the plastic ones.” Who do you think is right?", #question 14
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Jim agrees and says: “They are colder because metal is naturally colder than plastic.”", False),
            ("Kip says: “They are not colder, they are at the same temperature.”", True),
            ("Lou says: “They are not colder, the metal ones just feel colder because they are heavier.”", False),
            ("Mai says: “They are colder because metal has less heat to lose than plastic.”", False)
        ],
    },
    {
        "question_text": "A group is listening to the weather forecast on a radio. They hear: “... tonight it will be a chilly 5°C, colder than the 10°C it was last night...” Whose statement do you most agree with?", #question 15
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Jen says: “That means it will be twice as cold tonight as it was last night.”", False),
            ("Ali says: “That’s not right. 5°C is not twice as cold as 10°C.”", True),
            ("Raj says: “It’s partly right, but she should have said that 10°C is twice as warm as 5°C.”", False),
            ("Guy says: “It’s partly right, but she should have said that 5°C is half as cold as 10°C.”", False)
        ],
    },
    {
        "question_text": "Kim takes a metal ruler and a wooden ruler from his pencil case. He announces that the metal one feels colder than the wooden one. What is your preferred explanation?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 16
        "assigned_at": 0,
        "subtopic_order_number": 3,
        "difficulty_level": "Intermediate",
        "options": [
            ("Metal conducts energy away from his hand more rapidly than wood.", True),
            ("Wood is a naturally warmer substance than metal.", False),
            ("The wooden ruler contains more heat than the metal ruler.", False),
            ("Metals are better heat radiators than wood.", False),
            ("Cold flows more readily from a metal.", False)
        ],
    },
    {
        "question_text": "Amy took two glass bottles containing water at 20°C and wrapped them in towelling washcloths. One of the washcloths was wet and the other was dry. 20 minutes later, she measured the water temperature in each. The water in the bottle with the wet washcloth was 18°C, the water in the bottle with the dry washcloth was 22°C. The most likely room temperature during this experiment was:", #question 17
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("26°C", True),
            ("21°C", False),
            ("20°C", False),
            ("18°C", False)
        ],
    },
    {
        "question_text": "Dan simultaneously picks up two cartons of chocolate milk, a cold one from the refrigerator and a warm one that has been sitting on the bench-top for some time. Why do you think the carton from the refrigerator feels colder than the one from the bench-top? Compared with the warm carton, the cold carton -",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change", #question 18
        "subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("contains more cold.", False),
            ("contains less heat.", False),
            ("is a poorer heat conductor.", False),
            ("conducts heat more rapidly from Dan’s hand.", True),
            ("conducts cold more rapidly to Dan’s hand.", False)
        ],
    },
    {
        "question_text": "Ron reckons his mother cooks soup in a pressure cooker because it cooks faster than in a normal saucepan but he doesn’t know why. [Pressure cookers have a sealed lid so that the pressure inside rises well above atmospheric pressure.] Which person do you most agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 19
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("Emi says: “It’s because the pressure causes water to boil above 100°C.”", True),
            ("Col says: “It’s because the high pressure generates extra heat.”", False),
            ("Fay says: “It’s because the steam is at a higher temperature than the boiling soup.”", False),
            ("Tom says: “It’s because pressure cookers spread the heat more evenly through the food.”", False)
        ],
    },
    {
        "question_text": "Pat believes her Dad cooks cakes on the top shelf inside the electric oven because it is hotter at the top than at the bottom. Which person do you think is right?", #question 20
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Pam says that it’s hotter at the top because heat rises.", False),
            ("Sam says that it is hotter because metal trays concentrate the heat.", False),
            ("Ray says it’s hotter at the top because the hotter the air the less dense it is.", True),
            ("Tim disagrees with them all and says that it’s not possible to be hotter at the top.", False)
        ],
    },
    {
        "question_text": "Bev is reading a multiple-choice question from a textbook: “Sweating cools you down because the sweat lying on your skin…” Which answer would you tell her to select?", #question 21
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("wets the surface, and wet surfaces draw more heat out than dry surfaces.", False),
            ("drains heat from the pores and spreads it out over the surface of the skin.", False),
            ("is the same temperature as your skin but is evaporating and so is carrying heat away.", False),
            (
            "is slightly cooler than your skin because of evaporation and so heat is transferred from your skin to the sweat.",
            True)
        ],
    },
    {
        "question_text": "When Zac uses a bicycle pump to pump up his bike tyres, he notices that the pump becomes quite hot. Which explanation below seems to be the best one?", #question 22
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Energy has been transferred to the pump.", True),
            ("Temperature has been transferred to the pump.", False),
            ("Heat flows from his hands to the pump.", False),
            ("The metal in the pump causes the temperature to rise.", False)
        ],
    },
    {
        "question_text": "Why do we wear sweaters in cold weather?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 23
        "subtopic_order_number": 3,
        "assigned_at": 0,
        "difficulty_level": "Intermediate",
        "options": [
            ("To keep cold out.", False),
            ("To generate heat.", False),
            ("To reduce heat loss.", True),
            ("All three of the above reasons are correct.", False)
        ],
    },
    {
        "question_text": "Vic takes some popsicles from the freezer, where he had placed them the day before, and tells everyone that the wooden sticks are at a higher temperature than the ice part. Which person do you most agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 0, #question 24
        "difficulty_level": "Beginner",
        "options": [
            ("Deb says: “You’re right because the wooden sticks don’t get as cold as ice does.”", False),
            ("Ian says: “You're right because ice contains more cold than wood does.”", False),
            ("Ros says: “You’re wrong, they only feel different because the sticks contain more heat.”", False),
            ("Ann says: “I think they are at the same temperature because they are together.”", True)
        ],
    },
    {
        "question_text": "Gay is describing a TV segment she saw the night before: “I saw physicists make super-conductor magnets, which were at a temperature of —260 °C.” Who do you think is right?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature", #question 25
        "subtopic_order_number": 1,
        "assigned_at": 0,
        "difficulty_level": "Beginner",
        "options": [
            ("Joe doubts this: “You must have made a mistake. You can’t have a temperature as low as that.”", False),
            ("Kay disagrees: “Yes you can. There’s no limit on the lowest temperature.”", False),
            ("Leo believes he is right: “I think the magnet was near the lowest temperature possible.”", True),
            (
            "Gay is not sure: “I think super-conductors are good heat conductors so you can’t cool them to such a low temperature.”",
            False)
        ],
    },
    {
        "question_text": "Four students were discussing things they did as kids. The following conversation was heard: Ami: “I used to wrap my dolls in blankets but could never understand why they didn’t warm up.” Who do you agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 0, #quetion 26
        "difficulty_level": "Intermediate",
        "options": [
            ("Nic replied: “It’s because the blankets you used were probably poor insulators.”", False),
            ("Lyn replied: “It’s because the blankets you used were probably poor conductors.”", False),
            ("Jay replied: “It’s because the dolls were made of material which did not hold heat well.”", False),
            ("Kev replied: “It’s because the dolls were made of material which took a long time to warm up.”", False),
            ("Joy replied: “You’re all wrong.”", True)
        ],
    },


    #-------------------------------------------------------------------------------------------------------------------
    {
        "question_text": "What is the most likely temperature of ice-cubes stored in a refrigerator’s freezer compartment?", #question 1
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
        "question_text": "Ken takes six ice-cubes from the freezer and puts four of them into a glass of water. He leaves two on the bench-top. He stirs and stirs until the ice-cubes are much smaller and have stopped melting. What is the most likely temperature of the water at this stage?",
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
        "question_text": "The ice-cubes Ken left on the bench-top have almost melted and are lying in a puddle of water. What is the most likely temperature of these smaller ice-cubes?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point", #question 3
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
        "question_text": "On the stove is a kettle full of water. The water has started to boil rapidly. The most likely temperature of the water 1s about:",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 4
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("None of the above answers could be right.", False)
        ],
    },
    {
        "question_text": "Five minutes later, the water in the kettle is still boiling. The most likely temperature of the water now is about:",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 5
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("120 °C", False)
        ],
    },
    {
        "question_text": "What do you think is the temperature of the steam above the boiling water in the kettle?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation", #question 6
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("88 °C", False),
            ("98 °C", True),
            ("110 °C", False),
            ("120 °C", False)
        ],
    },
    {
        "question_text": "Lee takes two cups of water at 40°C and mixes them with one cup of water at 10°C. What is the most likely temperature of the mixture?", #question 7
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("20 °C", False),
            ("25 °C", False),
            ("30 °C", True),
            ("50 °C", False)
        ],
    },
    {
        "question_text": "Jim believes he must use boiling water to make a cup of tea. He tells his friends: “I couldn’t make tea if I was camping on a high mountain because water doesn’t boil at high altitudes.” Who do you agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",  # question 8
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Joy says: “Yes it does, but the boiling water is just not as hot as it is here.”", True),
            ("Tay says: “That’s not true. Water always boils at the same temperature.”", False),
            ("Lou says: “The boiling point of the water decreases, but the water itself is still at 100 degrees.”",
             False),
            ("Mai says: “I agree with Jim. The water never gets to its boiling point.”", False),
        ],
    },
    {
        "question_text": "Sam takes a can of cola and a plastic bottle of cola from the refrigerator, where they have been overnight. He quickly puts a thermometer in the cola in the can. The temperature is 7°C. What are the most likely temperatures of the plastic bottle and cola it holds?", #question 9
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("They are both less than 7 °C", False),
            ("They are both equal to 7 °C", True),
            ("They are both greater than 7 °C", False),
            ("The cola is at 7 °C but the bottle is greater than 7 °C", False),
            ("It depends on the amount of cola and/or the size of the bottle.", False),
        ],
    },
    {
        "question_text": "A few minutes later, Ned picks up the cola can and then tells everyone that the bench top underneath it feels colder than the rest of the bench. Whose explanation do you think is best?", #question 10
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Jon says: “The cold has been transferred from the cola to the bench.”", False),
            ("Rob says: “There is no energy left in the bench beneath the can.”", False),
            ("Sue says: “Some heat has been transferred from the bench to the cola.”", True),
            ("Eli says: “The can causes heat beneath the can to move away through the bench-top.”", False),
        ],
    },
    {
        "question_text": "Pam asks one group of friends: “If I put 100 grams of ice at 0°C and 100 grams of water at 0°C into a freezer, which one will eventually lose the greatest amount of heat?\n\na) Cat says: “The 100 grams of ice.”\nb) Ben says: “The 100 grams of water.”\nc) Nic says: “Neither because they both contain the same amount of heat.”\nd) Mat says: “There’s no answer, because ice doesn’t contain any heat.”\ne) Jed says: “There’s no answer, because you can’t get water at 0°C.”\n\nWhich of her friends do you most agree with?", #question 11
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Fusion/melting point and freezing point",
        "subtopic_order_number": 4,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Cat says: “The 100 grams of ice.”", False),
            ("Ben says: “The 100 grams of water.”", True),
            ("Nic says: “Neither because they both contain the same amount of heat.”", False),
            ("Mat says: “There’s no answer, because ice doesn’t contain any heat.”", False),
            ("Jed says: “There’s no answer, because you can’t get water at 0°C.”", False)
        ],
    },
    {
        "question_text": "Mel is boiling water in a saucepan on the stovetop. What do you think is in the bubbles that form in the boiling water? Mostly:", #question 12
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Air", False),
            ("Oxygen and hydrogen gas", False),
            ("Water vapour", True),
            ("There’s nothing in the bubbles.", False)
        ],
    },
    {
        "question_text": "After cooking some eggs in the boiling water, Mel cools the eggs by putting them into a bowl of cold water. Which of the following explains the cooling process?", #question 13
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Temperature is transferred from the eggs to the water.", False),
            ("Cold moves from the water into the eggs.", False),
            ("Hot objects naturally cool down.", False),
            ("Energy is transferred from the eggs to the water.", True)
        ],
    },
    {
        "question_text": "Jan announces that she does not like sitting on the metal chairs in the room because “they are colder than the plastic ones.” Who do you think is right?", #question 14
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Jim agrees and says: “They are colder because metal is naturally colder than plastic.”", False),
            ("Kip says: “They are not colder, they are at the same temperature.”", True),
            ("Lou says: “They are not colder, the metal ones just feel colder because they are heavier.”", False),
            ("Mai says: “They are colder because metal has less heat to lose than plastic.”", False)
        ],
    },
    {
        "question_text": "A group is listening to the weather forecast on a radio. They hear: “... tonight it will be a chilly 5°C, colder than the 10°C it was last night...” Whose statement do you most agree with?", #question 15
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Jen says: “That means it will be twice as cold tonight as it was last night.”", False),
            ("Ali says: “That’s not right. 5°C is not twice as cold as 10°C.”", True),
            ("Raj says: “It’s partly right, but she should have said that 10°C is twice as warm as 5°C.”", False),
            ("Guy says: “It’s partly right, but she should have said that 5°C is half as cold as 10°C.”", False)
        ],
    },
    {
        "question_text": "Kim takes a metal ruler and a wooden ruler from his pencil case. He announces that the metal one feels colder than the wooden one. What is your preferred explanation?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 16
        "assigned_at": 1,
        "subtopic_order_number": 3,
        "difficulty_level": "Intermediate",
        "options": [
            ("Metal conducts energy away from his hand more rapidly than wood.", True),
            ("Wood is a naturally warmer substance than metal.", False),
            ("The wooden ruler contains more heat than the metal ruler.", False),
            ("Metals are better heat radiators than wood.", False),
            ("Cold flows more readily from a metal.", False)
        ],
    },
    {
        "question_text": "Amy took two glass bottles containing water at 20°C and wrapped them in towelling washcloths. One of the washcloths was wet and the other was dry. 20 minutes later, she measured the water temperature in each. The water in the bottle with the wet washcloth was 18°C, the water in the bottle with the dry washcloth was 22°C. The most likely room temperature during this experiment was:", #question 17
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("26°C", True),
            ("21°C", False),
            ("20°C", False),
            ("18°C", False)
        ],
    },
    {
        "question_text": "Dan simultaneously picks up two cartons of chocolate milk, a cold one from the refrigerator and a warm one that has been sitting on the bench-top for some time. Why do you think the carton from the refrigerator feels colder than the one from the bench-top? Compared with the warm carton, the cold carton -",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change", #question 18
        "subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("contains more cold.", False),
            ("contains less heat.", False),
            ("is a poorer heat conductor.", False),
            ("conducts heat more rapidly from Dan’s hand.", True),
            ("conducts cold more rapidly to Dan’s hand.", False)
        ],
    },
    {
        "question_text": "Ron reckons his mother cooks soup in a pressure cooker because it cooks faster than in a normal saucepan but he doesn’t know why. [Pressure cookers have a sealed lid so that the pressure inside rises well above atmospheric pressure.] Which person do you most agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",  # question 19
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("Emi says: “It’s because the pressure causes water to boil above 100°C.”", True),
            ("Col says: “It’s because the high pressure generates extra heat.”", False),
            ("Fay says: “It’s because the steam is at a higher temperature than the boiling soup.”", False),
            ("Tom says: “It’s because pressure cookers spread the heat more evenly through the food.”", False)
        ],
    },
    {
        "question_text": "Pat believes her Dad cooks cakes on the top shelf inside the electric oven because it is hotter at the top than at the bottom. Which person do you think is right?", #question 20
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature",
        "subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Pam says that it’s hotter at the top because heat rises.", False),
            ("Sam says that it is hotter because metal trays concentrate the heat.", False),
            ("Ray says it’s hotter at the top because the hotter the air the less dense it is.", True),
            ("Tim disagrees with them all and says that it’s not possible to be hotter at the top.", False)
        ],
    },
    {
        "question_text": "Bev is reading a multiple-choice question from a textbook: “Sweating cools you down because the sweat lying on your skin…” Which answer would you tell her to select?", #question 21
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Boiling point, Liquifaction, Vaporation",
        "subtopic_order_number": 5,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("wets the surface, and wet surfaces draw more heat out than dry surfaces.", False),
            ("drains heat from the pores and spreads it out over the surface of the skin.", False),
            ("is the same temperature as your skin but is evaporating and so is carrying heat away.", False),
            (
            "is slightly cooler than your skin because of evaporation and so heat is transferred from your skin to the sweat.",
            True)
        ],
    },
    {
        "question_text": "When Zac uses a bicycle pump to pump up his bike tyres, he notices that the pump becomes quite hot. Which explanation below seems to be the best one?", #question 22
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and temperature change",
        "subtopic_order_number": 2,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Energy has been transferred to the pump.", True),
            ("Temperature has been transferred to the pump.", False),
            ("Heat flows from his hands to the pump.", False),
            ("The metal in the pump causes the temperature to rise.", False)
        ],
    },
    {
        "question_text": "Why do we wear sweaters in cold weather?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material", #question 23
        "subtopic_order_number": 3,
        "assigned_at": 1,
        "difficulty_level": "Intermediate",
        "options": [
            ("To keep cold out.", False),
            ("To generate heat.", False),
            ("To reduce heat loss.", True),
            ("All three of the above reasons are correct.", False)
        ],
    },
    {
        "question_text": "Vic takes some popsicles from the freezer, where he had placed them the day before, and tells everyone that the wooden sticks are at a higher temperature than the ice part. Which person do you most agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 1, #question 24
        "difficulty_level": "Beginner",
        "options": [
            ("Deb says: “You’re right because the wooden sticks don’t get as cold as ice does.”", False),
            ("Ian says: “You're right because ice contains more cold than wood does.”", False),
            ("Ros says: “You’re wrong, they only feel different because the sticks contain more heat.”", False),
            ("Ann says: “I think they are at the same temperature because they are together.”", True)
        ],
    },
    {
        "question_text": "Gay is describing a TV segment she saw the night before: “I saw physicists make super-conductor magnets, which were at a temperature of —260 °C.” Who do you think is right?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Nature of temperature", #question 25
        "subtopic_order_number": 1,
        "assigned_at": 1,
        "difficulty_level": "Beginner",
        "options": [
            ("Joe doubts this: “You must have made a mistake. You can’t have a temperature as low as that.”", False),
            ("Kay disagrees: “Yes you can. There’s no limit on the lowest temperature.”", False),
            ("Leo believes he is right: “I think the magnet was near the lowest temperature possible.”", True),
            (
            "Gay is not sure: “I think super-conductors are good heat conductors so you can’t cool them to such a low temperature.”",
            False)
        ],
    },
    {
        "question_text": "Four students were discussing things they did as kids. The following conversation was heard: Ami: “I used to wrap my dolls in blankets but could never understand why they didn’t warm up.” Who do you agree with?",
        "topic": "Thermodynamics",
        "topic_order": 1,
        "subtopic": "Heat transfer and material",
        "subtopic_order_number": 3,
        "assigned_at": 1, #quetion 26
        "difficulty_level": "Intermediate",
        "options": [
            ("Nic replied: “It’s because the blankets you used were probably poor insulators.”", False),
            ("Lyn replied: “It’s because the blankets you used were probably poor conductors.”", False),
            ("Jay replied: “It’s because the dolls were made of material which did not hold heat well.”", False),
            ("Kev replied: “It’s because the dolls were made of material which took a long time to warm up.”", False),
            ("Joy replied: “You’re all wrong.”", True)
        ],
    },

]

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
