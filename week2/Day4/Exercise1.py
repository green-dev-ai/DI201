# Read the file line by line
# Read only the 5th line of the file
# Read only the 5 first characters of the file
# Read all the file and return it as a list of strings. Then split each word into letters
# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
# Append your first name at the end of the file
# Append "SkyWalker" next to each first name "Luke"

# Read the file line by line
with open('names.txt', 'r') as file:
    for line in file:
       print(line.strip())
print("_______")

# Read only the 5th line of the file
with open('names.txt', 'r') as file:
    fifth_line = file.readlines()[4] # index starts at 0
    print(fifth_line.strip())
print("_______")

# Read only the 5 first characters of the file
with open('names.txt', 'r') as file:
    first_five = file.read(5) 
    print(first_five.strip())  
    print("_______")

# Read all the file and return it as a list of strings. Then split each word into letters
with open('names.txt', 'r') as file:
    names = file.read().splitlines()

letters = [list(name) for name in names]

print(letters)
print("_______")

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file

# with open('names.txt', 'r') as file:
#     names = file.read().splitlines()
# ....


print("_______")

# Append your first name at the end of the file
my_name = " Yossi"
with open('names.txt', 'r') as file:
    file.write("\n" + my_name)

print("_______")

# Append "SkyWalker" next to each first name "Luke"

# with open('names.txt', 'r') as file:
#    names = file.read().splitlines()
#....