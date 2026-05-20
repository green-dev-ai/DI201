# Challenge 1


word = input("please enter a word :")

my_dict = {

}


for (place, char) in enumerate(word):

    if char in my_dict:
        my_dict[char].append(place)
    else:
        my_dict[char] = []
        my_dict[char].append(place)
          
print(my_dict)

# --------- Challenge 2

# 1. Store Data:

# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
# 2. Data Cleaning:

# You need to clean the dollar sign and the commas using python. Don’t hard code it.
# 3. Determining Affordable Items:

# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.
# 4. Examples:



# example 1
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"

# exampe 2
items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"

# example 3
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"

# data cleaning
wallet = int(wallet.replace("$", "").replace(",", ""))
# print(wallet)

items_purchase_clean = {
}
basket = []

for (item, cost) in items_purchase.items():
    
    items_purchase_clean[item] = cost
    items_purchase_clean[item] = int(cost.replace("$", "").replace(",", ""))

    if wallet >= items_purchase_clean[item]:
        wallet = wallet - items_purchase_clean[item]
        basket.append(item)
    
if len(basket) == 0:
    print(f"Nothing")
else:
    print(f" The items to be purchased are: {sorted(basket)}")

# print(f"you have {wallet} left in your wallet")