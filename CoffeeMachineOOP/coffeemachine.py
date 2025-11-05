# File for Coffee Machine class

class CoffeMachine:
    def __init__(self, milk, water, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def report(self):
        return f"Milk: {self.milk}ml\nWater: {self.water}ml\nCoffee: {self.coffee}gr\nMoney: ${self.money}"

    def check_ingridients(self, milk_amount, water_amount, coffee_amount, money_amount):
        missing_ingridients = []
        if milk_amount > self.milk:
            missing_ingridients.append('milk')
        if water_amount > self.water:
            missing_ingridients.append('water')
        if coffee_amount > self.coffee:
            missing_ingridients.append('coffee')
        if money_amount > self.money:
            missing_ingridients.append('money')

    def consume_ingridients(self, milk_amount, water_amount, coffee_amount, money_amount):
        self.milk =- milk_amount
        self.water =- water_amount
        self.coffee =- coffee_amount
        self.money =- money_amount
