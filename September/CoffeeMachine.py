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
    
    def check_ingridients(drink):
        missing_ingridients = ""

        if milk - data[drink]["milk"] < 0:
            missing_ingridients + "milk"

        if water - data[drink]["water"] < 0:
            "water" if missing_ingridients == "" else ", water"
        
        if coffee - data[drink]["coffee"] < 0:
            "coffee" if missing_ingridients == "" else ", coffee"
        
        return(True if missing_ingridients == "" else False)
    
    def make_a_coffee(name):
        # Check if there are enough ingridients
        check_ingridients(name)
         

        print(data[name]["milk"])

    keep_playing = True

    while keep_playing:
        user_choice = input("What would you like?(Espresso, Capuccino, Latte):\n").lower()

        if user_choice == "report":
            print(report)
        
        elif user_choice == "espresso" or user_choice == "capuccino" or user_choice == "latte":
            make_a_coffee(user_choice)
        else:
            print("Invalid command. Please, try again.")



    return True




machine()
