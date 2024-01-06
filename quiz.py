import tkinter as tk
from tkinter import messagebox

choicess = ["1", "2", "3"]

# Create the main window
root = tk.Tk()
root.title("Quiz Game")
root.geometry("700x300")
root.configure(bg="#333333")  # Set background color

# Define variables
score = 0
question_number = 0

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
]

# Function to check the answer and move to the next question
def check_answer(user_answer):
    global score, question_number

    if user_answer not in choicess:
        messagebox.showinfo("Invalid Choice", "Please enter 1, 2, or 3.")
        return

    choice = int(user_answer)

    if questions[question_number]["choices"][choice - 1] == questions[question_number]["answer"]:
        messagebox.showinfo("Correct!", "Your answer is correct!")
        score += 1
    else:
        correct_answer = questions[question_number]["answer"]
        messagebox.showinfo("Wrong Answer", f"Wrong. The correct answer is: {correct_answer}")

    question_number += 1
    if question_number < num_questions:
        ask_question()
    else:
        display_final_score()

# Function to ask a question
def ask_question():
    question_label.config(text=questions[question_number]["question"], fg="white", font=("Helvetica", 12, "bold"), bg="#333333")
    for i, label in enumerate(choices_labels):
        label.config(text=f"{i + 1}. {questions[question_number]['choices'][i]}", bg="#333333", fg="white", font=("Helvetica", 10))
    answer_entry.delete(0, tk.END)

# Function to display the final score
def display_final_score():
    messagebox.showinfo("Game Over", f"Your final score: {score}/{num_questions}")
    root.destroy()

# Create widgets
question_label = tk.Label(root, text="", padx=10, pady=10, bg="#333333")
choices_labels = [tk.Label(root, text="", padx=10, pady=5, bg="#333333") for _ in range(3)]
answer_entry = tk.Entry(root, width=10, font=("Helvetica", 10))
submit_button = tk.Button(root, text="Submit Answer", command=lambda: check_answer(answer_entry.get()), bg="#4285F4", fg="white", font=("Helvetica", 10, "bold"))

# Organize widgets using grid layout
question_label.grid(row=0, column=0, columnspan=2)
for i, label in enumerate(choices_labels):
    label.grid(row=i + 1, column=0, columnspan=2, sticky="w")
answer_entry.grid(row=4, column=0, pady=10)
submit_button.grid(row=4, column=1, pady=10, sticky="e")

# Number of questions to ask
num_questions = len(questions)

# Call the ask_question function to start the quiz
ask_question()

# Start the main event loop
root.mainloop()

