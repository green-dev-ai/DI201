# --------------Exercise 1 - Pets

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Step 1
   
class Siamese(Cat):
    def sleep(self):
        self.is_sleep = True

# Step 2
Bengal_cat = Bengal("tiger", 3)
Chartreux_cat = Chartreux("billy", 4)
Siamese_cat = Siamese("blacky", 5)
all_cats = [Bengal_cat, Chartreux_cat, Siamese_cat]

# Step 3

sara_pets = Pets(all_cats)

# Step 4

sara_pets.walk()


# -------------- Exercise 2 - Dogs

# Step 1

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return print(f"{self.name} is barking")

    def run_speed(self):
        speed = self.weight / self.age * 10
#       print(f"{self.name}'s speed is: {speed}")
        return speed


    def fight(self, other_dog):
        self.other_dog = other_dog
        result1 = self.weight * self.run_speed()
        result2 = self.other_dog.weight * self.other_dog.run_speed()
        if result1 > result2:
            return print(f"{self.name} won the fight")
        else:
            return print(f"{self.other_dog.name} won the fight")

# Step 2: Create dog instances

dog1 = Dog("Burkey", 4, 7)
dog2 = Dog("Hudson", 10, 6)
dog3 = Dog("Pepper", 5, 10)


# Step 3: Test dog methods
dog1.bark()
dog2.bark()
dog3.bark()

print(f"{dog1.name} speed is: {dog1.run_speed()}")
print(f"{dog2.name} speed is: {dog2.run_speed()}")
print(f"{dog3.name} speed is: {dog3.run_speed()}")

dog1.fight(dog2)
dog2.fight(dog3)
dog1.fight(dog3)




