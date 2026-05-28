class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} barked, woof !") # class attriibutes


barky = Dog('Barkey')
barky.bark()
fido = Dog('fito')
fido.bark()

print(fido.species) # canis familiaris
print(barky.species) # canis familiaris

print(Dog.species) # canis familiaris

Dog.species = "Dog"

print(fido.species)  # Dog
print(barky.species)  # Dog

print(Dog.species)  # Dog

fido.species = "Chicken" # changed intance, not class

print(fido.species)  # Chicken
print(barky.species)  # Dog
print(Dog.species)  # Dog

