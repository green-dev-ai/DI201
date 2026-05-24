# class Dog:
#     pass


# peanut = Dog()

# peanut.color = "brown"
# peanut.name = "peanut butter"

# print(peanut)  # memory addres
# print(peanut.color) 
# print(peanut.name) 


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)
  
  def change_name(self, new_name):
    self.name = new_name
    print("Hello my name is " + self.name)


first_person = Person("John", 36)
first_person.show_details()

first_person.change_name("Joe")



