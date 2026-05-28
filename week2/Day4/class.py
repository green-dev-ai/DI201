# f = open('output.txt', 'w')
# for i in range(10):
#     f.write("this is line: {i}\n")
# f.close()

# Same as
with open('output.txt', 'w') as f: # closes automaically after using the file
    for i in range(10):
       f.write(f"this is line: {i}\n")

