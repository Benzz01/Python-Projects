first_user = float(input("Enter your meal cost: "))
print()
friends_meal =float(input("Enter your friend's meal cost: "))
print()
second_friend = float(input("Enter your second friend's meal cost: "))
print()

print("The cost of my meal was $",
      format(first_user, ".2f"), sep = '' + '')
print()

print("The cost of my friend's meal was $",
      format(friends_meal, ".2f"), sep = '')
print()

print("The cost of my second friend's meal was $",
      format(second_friend, ".2f"), sep = '')
print()

#first total of all users meal together
total = (first_user + friends_meal + second_friend)


tax = (total * .05)
#total with tax
total_with_tax = (total + tax)

print("The cost of the meals and tax was $",
      format(total_with_tax, '.2f'), sep = '')
print()


#calculate tip 
tip = (total_with_tax * .2)
print("The tip cost was $",
      format(tip, ".2f"), sep = '')
print()

#total with tax and tip
total_meal_cost = (total_with_tax + tip)


print("The total meal cost was $",
      format(total_meal_cost, ".2f"), sep = '')


      
