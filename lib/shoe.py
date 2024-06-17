#!/usr/bin/env python3
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"  # Initially, the condition is set to "New"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"  # Setting condition to "New" after repair
        print("Your shoe is as good as new!")
