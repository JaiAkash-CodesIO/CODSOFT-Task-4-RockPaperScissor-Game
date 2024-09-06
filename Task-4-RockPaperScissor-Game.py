import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play_round(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=('Arial', 14))
instructions_label.pack(pady=10)

rock_button = tk.Button(root, text="Rock", font=('Arial', 14), width=10, command=lambda: play_round("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=('Arial', 14), width=10, command=lambda: play_round("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=('Arial', 14), width=10, command=lambda: play_round("Scissors"))
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer Score: {computer_score}", font=('Arial', 14))
score_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
