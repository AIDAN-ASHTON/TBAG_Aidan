from character import Enemy

dave = Enemy("Dave", "A Smelly Zombie")
dave.describe()

dave.set_converstion("Hi I'm Dave and totally won't eat you")
dave.talk()
dave.set_weakness("cheese")
print("What will you fight wiht?")
fight_with = input("Enter item here: ")
dave.fight(fight_with.lower())