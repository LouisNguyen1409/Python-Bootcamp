from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
loop = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
while loop:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}): ")
    
    if user_input == "off":
        loop = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost) == True:
                coffee_maker.make_coffee(drink)


