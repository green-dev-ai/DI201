# Working with the following string:

# description = "strings are..."

# make it all uper case
# replace the word "are" to "is"
# print just the word "strings"

description = "strings are..."

description_upper = description.upper()
description_rep = description.replace("are", "is")
description_string = description.replace(" are...","")

print(description_upper)
print(description_rep)
print(description_string)
