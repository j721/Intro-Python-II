# The item should have name and description attributes.
# Add an on_take method to Item.
# on_take should print out "You have picked up [NAME]" when you pick up an item.
# add an on_drop method to Item
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pick_up(self):
        print (f"You have picked up {self.name}")

    def drop(self):
        print(f"You have dropped the item: {self.name}")