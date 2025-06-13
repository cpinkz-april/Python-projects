import random

computer_random = random.randint(1, 100)
attempts = 0
guess_number = input("Enter the number to guess from 1-100: ")

if int(guess_number) == computer_random:
    print("You win! You make the correct guess.")
elif int(guess_number) != computer_random:
    while True:
        if int(guess_number) > computer_random:
            print("Too high")
            guess_number = input("Enter the number to guess from 1-100: ")
            attempts += 1
            print(f"Attempts = {attempts}")
        elif int(guess_number) < computer_random:
            print("Too low")
            guess_number = input("Enter the number to guess from 1-100: ")
            attempts += 1
            print(f"Attempts = {attempts}")
        elif int(guess_number) == computer_random:
            print("You win! You make the correct guess.")
            attempts += 1
            print(f"Attempts = {attempts}")
