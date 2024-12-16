

first_item = float(input("Enter your meal cost: "))
second_item = float(input("Enter you friend's meal cost: "))
third_item = float(input("nter your second friend's meal cost: "))

print("The cost of my meal was $",first_item)
print("The cost of my friend's meal was $",second_item)
print("The cost of my second friend's meal was $",third_item)

subtotal = (first_item + second_item + third_item)
sales_tax = (subtotal * .05)
tip =( total *.20)
total = (subtotal + sales_tax)
new_total = (total + tip)
print("Your subtotal is $",subtotal)
print("Your sales tax is $",sales_tax)
print("Your total amount is $",total)
print("The tip cost was $",tip)
print("The total meal cost was $",new_total)


