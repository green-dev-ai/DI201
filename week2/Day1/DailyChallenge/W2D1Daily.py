# --------------------- W2D1 Daily Challenge

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        
        print(f"{self.name} :")
        print("--------------\n")
        for animal, count in self.animals.items():
            print(f"{animal}    {count}")
        print(f"\n  E-I-E-I-O!")


my_farm = Farm("My Farm")

my_farm.add_animal("Horse", 3)
my_farm.add_animal("Cow", 15)
my_farm.add_animal("Sheep", 33)
my_farm.add_animal("Cow", 8)
my_farm.add_animal("Horse",)
my_farm.add_animal("Sheep",)

my_farm.get_info()
