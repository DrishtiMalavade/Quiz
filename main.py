import random

choicess = ["1", "2", "3",]
print("welcome to the quiz game")
user = input("do you want to play? ")
if user == "no":
    print('aw sucks :(')
    quit()
else:
    print('lets play :)')
    

# Define a list of questions with choices and correct answers
questions = [
    {
        "question": "How many versions of \"Sunflowers\" did Vincent Van Gogh create?",
        "choices": ["Five", "Three", "Seven"],
        "answer": "Seven"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Earth"],
        "answer": "Mars"
    },
    {
        "question": "Which planet is known as the \"Morning Star\" and the \"Evening Star\" due to its visibility at sunrise and sunset?",
        "choices": ["Mars", "Venus", "Mercury"],
        "answer": "Venus"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Who is the author of the book \"Crime and Punishment\"?",
        "choices": ["Fyodor Dostoevsky", "Leo Tolstoy", "Marcel Proust"],
        "answer": "Fyodor Dostoevsky"
    },
    {
        "question": "What is the closest star to Earth?",
        "choices": ["Sirius", "Proxima Centauri", "Earth"],
        "answer": "Proxima Centauri"
    },
    {
        "question": "What is the term for a group of stars that form a recognizable pattern in the night sky?",
        "choices": ["Nebula", "Constellation", "Galaxy"],
        "answer": "Constellation"
    },
    {
        "question": "Who famously flew too close to the sun with wax wings, leading to his downfall?",
        "choices": ["Daedalus", "Icarus", "Orpheus"],
        "answer": "Icarus"
    },
    {
        "question": " Who was cursed to turn everything he touched into gold, a power known as the \"Golden Touch\"?",
        "choices": ["King Minos", "King Aegeus", "King Midas"],
        "answer": "King Midas"
    },
    {
        "question": "Who wrote the play \"Romeo and Juliet\"?",
        "choices": ["Charles Dickens", "Jane Austen", "William Shakespeare"],
        "answer": "Mars"
    },
    
]

# Initialize the score
score = 0  # Added

# Function to select and display a random question
def ask_question():
    global score  # Added
    question = random.choice(questions)
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}. {choice}")
    
    user_answer = input("Enter the number of your answer: ")
    
    if user_answer not in choicess:
        while True:
            print("please enter a valid choice")
            user_answer = input("Please enter 1, 2, or 3: ")
            if user_answer in choicess:
                break
    else:
        choice = int(user_answer)
        
#accidently used return choice here do not do that
    
    if question["choices"][int(user_answer) - 1] == question["answer"]:
        print("Correct!")
        score += 1  # Added
    else:
        print("Wrong. The correct answer is:", question["answer"])

# Number of questions to ask
num_questions = 5

# Call the ask_question function to start the quiz
for _ in range(num_questions):
    ask_question()
  
# Display the final score
print(f"Your score: {score}/{num_questions}")  # Added