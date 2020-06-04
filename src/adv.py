from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Wizard', room['outside'])
#print(f"Greetings, {player.name}")
# print('Player is in the:', player.current_room.name

# def change_room():
#     new_player.move(selection[0])
#     if getattr(new_player.current_room, f"{selection}_to") is None:


running = True
# Write a loop that:
while running:
    #Prints the current room name
    print(f"You are in: {new_player.current_room.name}")
    # Prints the current description (the textwrap module might be useful here).
    print(f"You are seeing {new_player.current_room.description}")

# Waits for user input and decides what to do.
    selection = input("What do you want to do?/n n for north, e for east, w for west, s for south. q for quit game.)")
    user_selection = selection.lower().split(" ")
# If the user enters a cardinal direction, attempt to move to the room there.
    if selection == "q":
        print("Until next time...exiting the game")
        break
        
    elif selection == "n" or selection == "s" or selection == "e" or selection == "w":
        print("f {selection} made it to selection ")
        new_player.move(selection)
        print(f"/n {new_player.name} is in {new_player.current_room.name}/n {new_player.current_room.description}/n/n {new_player.current_room.list_items()}")
    
    elif selection == "i":
        new_player.print_items()
    
    # elif len(user_selection) ==2:
    #     if user_selection[0] in ["get", "pickup"]:
    #         if new_player.items [user_selection[1]]:
    #             new_player.pickup_item(new_player.items[user_selection[1]])

    #             print("\n\n You have now added a new item into your listed inventory!")
    else:
        print("Sorry, command is not recognized.")
    
        
# Print an error message if the movement isn't allowed.
# If the user enters "q", quit the game.
