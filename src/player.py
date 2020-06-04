# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items =[]):
        self.name = name
        self.current_room = current_room
        self.items = []  #List of items that are currently in that room.
    def __str__(self):
        print(self.name, self.current_room, self.items)

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("There is no room available in that direction. Try again.")
    
    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pickup()
        else:
            print(f"A {item.name} is not in this room.")
    
    def drop_item(self,item):
        if self.items.count(item) > 0:
            self.current_room.items.append(item)
            self.items.remove(item)
            item.drop()
        else:
            print(f"You do not have the item: {item.name} to drop.")
    
    def print_items(self):
        if not self.items:
            print("You have no items in hand.")
        else:
            print("Here is the list of items you have so far:")
            for x in self.items:
                print(x.name)
    # def __repr__(self):
    #     return self
