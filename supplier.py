# Jonathan Kocur
# 3/26/23
# Assignment 5 Supplier


# This code creates a class for each supplier given with the user input, where
# the part name and price is organized with its given supplier. Attributes are
# then added by the use of methods

import part

class Supplier:

    # This method takes the suppliers name as its input
    def __init__(self, name):
        self.name = name
        self.parts = []
    
    # This method adds the name and price of the inputed part
    def add_part(self, name, price):
        self.parts.append(part.Part(name,price))

    # This method returns the cost of the part when called
    def find_price(self,part):
        return part.cost
    
    # This method checks if the part is contained in the specified object
    def part_exists(self, part):
        if part in self.parts:
            return True
        else:
            return False