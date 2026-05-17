user_input = input("please enter a string that is 10 charecters long :")
if len(user_input) != 10:
    if len(user_input) < 10:
        print("the string is not long enough.")
    else:
        print("the string is too long.")
else:
    print(user_input[0])
    print(user_input[-1])
new_string = ""
for i in range(len(user_input)):
    new_string = new_string + user_input[i]
    print(new_string)

