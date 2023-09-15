from lib import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")
info = {}
loop = "yes"
while loop == "yes":
    name_input = input("What is your name?: ")
    bid_input = int(input("What is your bid?: $"))
    info[name_input] = bid_input
    loop = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()

max = 0
for key in info:
    bid = info[key]
    if bid > max:
        max = bid
        person = key
print(f"The winner is {person} with a bid of ${max}.")