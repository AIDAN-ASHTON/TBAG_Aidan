<<<<<<< HEAD
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

=======
from room import Room
from character import Enemy, Character
import random

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

    # check if there's a character in the current room
    inhabitant = current_room.get_character()

    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ").lower()

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("No one to talk to I'm afraid")
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("what will you fight with?")
            fight_with = input("> ")
            if inhabitant.fight(fight_with):
                print(f"you have defeated {inhabitant.name}!")
                current_room.set_character(None)
            else:
                print("You have been defeated! Game over")
                break
        else:
            print("There is no one here to fight.")
    else:
        print("Enter one of: 'North', 'South', 'East', 'West', 'Talk' or 'Fight'")
        

>>>>>>> master
