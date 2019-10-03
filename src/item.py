class Item:
    def __init__(self, name):
        self.name = name

    def __str__(self):    # for human consumption
        return f"Item (name: {self.name})"

    def __repr__(self):   # for programmers consumption
        return f"Item(name: {self.name})"
