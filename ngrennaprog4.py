#initalizing days to zero 
days = 0;
#while loop for days input between 1-30,if outside that then loop repeats
while days < 1 or days > 30:
    #gets days in int from user
    days = int(input("Enter number of days: "))
    # checks to see if its outside the 1-30 range then it will print invaild and also go back to the loop
    if days < 1 or days > 30:
        print("Invaild Input. Number of days must be btween 1-30.")

#nickels to 1 for first days pay
nickels = 1
#total pay for all days nickels totaled up and stored in. stored as a dollar value
total_pay = 0.0
#print line for a blank line inbetween
print()
#printing day and salary table
print("Day         Salary")
print("-------------------")
#starts loop from day 1 and every day goes up by 1 for the days+1 
for day in range(1, days + 1):
    #day gets increased by one and the $ prints after some spacing
    print(day, "     $",
          #formats nickel amount into dollars. 1 nickel = 0.05 dollars
          format(nickels * 0.05, ",.2f"), sep='')
    #adds the current days salary to toal pay
    total_pay += (nickels * 0.05)
    #doubles nickels pay for next days pay
    nickels *= 2
#adds a blank line between
print()
print("The total salary for", days, "days is: $",
      #formats pay as dollar amount with commas and 2 decimal places
      format(total_pay,",.2f"), sep = "")
