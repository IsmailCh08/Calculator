number_1 = input("First number: ")
operation_1 = input("What operation do you want to do? Enter +, -, %, *: ")
number_2 = input("Second number: ")

number_1 = int(number_1)
number_2 = int(number_2)

if operation_1 == '+':
    print(number_1 + number_2)
elif operation_1 == '-':
    print(number_1 - number_2)
elif operation_1 == '*':
    print(number_1 * number_2)
elif operation_1 == '%':
    print(number_1 % number_2)
else:
    print("invalid character")