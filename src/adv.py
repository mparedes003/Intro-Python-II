from room import Room
from player import Player

# Instantiate a few new Room objects
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
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
while True:
    #
    # * Prints the current room name in the color green
    # which room the player currently is in
    print("\n\x1b[32m You are in the {}.".format(player.location.name))
# * Prints the current description (the textwrap module might be useful here).
    print(player.location.description)
# * Waits for user input and decides what to do.
    input_cmd = input("What would you like to do: ")

    command = input_cmd
# If the user enters "q", quit the game.
    # Upper Method automatically converts
    # any lowercase entries to UPPERCASE
    # to fascilitate better user experience
    # and avoid errors or non-responsiveness
    if command.upper() == "Q":
        break
#
# If the user enters a cardinal direction, attempt to move to the room there.
    # Enter "N" command to move NORTH
    elif command.upper() == "N":
        if player.location.n_to:
            player.location = player.location.n_to

    # Enter "S" command to move SOUTH
    elif command.upper() == "S":
        if player.location.s_to:
            player.location = player.location.s_to

    # Enter "E" command to move EAST
    elif command.upper() == "E":
        if player.location.e_to:
            player.location = player.location.e_to

    # Enter "W" command to move WEST
    elif command.upper() == "W":
        if player.location.w_to:
            player.location = player.location.w_to
# Print an error message if the movement isn't allowed.
#
