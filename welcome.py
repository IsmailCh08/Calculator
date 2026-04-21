number = 0
operation = 0

def add(x,y):
    x + y

def multiply(x,y):
    x * y

def divide(x,y):
    x/y

def subtract(x,y):
    x-y

operation_lookup = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

while number != "quit":
    number = input("Enter a number (or 'quit' to exit): ")
    number = int(number)
    operation = input("Enter an operation (+, -, *, /): ")
    if operation != ["+", "-", "/", "*"]:
        print("Invalid operation. Please try again.")
        
