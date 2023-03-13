# # Quiz Game

# questions = [
#     {
#         "question": "What is the capital of France?",
#         "options": ["Berlin", "Paris", "London", "Madrid"],
#         "answer": "Paris"
#     },
#     {
#         "question": "What is the largest country in the world?",
#         "options": ["Russia", "Canada", "China", "USA"],
#         "answer": "Russia"
#     },
#     {
#         "question": "What is the color of the sky?",
#         "options": ["Red", "Green", "Yellow", "Blue"],
#         "answer": "Blue"
#     }
# ]

# score = 0

# for i, question in enumerate(questions):
#     print(f"\n{i+1}. {question['question']}")
#     for j, option in enumerate(question['options']):
#         print(f"{j+1}. {option}")
#     answer = input("Your answer: ")
#     if answer.lower() == question['answer'].lower():
#         print("Correct!")
#         score += 1
#     else:
#         print(f"Incorrect! The answer is {question['answer']}")

# print(f"\nYour final score is {score}/{len(questions)}")


import random

# Define a list of questions, where each question is a dictionary
# with the following keys: 'text', 'choices', and 'answer'.
# For example:
questions = [
    {
        'text': 'What is the capital city of Pakistan?',
        'choices': ['Karachi', 'Lahore', 'Islamabad', 'Peshawar'],
        'answer': 'Islamabad'
    },

    {
        'text': 'What is the national language of Pakistan?',
        'choices': ['Urdu', 'Punjabi', 'Sindhi', 'Pashto'],
        'answer': 'Urdu'
    },

    {
        'text': 'Who is the current prime minister of Pakistan?',
        'choices': ['Imran Khan', 'Nawaz Sharif', 'Asif Ali Zardari', 'Benazir Bhutto'],
        'answer': 'Imran Khan'
    },

    {
        'text': 'What is the highest mountain in Pakistan?',
        'choices': ['Nanga Parbat', 'Gasherbrum I', 'K2', 'Broad Peak'],
        'answer': 'K2'
    },

    {
        'text': 'What is the name of the famous archaeological site in Pakistan that dates back to the Indus Valley Civilization?',
        'choices': ['Mohenjo Daro', 'Harappa', 'Taxila', 'Chanhudaro'],
        'answer': 'Mohenjo Daro'
    }, 
    {
        'text': 'What is the name of the national flag carrier airline of Pakistan?',
        'choices': ['PIA', 'Airblue', 'SereneAir', 'Shaheen Air'],
        'answer': 'PIA'
    },

    {
        'text': 'What is the name of the famous mountain range in Pakistan?',
        'choices': ['Himalayas', 'Karakoram', 'Pamir', 'Hindu Kush'],
        'answer': 'Karakoram'
    },

    {
        'text': 'What is the name of the river that flows through Pakistan?',
        'choices': ['Ganges', 'Brahmaputra', 'Indus', 'Yamuna'],
        'answer': 'Indus'
    },

    {
        'text': 'What is the name of the largest province by area in Pakistan?',
        'choices': ['Punjab', 'Sindh', 'Balochistan', 'Khyber Pakhtunkhwa'],
        'answer': 'Balochistan'
    },

    {
        'text': 'What is the name of the famous historical fort in Lahore, Pakistan?',
        'choices': ['Lahore Fort', 'Shalimar Gardens', 'Badshahi Mosque', 'Hiran Minar'],
        'answer': 'Lahore Fort'
    }
    # add more questions here
]

# Define a function to ask a single question
def ask_question(question):
    # Print the question text
    print(question['text'])
    
    # Shuffle the answer choices
    random.shuffle(question['choices'])
    
    # Print the answer choices
    for i, choice in enumerate(question['choices']):
        print(f"{i + 1}. {choice}")
    
    # Ask the user for their answer
    user_answer = input("Enter the number of your answer: ")
    
    # Check if the user's answer is correct
    if question['choices'][int(user_answer) - 1] == question['answer']:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")
        return False

# Define a function to play the entire game
def play_game(questions):
    # Shuffle the questions
    random.shuffle(questions)
    
    # Keep track of the user's score
    score = 0
    
    # Ask each question in turn
    for question in questions:
        if ask_question(question):
            score += 1
    
    # Print the final score
    print(f"You got {score} out of {len(questions)} questions correct.")

# Play the game
play_game(questions)

