
# Prompt for the first num
# Show different options(+ - * /)
# Prompt user to pick one
# Prompt for second num
# Show Result
# Prompt for continuing using the same result number or not
# loop again

# def calculator():
#     "Welcome to calculator!"

#     keep_calculating = True
    
#     def calculate(first_num, operation, second_num):
#         result = 0
#         if operation == "+":
#             first_num 

#         return()
#         while keep_calculating:
#             print("Please, ")

# CHALLENGE
def is_leap_year(year):

    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 != 0:
        return False
    return True


print(is_leap_year(2100))
