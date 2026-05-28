import json

# step 1
file = 'file.json'
with open(file, 'r') as file_obj:
    family = json.load(file_obj)


# step 2
for child in family["children"]:
    print(f"Name: {child['firstName']}")
    print(f"Age: {child['age']}")
    print()

# step 3 

colors = ["blue", "green"]
for child, color in zip(family["children"], colors):
    child["favoriteColor"] = color

with open(file, 'w') as file_obj:
    json.dump(family, file_obj, indent = 2)   

# print(family)
