# Jonathan Kocur
# 1/30/23

# This program uses 2 lists, a list for a table order at a restaurant, and a list
# for the prices of each item. Then the total price of meal is calculated along with
# tax, and a receipt is printed that lists all of the information of the sale.


# Here the input lists are defined
table_order = ["Krabby Patty", "Triple Krabby Patty", "Kelp Rings", "Kelp Shake", "Seafoam Soda"]
menu_prices = [1.50,3.25,1.50,2.00,1.50]


# Here, mathematical functions are used to calculate the rounded total costs with tax
total = sum(menu_prices)
rounded_total = round(total,2)
tax = total * (6.25/100)
rounded_tax = round(tax,2)
grand_total = total + tax
rounded_grand = round(grand_total,2)


# Here the output of the program is printed using a for loop 
print('The Krusty Krab Receipt','\n')

for i in range(len(table_order)):
    print (table_order[i],"- ${}".format(menu_prices[i])),

print('\n')
print("Total: ${}".format(rounded_total))
print("Tax 6.25%: ${}".format(rounded_tax))
print("Grand Total: ${}".format(rounded_grand),'\n')
print("Thank you and please come again!")