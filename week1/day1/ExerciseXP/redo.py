# Print the following output using one line of code:

print("hello world \n"*4)

# Write code that calculates the result of:

# (99^3)*8 (meaning 99 to the power of 3, times 8).

number = (99 ** 3) * 8
print(number)

# Predict the output of the following code snippets:
# Coment what is your guess, then run the code and compare

5 < 3  # False
3 == 3  # True
3 == "3"   # True
int("3") > 3  # False
"Hello" == "hello" # False

5 < 3
3 == 3
3 == "3"
int("3") > 3
"Hello" == "hello"

# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable, print a sentence that states the following:
# "I have a <computer_brand> computer."

computer_brand = "Dell"
print(f"I have a {computer_brand} computer")

# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
# Have your code print the info message.
# Run your code.

name = "Joe"
age = "54"
shoe_size = "43"
info = f"I am {age} years old, and When I play Basketball I were shoes size {shoe_size}, and all my friends call me {name} show during the game."
print(info)

# Create two variables, a and b.
# Each variable’s value should be a number.
# If a is bigger than b, have your code print "Hello World"

a = 13
b = 10
if a > b:
    print("Hello World")

# Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Please enter a number :"))
if num % 2 == 0:
    print("you've selected an even number")
else:
    print("you've selected an odd number")
    

# Write code that asks the user for their name and determines whether or not you have the same name. Print out a funny message based on the outcome.

user_name = input("please write your name :")
if user_name == "Joe":
    print(f"Amazing !!! we are both called {user_name}")
else:
    print(" You lose !!! we don't have the same name")
    

# Write code that will ask the user for their height in centimeters.
# If they are over 145 cm, print a message that states they are tall enough to ride.
# If they are not tall enough, print a message that says they need to grow some more to ride.

user_height = int(input("What is you height in centimeters :"))
if user_height >= 145:
    print("you are tall enough to ride")
else:
    print("you need to grow some more before you can ride here")
