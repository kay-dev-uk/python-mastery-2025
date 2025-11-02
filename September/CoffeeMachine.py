# Default report:
# 300ml Water
# 200ml Milk
# 100gr COffee
# Money $0

# Espress - 50ml water 18gr coffee 1.50
# Cappucino - 250ml water 24gr coffee 100ml milk 3.00
# Latte - 200ml water 24gr coffee 150ml Milk 2.50

# Penny - 0.01 , dime - 0.10, nickel - 0.05, quarter - 0.25

# report func - return report on ingridients
# ask what user would like (3 options)
# 4 questions one for each coin type?
# check how many ingridients left after each drink

def machine():

    milk = 200
    water = 300
    coffee = 100
    money = 0

    data = {"espresso": {"milk": 0, "water": 50, "coffee": 18, "price": 1.50}, "cappucino": {"milk": 100, "water": 250, "coffee": 24, "price": 3.00}, "latte": {"milk": 150, "water": 200, "coffee": 24, "price": 2.50}}

    def report():
        return f"Milk: {milk}ml\nWater: {water}ml\nCoffee: {coffee}gr\nMoney: ${money}"
    
    def insert_coins(coin, amount):
        nonlocal money
        if coin == "penny":
            money += (0.01 * amount)
        elif coin == "dime":
            money += (0.05 * amount)
        elif coin == "nickel":
            money += (0.10 * amount)
        elif coin == "quarter":
            money += (0.25 * amount)
    
    def check_ingridients(drink):
        missing_ingridients = []

        if milk < data[drink]["milk"]:
            missing_ingridients.append("milk")

        if water < data[drink]["water"]:
            missing_ingridients.append("water")
        
        if coffee < data[drink]["coffee"]:
            missing_ingridients.append("coffee")
        
        if missing_ingridients:
            print(f"Sorry, there is not enough {', '.join(missing_ingridients)}.")
            return False
        else:
            return True
    
    def make_a_coffee(name):
        # Check if there are enough ingridients
        nonlocal milk, water, coffee, money
        if check_ingridients(name) == True:


            while money < data[name]["price"]:
                print("Not enough balance! Please, insert more coins")
                insert_coins("penny", int(input("How many pennies: ")))
                insert_coins("dime", int(input("How many dimes: ")))
                insert_coins("nickel", int(input("How many nickels: ")))
                insert_coins("quarter", int(input("How many quarters: ")))
            money -= data[name]["price"]
            milk -= data[name]["milk"]
            water -= data[name]["water"]
            coffee -= data[name]["coffee"]

    keep_playing = True

    while keep_playing:
        user_choice = input("What would you like?(Espresso, Capuccino, Latte):\n").lower()

        if user_choice == "report":
            print(report())
        
        elif user_choice == "espresso" or user_choice == "capuccino" or user_choice == "latte":
            make_a_coffee(user_choice)
            print(f"Here is your {user_choice}. Enjoy!")
        else:
            print("Invalid command. Please, try again.")



    return True




machine()
