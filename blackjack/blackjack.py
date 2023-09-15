from art import logo
from random import choice
from lib import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
loop = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def sum_cards(list_cards):
    sum = 0
    for card in list_cards:
        sum += card
    return sum

def computer_process(list_cards):
    while sum_cards(list_cards) < 17:
        list_cards.append(choice(cards))
    if sum_cards(list_cards) > 21 and 11 in list_cards:
        pos = list_cards.index(11)
        list_cards[pos] = 1
        computer_process(list_cards)
    return list_cards


while loop == "y":
    clear()
    print(logo)
    your_card = []
    computer_card = []
    your_card.append(choice(cards))
    computer_card = computer_process(computer_card)
    user_decision = "y"
    while user_decision == "y":
        your_card.append(choice(cards))
        print(f"Your cards: {your_card}, current score: {sum_cards(your_card)}")
        print(f"Computer's first card: {computer_card[0]}")
        if sum_cards(your_card) > 21:
            user_decision = "n"
        else:
            user_decision = input("Type 'y' to get another card, type 'n' to pass: ")
    print(f"Your final hand: {your_card}, final score: {sum_cards(your_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum_cards(computer_card)}")

    if sum_cards(your_card) == sum_cards(computer_card):
        print("Draw 🙃")
    elif sum_cards(computer_card) == 21:
        print("You lose 😭")
    elif sum_cards(your_card) == 21:
        print("You win 😃")
    elif sum_cards(your_card) > 21:
        print("You went over. You lose 😭")
    elif sum_cards(computer_card) > 21:
        print("You win 😃")
    elif sum_cards(computer_card) > sum_cards(your_card):
        print("You lose 😭")
    elif sum_cards(your_card) > sum_cards(computer_card):
        print("You win 😃")
    loop = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")