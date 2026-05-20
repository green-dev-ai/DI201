
# ------ Cooffe Shop Exercise


menu_dict = {
    "espresso":7.0,
    "latte":12.0,
    "cappuccino":10.0
}

def show_menu(menu_dict):
    """this function displays the entire menu"""
    if len(menu_dict) == 0:
        print(f"The Menu is empty")
    else:
        for drink, price in menu_dict.items():
            print(f"{drink} - {price}$")

def add_item(menu_dict):
    """this function enables the euser to add item to the menu"""
    new_drink = input(f"Enter the name of the new drink: ")
    if new_drink in menu_dict:
        print(f"{new_drink} already exsits in menu !")
    else:
        new_price = input(f"enter the price of {new_drink}: ")
        menu_dict[new_drink] = new_price
        print(f"{new_drink} added to menu !")

def update_price(menu_dict):
    """this function enables the user to update the price of an item from the menu"""
    update_drink = input(f"what drink would you like to update? ")
    if update_drink in menu_dict:
        menu_dict[update_drink] = input(f"what is the new price of {update_drink}? ")
        print(f"price of {update_drink} was updated !")
    else:
        print(f"Item not found !!")

def delete_menu(menu_dict):
    """ this function enables the user to delete an item from the menu"""
    delete_drink = input(f"what drink would you like to remove from the menu? ")
    if delete_drink in menu_dict:
        del menu_dict[delete_drink]
        print(f"{delete_drink} was deleted from the menu !!")
    else:
        print(f"{delete_drink} was not found !!")

def show_options():
    """this function presents the different option for the user"""
    print(f"What would you like to do?")
    print(f"1. Show menu")
    print(f"2. Add item")
    print(f"3. Update price")
    print(f"4. Delete item")
    print(f"5. Exit")

def run_coffee_shop():
    """this function controls the entire program"""
    flag = True
    while flag is True:
        show_options()
        selection = int(input(f"Choose 1-5: "))
        if selection == 1:
            show_menu(menu_dict)
        elif selection == 2:
            add_item(menu_dict)
        elif selection == 3:
            update_price(menu_dict)
        elif selection == 4:
            delete_menu(menu_dict)
        elif selection == 5:
            print(f"Goodbye !")
            break
        else:
            print(f"Invalid choce, Try again !")
            continue


run_coffee_shop()
    
        

