from lib import clear
from art import logo


def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return round(num_1 / num_2)

operation_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
} 
reuse = 'n'
while True: 
    if reuse == 'n':
        print(logo)
        num_1 = float(input("What is the first number?: "))
        for key in operation_dict:
            print(key)
        result = num_1
    operation = input("Pick an operation: ")
    num_2 = float(input("What is the next number?: "))
    pre_result = result
    function = operation_dict[operation]
    result = function(pre_result, num_2)

    print(f"{pre_result} {operation} {num_2} = {result}")

    reuse = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if reuse == 'n':
        clear()