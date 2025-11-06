#!/usr/bin/env python3
# Bilkovskyi Oleksandr


import random

options = ["Rock", "Scissors", "Paper" ]

user = input("Your choice: Rock, Scissors, Paper ")

computer = random.choice(options)

print(f"\nYour choice : {user}")
print(f"Computer choice: {computer}")

if user == computer:
    print("Draw")
elif (
    (user == "Rock" and computer == "Scissors") or
    (user == "Scissors" and computer == "Paper") or
    (user == "Paper" and computer == "Rock")
):
    print("You Win!")
elif user in options:
    print("You Lose")
else:
    ptint("Incorrect enter")