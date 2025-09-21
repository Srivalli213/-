import tkinter as tk
import random

def check_guess():
    try:
        user_guess = int(entry.get())
        if user_guess < number_to_guess:
            result_label.config(text="Too low! Try again.")
        elif user_guess > number_to_guess:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Correct! The number was {number_to_guess}")
    except ValueError:
        result_label.config(text="Please enter a valid integer.")

def reset_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    result_label.config(text="New game started! Guess a number between 1 and 100.")
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x200")

# Random number for first round
number_to_guess = random.randint(1, 100)

title_label = tk.Label(root, text="Guess the Number (1–100)", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="Enter a number to start guessing!", font=("Arial", 12))
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()
