# Jonathan Kocur
# 3/26/23
# Assignment 5 Database


# This code works as the database for the ordering system, that creates a class
# for all the suppliers which can then access all of their part information

class Database:

    # This method initializes the database
    def __init__(self):
        self.suppliers = []
      
    # This method is used to add suppliers to a list from the user input
    def add_supplier(self, supplier):
        self.suppliers.append(supplier)
       
    # This method is used to take a part name as input, and find the supplier
    # offering the lowest price
    def find_part(self, part_name):

        # This nested for loop looks through each of the parts for each supplier
        # to check if the requested part is offered and adds them to a list
        current_suppliers = []
        for supplier in self.suppliers:
            for part in supplier.parts:
                if part.name == part_name:
                    current_suppliers.append(supplier)
                    break
        
        # This if statement returns false booleans values if the inputed part is
        # not given by any suppliers
        if len(current_suppliers) == 0:
            return False, False
        else:
            lowestPriceSupplier = current_suppliers[0]
            lowestPrice = None
        
            # These for loops go through the current suppliers and update the lowest
            # price, then when the loop is done the lowest price and its supplier are
            # returned
            for part in lowestPriceSupplier.parts:
                if part.name == part_name:
                    lowestPrice = part.cost
                    break

            for supplier in current_suppliers:
                for part in supplier.parts:
                    if (part.name == part_name) and part.cost <= lowestPrice:
                        lowestPriceSupplier = supplier
                        lowestPrice = part.cost
                        break
            return lowestPriceSupplier.name, lowestPrice
