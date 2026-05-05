def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "undefined"
    else:
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
    while True:
        number = input("Enter a number (or 'quit' to exit): ")
        if number == "quit":
            break
        try:
            number = float(number)
        except ValueError:
            print("Not an integer")
        

    while True:
        operation = input("Enter an operation ( +, -, *, / ): ")
        if operation not in ["+", "-", "/", "*"]:
            print("Invalid operation. Please try again.")
        else:
            break
        
    while True:
        number_2 = input("Enter your second number (or 'quit' to exit): ")
        if number_2 == "quit":
            break
        try:
            number_2 = float(number_2)
        except ValueError:
            print("Not an integer")

    if operation in operation_lookup:
        used_Operation = operation_lookup[operation]
        result = used_Operation(number, number_2)
        print(result)        
