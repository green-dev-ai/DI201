
# Given a list of numbers, write a function that returns the sum of every number. BUT you can have a malicious
# string inside the list.

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
total = 0
for num in my_list:
    try:
        total += my_list[num]
        print(f"{total}")
    except:
        pass

print(f"the total is : {total}")        

        