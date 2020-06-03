# Implement a class to hold room information. This should have name and
# description attributes.
#  also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.


# Room class should be extended with a list that holds the Items that are currently in that room.



class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
 