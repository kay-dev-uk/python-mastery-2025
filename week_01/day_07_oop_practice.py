
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")

    def get_human_years(self):
        print(self.age * 7)


my_dog = Dog("Rex", 4)

other_dog = Dog("Lucy", 7)


my_dog.bark()
print(my_dog.name)
my_dog.get_human_years()
other_dog.get_human_years()
