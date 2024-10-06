<<<<<<< HEAD
class Character():
    def __init__(self, char_name, char_description ):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f'{self.name} is in this room!')
        print(self.description)

    def set_converstion(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name}] says : {self.conversation}')
        else:
            print(f"{self.name} doesn't wan't to talk to you")

    def fight(self, combat_item ):
        print(f"{self.name} doesn't want to fight with you")
        return True
    
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    
=======
import random

class Character():
    def __init__(self, char_name, char_description ):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f'{self.name} is in this room!')
        print(self.description)

    def set_converstion(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f'[{self.name}] says : {self.conversation}')
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self, combat_item ):
        print(f"{self.name} doesn't want to fight with you")
        return True
    
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False
        
    def steal(self):
        print(f"Let's steal from {self.name}")
        if random.choice([True, False]):
            print(f"{self.name} catches you attempting to steal!")
            return False
        else:
            print(f"you manage to steal from {self.name}!")
            return True
        
    def bribe(self, amount):
        print(f"you offer {self.name} {amount} coins as a bribe.")

        if amount >= 100:
            print(f"{self.name} accepts your bribe!")
            return True
        else:
            print(f"{self.name} refuses your bribe!")
            return False
    
    def send_to_sleep(self):
        print(f"you attempt to put {self.name} to sleep")

        if random.choice([True, False]):
            print(f"{self.name} falls asleep.")
            return True
        else:
            print(f"{self.name} resists your attempt to put them to sleep")
            return False
        

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.favourtie_gift = None

    def set_favourtie_gift(self, gift):
        self.favourtie_gift = gift

    def hug(self):
        print(f"You give {self.name} a big hug!")
        print(f"{self.name} smiles and seems very happy.")

    def offer_gift(self, gift):
        print(f"You offer {self.name} a {gift}.")
        if gift == self.favourtie_gift:
            print(f"{self.name} loves the {gift}! You've made a great friend.")
        else:
            print(f"{self.name} politely accepts the {gift}, but seems unimpressed.")

    
>>>>>>> master
