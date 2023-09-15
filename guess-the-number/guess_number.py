#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    lives = 10
else:
    lives = 5
destination = randint(1, 100)
print(f"Cheat {destination}")
while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > destination:
        print("Too high.")
        print("Guess again.")
        lives -= 1
    elif guess < destination:
        print("Too low.")
        print("Guess again.")
        lives -= 1
    elif guess == destination:
        print(f"You got it! The answer was {destination}.")
        lives = -1

if lives == 0:
    print("You've run out of guesses, you lose.")