
# Prompt for the first num
# Show different options(+ - * /)
# Prompt user to pick one
# Prompt for second num
# Show Result
# Prompt for continuing using the same result number or not
# loop again

def calculator():
    "Welcome to calculator!"

    keep_calculating = True
    first_num = input("What's the first number: ")
    def calculate(first_number, second_number, operation):
        def add(n1, n2):
            return n1 + n2
        def subtract(n1, n2):
            return n1 - n2
        def multiply(n1, n2):
            return n1 * n2    
        def divide(n1, n2):
            return n1 / n2
        if operation == "+":
            return add(first_number, second_number)
        elif operation == "-":
            return subtract(first_number, second_number)
        elif operation == "*":
            return multiply(first_number, second_number)
        elif operation == "/":
            return divide(first_number, second_number)

    while keep_calculating:
        print("+\n-\n*\n/")
        op = input("Pick an operation: ")
        second_num = int(input("What's the second number: "))
        result = calculate(first_num, second_num, op)
        print(f"{first_num} {op} {second_num} = {result}")

        user_choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if user_choice == 'y':
            first_num = result
        else:
            first_num = int(input("What's the first number: "))

calculator()

# CHALLENGE
# def is_leap_year(year):

#     if year % 4 != 0:
#         return False
#     if year % 100 != 0:
#         return True
#     if year % 400 != 0:
#         return False
#     return True


# print(is_leap_year(2100))
