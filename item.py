<<<<<<< HEAD
class Item():
    def __init__(self):
        self.name = None
        self.description = None

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_desciption(self, item_description):
        self.description = item_description
=======
class Item():
    def __init__(self):
        self.name = None
        self.description = None

    def get_name(self):
        return self.name
    
    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description
    
    def set_desciption(self, item_description):
        self.description = item_description

    def describe(self):
        print(f"Item: {self.name}")
        print(f"Description: {self.description}")
>>>>>>> master
