from room import Room
from character import Enemy

kitchen = Room('Kitchen')
ballroom = Room('Ballroom')
dining_hall = Room('Dining Hall')

dave = Enemy("Dave", "A Smelly Zombie")
dave.set_converstion("Hi I'm Dave and totally won't eat you")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

kitchen.set_description('A dank and dirty room buzzing with flies')
ballroom.set_description('A vast room with a shiny wooden floor')
dining_hall.set_description('A large room with ornate decorations')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')


current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")
    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        # Add code here

