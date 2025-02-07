from my_app.models import Question, Option

# Create 10 Thermodynamics Questions with their respective options
questions_data = [
    {
        "question_text": "What is the first law of thermodynamics?",
        "topic": "Thermodynamics",
        "difficulty_level": "Beginner",
        "options": [
            ("Energy cannot be created or destroyed", True),
            ("The total energy of the universe is constant", False),
            ("Energy is only conserved in closed systems", False),
            ("Heat is the only form of energy", False)
        ]
    },
    {
        "question_text": "What is the formula for work done by an ideal gas during an isothermal process?",
        "topic": "Thermodynamics",
        "difficulty_level": "Intermediate",
        "options": [
            ("W = P(V2 - V1)", False),
            ("W = nRT ln(V2/V1)", True),
            ("W = nR(T2 - T1)", False),
            ("W = P(V1 + V2)", False)
        ]
    },
    {
        "question_text": "Which process describes the change in energy with no heat exchange?",
        "topic": "Thermodynamics",
        "difficulty_level": "Intermediate",
        "options": [
            ("Isothermal", False),
            ("Adiabatic", True),
            ("Isobaric", False),
            ("Isochoric", False)
        ]
    },
    {
        "question_text": "What is the definition of entropy?",
        "topic": "Thermodynamics",
        "difficulty_level": "Beginner",
        "options": [
            ("A measure of heat flow", False),
            ("A measure of randomness or disorder", True),
            ("A measure of pressure", False),
            ("A measure of energy", False)
        ]
    },
    {
        "question_text": "In thermodynamics, what does a negative value for enthalpy indicate?",
        "topic": "Thermodynamics",
        "difficulty_level": "Advanced",
        "options": [
            ("The system is absorbing heat", False),
            ("The system is at equilibrium", False),
            ("The system is releasing heat", True),
            ("There is no change in the system", False)
        ]
    },
    {
        "question_text": "What does the second law of thermodynamics state?",
        "topic": "Thermodynamics",
        "difficulty_level": "Intermediate",
        "options": [
            ("Energy flows from cold to hot", False),
            ("Entropy of an isolated system always decreases", False),
            ("The total energy of a system is conserved", False),
            ("Entropy of an isolated system always increases", True)
        ]
    },
    {
        "question_text": "What is a Carnot engine?",
        "topic": "Thermodynamics",
        "difficulty_level": "Advanced",
        "options": [
            ("An engine that operates with maximum efficiency", True),
            ("An engine that works only in the isothermal process", False),
            ("An engine that works only in adiabatic process", False),
            ("An engine that converts only electrical energy", False)
        ]
    },
    {
        "question_text": "Which of the following is a state function in thermodynamics?",
        "topic": "Thermodynamics",
        "difficulty_level": "Intermediate",
        "options": [
            ("Heat", False),
            ("Work", False),
            ("Pressure", True),
            ("Time", False)
        ]
    },
    {
        "question_text": "What is the unit of specific heat capacity?",
        "topic": "Thermodynamics",
        "difficulty_level": "Beginner",
        "options": [
            ("Joule", False),
            ("Joule per kilogram", False),
            ("Joule per kilogram per Kelvin", True),
            ("Newton per meter", False)
        ]
    },
    {
        "question_text": "What does the third law of thermodynamics state?",
        "topic": "Thermodynamics",
        "difficulty_level": "Advanced",
        "options": [
            ("Entropy of a system approaches a constant as temperature approaches absolute zero", True),
            ("The energy in a system remains constant", False),
            ("Energy can be created and destroyed", False),
            ("Entropy decreases at lower temperatures", False)
        ]
    }
]

# Insert the questions and options into the database
for q_data in questions_data:
    question = Question.objects.create(
        question_text=q_data["question_text"],
        topic=q_data["topic"],
        difficulty_level=q_data["difficulty_level"]
    )

    for option_text, is_correct in q_data["options"]:
        Option.objects.create(
            question=question,
            option_text=option_text,
            is_correct=is_correct
        )

print("Dummy data for thermodynamics questions and options inserted successfully!")
