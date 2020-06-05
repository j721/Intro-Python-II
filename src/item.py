# The item should have name and description attributes.
# Add an on_take method to Item.
# on_take should print out "You have picked up [NAME]" when you pick up an item.
# add an on_drop method to Item
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # def pick_up(self):
    #     print (f"You have picked up {self.name}")
    
    def pickup_item(self, player):
        player.items.append(self)
        player.current_room.items.remove(self)
        print(f"You have picked up {self.name}")
        

    # def drop(self):
    #     print(f"You have dropped the item: {self.name}")

    def on_drop(self,player):
        player.items.remove(self)
        player.current_room.items.append(self)
        print(f"You have dropped this item: {self.name}")