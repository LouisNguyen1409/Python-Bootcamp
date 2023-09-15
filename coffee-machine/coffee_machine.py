from data import MENU, resources
cost = 0
loop = True

#FUNCTION

def print_report():
    for key in resources:
        if key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
        else:
            print(f"{key.title()}: {resources[key]}ml")
    print(f"Cost: ${cost}")

def coin_process(price):
    coins = 0
    print("Please insert coins.")
    coins += int(input("how many quarters?: ")) * 0.25
    coins += int(input("how many dimes?: ")) * 0.1
    coins += int(input("how many nickles?: ")) * 0.05
    coins += int(input("how many pennies?: ")) * 0.01
    if coins < price:
        print("Sorry that's not enough money. Money refunded.")
        return 1
    print(f"Here is ${coins - price} in change.")
    return 0

def coffee_process(coffee_type, cost):
    coffee = MENU[coffee_type]
    for key in coffee["ingredients"]:
        resources[key] -= coffee["ingredients"][key]
    cost += coffee["cost"]
    print(f"Here is your {coffee_type}. Enjoy!")
    return cost

def check_sufficient(coffee):
    for key in coffee["ingredients"]:
        if resources[key] < coffee["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            return 1
    return 0

#MAIN
while loop == True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        loop = False
    elif user_input == "report":
        print_report()
    elif user_input == "espresso":
        if check_sufficient(MENU["espresso"]) == 0:
            if coin_process(MENU["espresso"]["cost"]) == 0:
                cost = coffee_process("espresso", cost)
    elif user_input == "latte":
        if check_sufficient(MENU["latte"]) == 0:
            if coin_process(MENU["latte"]["cost"]) == 0:
                cost = coffee_process("latte", cost)
    elif user_input == "cappuccino":
        if check_sufficient(MENU["cappuccino"]) == 0:
            if coin_process(MENU["cappuccino"]["cost"]) == 0:
                cost = coffee_process("cappuccino", cost)





