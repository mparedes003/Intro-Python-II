# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location    # what room they are currently in

    def change_location(self, new_location):
        self.location = new_location

    def __str__(self):      # for human consumption
        return f"Player (location: {self.location})"

    def __repr__(self):     # for programmers consumption
        return f"Player(location: {self.name})"
