# Try to recreate the class explained below:

# We have a class called Door that has an attribute of is_opened declared when an instance is initiated.

# We can create a class called BlockedDoor that inherits from the base class Door.

# We just override the parent class's functions of open_door() and close_door() with our own 
# BlockedDoor version of those functions, which simply raises an Error that a blocked door cannot be opened or closed.
    

class Door:
    def __init__(self, is_open):
        self.is_open = is_open

    def open_door(self):
        if Door.is_open() is True:
            print(f"door is already open")
        else:
            self.is_open = True
            print(f"you've open the door") 

    def close_door(self):
        if Door.is_open() is True:
            print(f"you've succesfully closed the door")
            self.is_open = False
        else:
            print(f"the door is already closed")

class BlockedDoor(Door):
    def __init__(self):
        self.is_open = False

    def open_door(self):
        print("Blocked door can't be open")

    def close_door(self):
        print("Blocked door can't be closed")

