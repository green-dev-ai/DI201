# --------- Exercise 1 (Cat)

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects

cat1 = Cat("baily", 3)
cat2 = Cat("hudson", 5)
cat3 = Cat("jinji", 10)

# cat1 = create the object

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    """this function finds the oldest cat's age and returns the oldest cat"""    
    if cat1.age >= cat2.age and cat1.age >= cat3.age:
        return cat1   
    elif cat2.age >= cat3.age and cat2.age >= cat1.age:
        return cat2
    elif cat3.age >= cat2.age and cat3.age >= cat1.age:
        return cat3
    else:
        print(f"There is no one cat that is the oldest")
        return "none"

# Step 3: Print the oldest cat's details

# print(f"{cat1.name}, {cat1.age}")


oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is: {oldest_cat.name} and it is {oldest_cat.age} years old.")


# -------- Exercise 2 DOGS


class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print(f"{self.name} goes Woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")

# step 2

davids_dog = Dog("river", 60)
sarahs_dog = Dog("mishmish", 34)

# step 3

print(f"Davis's dog is called: {davids_dog.name} and it is {davids_dog.height} cm high.")
print(f"Sarah's dog is called: {sarahs_dog.name} and it is {sarahs_dog.height} cm high.")

davids_dog.bark()
davids_dog.jump()

sarahs_dog.bark()
sarahs_dog.jump()

# step 4

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} if higher !")
else:
    print(f"{sarahs_dog.name} is higher !")


# ----------  Exercise 3 - song producer

# Create a Song class with a method to print song lyrics line by line.



# Step 1: Create the Song Class

# Create a class called Song.
# In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
# Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.


# Example:

# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(f"{line}")


my_song = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

my_song.sing_me_a_song()


# ---------- Exercise 4 - Zoo

class Zoo:
    def __init__(self, zoo_name, animals):
        self.name = zoo_name
        self.animals = animals

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"animal {new_animal} was added.")

    def get_animals(self):
        for animal in self.animals:
            print(f"{animal}")

    def sell_animal(self, sold_animal):
        if sold_animal in self.animals:
           self.animals.remove(sold_animal)

    def sort_animals(self):
        self.animals.sort()
        animals_groups = {
        }
        for animal in self.animals:
            first_letter = animal[0]
            if first_letter not in animals_groups:
                animals_groups[first_letter] = []
            animals_groups[first_letter].append(animal)            
        
        return animals_groups

    def get_groups(self):
        my_groups = self.sort_animals()
        for letter, animals in my_groups.items(): 
            print(f"{letter}: {animals}") 
     

CP_zoo = Zoo("Central Park Zoo",["Elephant", "Lion", "Giraffe", "Bear", "Cougar"])

CP_zoo.add_animal("Cat")
CP_zoo.add_animal("Baboon")
CP_zoo.add_animal("Tiger")

CP_zoo.get_animals()
CP_zoo.sell_animal("Wolf")
CP_zoo.sell_animal("Giraffe")
CP_zoo.get_animals()

CP_zoo.sort_animals()
CP_zoo.get_groups()
