class NameOfClass():
    def __init__(self,param1,param2):
        self.param1 = param1
        self.param2 = param2

    def method(self):
        print(self.param1)


class Sample():
    pass

my_sample = Sample()

class Dog:
    species = 'mammal'
    all_dog_names = []

    def __init__(self, breed, name, spots=False):
        self.breed = breed
        self.name = name
        self.spots = spots
        Dog.all_dog_names.append(name)

    def bark(self, number):
        return f"{self.name} says: Woof! " * number

    def describe(self):
        spot_status = "has spots" if self.spots else "does not have spots"
        return f"This is {self.name}, a {self.breed}. It is a {self.species} and {spot_status}."

    def change_name(self, new_name):
        old_name = self.name
        self.name = new_name
        if old_name in Dog.all_dog_names:
            Dog.all_dog_names.remove(old_name)
        Dog.all_dog_names.append(new_name)


my_dog = Dog(breed='Lab', name='Sammy')
your_dog = Dog(breed='Husky', name='Lucy', spots=True)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)

print(your_dog.name)
print(your_dog.species)

print(Dog.species)
print(Dog.all_dog_names)

print(my_dog.bark(2))
print(your_dog.describe())

my_dog.change_name('Max')
print(my_dog.name)
print(Dog.all_dog_names)



