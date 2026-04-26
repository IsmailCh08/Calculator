number = 0
operation = 0
number_2 = 0
def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y

operation_lookup = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

while True:
    number = input("Enter a number (or 'quit' to exit): ")
    if number == "quit":
        break
    number = float(number)
    operation = input("Enter an operation (+, -, *, /): ")
    if operation not in ["+", "-", "/", "*"]:
        print("Invalid operation. Please try again.")
    number_2 = input("Enter second number (or 'quit' to exit): ")
    number_2 = float(number_2)
    break

if operation in operation_lookup:
    used_Operation = operation_lookup[operation]
    result = used_Operation(number, number_2)
    print(result)

        
