# Implement a class to hold room information. This should have name and
# description attributes.
#  also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.


# Room class should be extended with a list that holds the Items that are currently in that room.



class Room:
    def __init__(self, name, description, items =[],  n_to=[], s_to=[], e_to=[], w_to=[]):
        self.name = name
        self.description = description
        self.items = items
        #assigning direction attributes to room
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    
    def __str__(self):
        print (self.name, self.description)
    
    def __repr__(self):
        return self
 