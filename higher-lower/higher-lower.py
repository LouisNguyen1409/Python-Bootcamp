from art import logo, vs
from game_data import data
from random import choice
from lib import clear
score = 0
object_higher = choice(data)
loop = True

while loop == True:
    print(logo)
    if score != 0:
        print(f"You are right! Current score {score}.")
    object_a = object_higher
    print(f"Compare A: {object_a['name']}, {object_a['description']}, from {object_a['country']}.")
    object_b = choice(data)
    while object_a == object_b:
        object_b = choice(data)

    print(vs)
    print(f"Against B: {object_b['name']}, {object_b['description']}, from {object_b['country']}.")

    if object_a['follower_count'] > object_b['follower_count']:
        answer = "a"
        object_higher = object_a
    elif object_a['follower_count'] < object_b['follower_count']:
        answer = "b"
        object_higher = object_b

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess != answer:
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")
        loop = False
    else:
        clear()
        loop = True
        score += 1