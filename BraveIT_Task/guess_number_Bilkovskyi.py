#!/usr/bin/env python3
# Bilkovskyi Oleksandr


import random


def guess_number():
    secret_namber = random.randint(1,100)
    iterations = 0
    max_try = 7
    print("I thought of a number, try to guess it")
    
    while True:
        try:
            guess = int(input("Your number:"))
        except ValueError:
            print("Incorrect enter")
            continue

        iterations += 1

        if guess == secret_namber:
            print(f"Its impossible YOU find number {secret_namber} for {iterations} try ")
            break
        elif guess > secret_namber:
            print(f"Your number {guess} lot then my ")
        else:
            print(f"Your number {guess} less then my")
        if iterations >= max_try:
            print(f"Your try finished")
            break


if __name__ == '__main__':
    guess_number()


