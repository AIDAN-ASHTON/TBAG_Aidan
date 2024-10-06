class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    def get_description(self):
        return self.description

    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def set_item(self, item):
        self.item = item  # Set an item in the room
    
    def get_item(self):
        return self.item  # Get the item in the room
    
    def remove_item(self):
        self.item = None  # Remove the item from the room after it is picked up
    
    def link_room(self, room_to_link, direction, locked = False):
        self.linked_rooms[direction] = {"room": room_to_link, "locked" : locked}  # lock all doors

    def get_details(self):
        print(self.name)
        print('-----------------------------------------------------------------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]["room"]
            locked_status = "(locked)" if self.linked_rooms[direction]["locked"] else ""
            print(f'The {room.get_name()} is {direction} {locked_status}')
        if self.item:
            print(f"there is a {self.item.get_name()} here.")

    def move(self, direction, has_key=False):
        if direction in self.linked_rooms:
            if self.linked_rooms[direction]["locked"]:
                if has_key:
                    print("You unlock the door with the key!")
                    self.linked_rooms[direction]["locked"] = False  # Unlock the door
                    return self.linked_rooms[direction]["room"]
                else:
                    print("The door is locked. You need a key.")
                    return self
            else:
                return self.linked_rooms[direction]["room"]
        else:
            print("You can't go that way")
            return self

