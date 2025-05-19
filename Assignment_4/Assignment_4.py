# Jonathan Kocur
# 2/28/23
# Assignment 4

# This program acts as an online ordering program. The supplier data is provided will be taken into
# The program and shown to the user. The user is then prompted to pick an item and quantity which it
# Then adds to a total cost. Errors are prited if the user asks for too much or the part doesn't exist


# Here is where the supplier data is imported, this program is designed such that any specifications 
# can be imported and the program will still work. The json file is converted to a Dictionary so that
# The values in the file can be extracted and indexed.
import json
supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'
Dict = json.loads(supplier_data)
parts = list(Dict['parts'])


# This section prints the welcome message along with a for loop to print whatever parts are given in 
# the supplier data
print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity\n\n")
print("Parts for order are:")
for i in range(len(parts)):
    print(parts[i])
print()


# Here we are presetting the ordering boolean to true and empty lists to be used in the while loop
# for ordering. These lists will be filled with the parts and quantity that the user specifies which
# will then be used in the total order calculation
ordering = True
partsList = []
partsQuantity = []


# This while loop controls the ordering of the parts and their quantities. The program also prints
# error messages if the part does not exist or the quantity is more than is in stock
while ordering == True:

    # This part of the while loop groups together the printing and error referring to the part
    print("Please enter in a part name, or quit to exit: ",end="")
    selectedPart = input()
    if selectedPart == 'quit':
        break
    if selectedPart not in parts:
        print("Error, part does not exist, try again")
        continue


    # This part of the while loop groups together the printing and error referring to the quantity
    print("Please enter in a quantity to order: ",end="")
    selectedQuantity = input()
    if int(Dict[selectedPart]["quantity"]) < int(selectedQuantity):
        print("Error, only",int(Dict[selectedPart]["quantity"]),"of",selectedPart,"are available!")
        continue
    if int(Dict[selectedPart]["quantity"]) >= int(selectedQuantity):
        Dict[selectedPart]["quantity"] = int(Dict[selectedPart]["quantity"]) - int(selectedQuantity)


    partsList.append(selectedPart)
    partsQuantity.append(selectedQuantity)


# Here the order details along with the total cost are printed showing the user the costs of
# each part as well as the total cost of the order. A for loop is used to scan through the 
# parts list that was requested and the quantity requested and calculate the total
print("\nYour order")
GrandTotal = []

for i in range(len(partsList)):
    currentPrice = float(Dict[partsList[i]]["price"])
    partsQuantityFLOAT = float(partsQuantity[i])
    total = round((currentPrice * partsQuantityFLOAT),2)

    print(partsList[i],"-",partsQuantity[i],"@",currentPrice,"=",total)
    GrandTotal.append(total)

print("Total: ${}".format(sum(GrandTotal)))
print("Thank you for using the parts ordering system!")
