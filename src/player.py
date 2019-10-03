from item import Item
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, location, items=None):
        self.name = name            # name of player
        self.location = location    # what room they are currently in
        # If the player is not carrying any items
        self.items = [] if items is None else items
        # return an empty array
        # else return the items the player is carrying

    def change_location(self, new_location):
        self.location = new_location

    def __str__(self):      # for human consumption
        return f"Player (location: {self.location})"

    def __repr__(self):     # for programmers consumption
        return f"Player({repr(self.name)}, {repr(self.location)})"

    # function that allows a player to pick up an item
    def get(self, item):
        # append method adds the item to the players inventory
        self.items.append(item)
