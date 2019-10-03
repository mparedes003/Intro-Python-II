from room import Room
from player import Player
from item import Item

# Instantiate a few new Item objects
# Declare some items
items = {
    "gold_coins": Item("gold coins"),
    "potion": Item("potion"),
    "sword": Item("sword"),
    "torch": Item("torch"),
    "two_rocks": Item("two rocks"),
    "treasure_chest": Item("treasure chest filled with diamonds")
}

# Instantiate a few new Room objects
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['two_rocks']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['torch']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Angel', room['outside'])

# Write a loop that:
while True:
    #
    # * Prints the current room name in the color green
            # which room the player currently is in
    print("\n\x1b[32m You are in the {}.".format(player.location.name))

# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)

    # Print the list of items in the room
    player.location.list_items()

# * Waits for user input and decides what to do.
    input_cmd = input("\nWhat would you like to do: ")

    command = input_cmd
# If the user enters "q", quit the game.
    # Upper Method automatically converts
    # any lowercase entries to UPPERCASE
    # to fascilitate better user experience
    # and avoid errors or non-responsiveness
    if command.upper() == "Q":
        print("\nTHANK YOU FOR PLAYING!\nHOPE TO SEE YOU AGAIN SOON :) \n")
        break
#
# If the user enters a cardinal direction, attempt to move to the room there.
    if command.upper() == "N" or command.upper() == "S" or command.upper() == "E" or command.upper() == "W":
        enter_room = player.location.direction_to_move_in(command.upper())

        # If there is no room in the dicrection you want to move in, print an error message
        if enter_room == None:
            print(
                "\n\x1b[35m===Moving in that direction is not an option===\n           Please try again\n")
        else:
            # Else move the user to the room specified
            player.change_location(enter_room)

# Print an error message if the movement isn't allowed.
    else:
        print(
            "\n\x1b[35m===I don't think I know what to do with that===\n          Please try another command\n")
