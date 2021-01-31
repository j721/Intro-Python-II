# Implement a class to hold room information. This should have name and
# description attributes.
#  also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.


# Room class should be extended with a list that holds the Items that are currently in that room.



class Room:
    def __init__(self, name, description, items =[]):
        self.name = name
        self.description = description
        self.items = items
        #assigning direction attributes to room. Initializing the rooms having no value
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        print (self.name, self.description)
    
    def add_item(self, item):
        self.items.append(item)
    
    def list_items(self):
        if not self.items:
            print("Sorry, this room contains no items in it.")
        else:
            print("This room has: ")
            for item in self.items:
                print(item.name)
                print(item.description)



    # def __repr__(self):
    #     return self
 