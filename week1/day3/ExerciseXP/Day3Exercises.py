# You are given two lists. Convert them into a dictionary where the first list contains 
# the keys and the second list contains the corresponding values.


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = {}

for key, value in zip(keys, values):
    my_dict[key] = value
   
   
print(my_dict)


#-------- Exercise 2

# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.
total_cost = 0
for name, age in family.items():
    if age < 3:
        print(f"{name} ticket cost $0")
    elif age < 13:
        print(f"{name} ticket cost $10")
        total_cost += 10
    else:
        print(f"{name} ticket cost $15")
        total_cost += 15

print(f"The total cost of the tickets is: {total_cost}")

#-------- Exercise 3

# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.


brand_dict = {
'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Americo Ortega Geona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color':{
    'France':['Blue'],
    'Spain': ['red'],
    'US':['pink', 'green']
    }

}

brand_dict['number_stores'] = 2
# print(brand_dict['number_stores'])

print(f"{brand_dict['name']}'s clients include: {brand_dict['type_of_clothes'][0]}, and {brand_dict['type_of_clothes'][2]}")

brand_dict['country_creation'] = 'Spain'
# print(brand_dict)

if brand_dict['international_competitors'] != False:
    brand_dict['international_competitors'].append('Desigual')

# print(brand_dict)

del brand_dict['creation_date']
# print(brand_dict)

print(brand_dict['international_competitors'][-1])

print(brand_dict['major_color']['US'])

num_keys = 0
for key in brand_dict:
    num_keys += 1

print(num_keys)

print(brand_dict.keys())


more_on_zara = {

'creation_date': 1975,
'number_stores': 7000,
}

brand_dict.update(more_on_zara)

print(brand_dict)

# Exercise 4

# You are given a list of Disney characters. Create three dictionaries 
# based on different patterns as shown below:

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict_char_to_indices = {}
dict_indicies_to_char = {}
dict_sorted_to_indicies = {}
i = 0
for name in users:
    dict_char_to_indices[name] = i
    i += 1
print(dict_char_to_indices)

i = 0
for name in users:
    dict_indicies_to_char[i] = name
    i += 1
print(dict_indicies_to_char)

users.sort()
i = 0
for name in users:
    dict_sorted_to_indicies[name] = i
    i += 1
print(dict_sorted_to_indicies)
