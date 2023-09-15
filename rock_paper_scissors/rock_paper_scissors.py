rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_img = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!")
else :
    print(game_img[user_input])

    computer_choice = random.randint(0, 2)

    print(game_img[computer_choice])


    if user_input == computer_choice:
        print("Draw.")
    elif user_input == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice == 0 and user_input == 2:
        print("You lose.")
    elif user_input < computer_choice:
        print("You lose.")
    elif user_input > computer_choice:
        print("You win.")
    if user_input >= 3 or user_input < 0:
        print("You typed an invalid number, you lose!")