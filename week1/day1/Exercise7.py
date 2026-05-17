# Ask the user for a number between 1 and 100

# If the number is a divisible by three, print Fizz

# If the number is a divisible by five, print Buzz.

# If the number is a divisible by both three and five, print FizzBuzz instead.

numbr = int(input(" give me anumber between 1 and 100:"))
if numbr % 3 == 0 and numbr % 5 == 0:
    print("FizzBuzz")
elif numbr % 5 == 0:
    print("Buzz")
elif numbr % 3 == 0:
    print("Fizz")

15
