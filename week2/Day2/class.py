class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barked, WAF !")

my_dog = Dog("hudson")

print(my_dog.name)
my_dog.bark()

fish= Animal("fred")
print(fish.name)

# fish don't bark (only Dogs)
# fish.bark()








