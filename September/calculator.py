
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
    
    def calculate(first_num, operation, second_num):
        result = 0
    
        def add(n1, n2):
            return n1 + n2
    
        def subtract(n1, n2):
            return n1 - n2
    
        def multiply(n1, n2):
            return n1 * n2
        
        def divide(n1, n2):
            return n1 / n2

        # while keep_calculating:
        #     print("Please, ")

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
