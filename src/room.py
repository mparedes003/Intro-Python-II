# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name                  # name of room
        self.description = description    # what player sees and feels when in the room
        self.items = [] if items is None else items  # if there are no items in the room
        self.n_to = None                                # return an empty array
        self.s_to = None                              # else return the items in the room
        self.e_to = None
        self.w_to = None

    def __str__(self):      # for human consumption
        return f"Room (name: {self.name}, description: {self.description}, items: {self.items})"

    def __repr__(self):     # for programmers consumption
        return f"Room({repr(self.name)}, {repr(self.description)})"

    def direction_to_move_in(self, direction):
        if direction == "N":
            return self.n_to
        elif direction == "S":
            return self.s_to
        elif direction == "E":
            return self.e_to
        elif direction == "W":
            return self.w_to
        else:
            return None

    def __str__(self):      # for human consumption
        return f"Room (name: {self.name}, description: {self.description}, items: {self.items})"

    # function that lists items that can be found in the room
    def list_items(self):
        # print with f string
        # use the join method on a comma as an items separator
            #  use a for loop to loop over the item list
        print(
            f"\n This room contains: {', '.join(item.name for item in self.items)}")

    # function that checks the room for a specific item
    def find_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False
