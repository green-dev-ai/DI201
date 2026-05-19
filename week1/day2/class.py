# Given this list:


# list1 = [5, 10, 15, 20, 25, 50, 20]


# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


# Hint : Look at the index method

# Expected output:
# list1 = [5, 10, 15, 200, 25, 50, 20]

list1 = [5, 10, 15, 20, 25, 50, 20]

if list1.index(20) != False:
    list1[list1.index(20)] = 200

# print(list1)


# -------

# Unpack the following tuple into 4 variables


# a_tuple = (10, 20, 30, 40)

a_tuple = (10, 20, 30, 40)

a, b, c, d = a_tuple

print(a)
print(b)
print(c)
print(d)


# Accept a number from the user and print its multiplication table

number = int(input("provide a number:"))

for i in range(1,int(number/2)+1):
    if number % i == 0:
        print(i)

