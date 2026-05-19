
#---------- Challenge 1

# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.


number = int(input("please provide a number: "))
length = int(input("please provide the length of the multiples: "))
numbers_list = []
i = 1
while i <= length:
    numbers_list.append(number * i)
    i += 1
print(numbers_list)


#------------ Challenge 2

# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.

# The new string should only contain unique consecutive letters.
# For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

string = input("please provice a string with duplicates: ")

i = 0
while i < (len(string)-1):
    if string[i] == string[i+1]:
        string = string[:i] + string[i+1:]
    i += 1

print(string)


