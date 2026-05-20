# ------- Exercise 1
def display_message():
    """this function displays message"""
    print("I am learning about functions in Python")

# -------- Exercise 2

def favorite_book(title):
    """this function display message about my favorite book"""
    print(f"My favorite book is {title}.")

favorite_book("The Bible")

# -------- Exercise 3

def describe_city(city, country="unknown"):
    """this function describes the city and the country"""
    print(f"{city} is located in {country}")

describe_city("Tel Aviv", "Israel")

describe_city("London")

# ---------- Exercise 4

import random

def number(num):
    """this function receives an integer number between 1-100"""
    rand_num = random.randint(1,100)
    if num == rand_num:
        print(f"Success !!!")
    else:
        print(f"Fail ! Your number was: {num}. The random number was: {rand_num}")

number(50)

# ------------ Exercise 5

def make_shirt(size="large", text="I love Python"):
    """this function describes a shirt's size and written text on it"""
    print(f"The size of this shirt is {size} and the text is: {text}")


make_shirt()
make_shirt(size="medium")
make_shirt("small", "Basketball is the Best !!")
make_shirt(size="small", text="Hello !")

# ------------  Exercise 6

magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]

def show_magician(magician_names):
    """this function display the names of magicians"""
    for name in magician_names:
        print(f"{name}")

def make_great(magician_names):
    """this function adds the great to each magician name"""
    for name in magician_names:
        print(f"The Graet {name}")

show_magician(magician_names)
make_great(magician_names)

# ------------ Exercise 7

def get_random_temp():
    """this function return a random temperrature (between -10-40)"""
    return random.randint(-10,40)

def main():
    """this function get a temperature and provides an advice accordingly"""
    temp = get_random_temp()
    print(f"the temperature outside is {temp} degrees Celsius.")
    if temp < 0:
        print(f"Brrr, that's freezing! Wear some extra layers today.")
    elif temp < 16:
        print(f"Quite chilly! Don't forget your coat.")
    elif temp <= 23:
        print(f"Nice weather.")
    elif temp <= 32:
        print(f"A bit warm, stay hydrated.")
    else:
        print(f"It's really hot! Stay cool.")

main()
