def main():
    #months array/list that has all the 12 months
    months = ["January", "February", "March", "April", "May", "June", "July"
              ,"August", "September", "October", "November", "December"]
    #empty  list named rainfall for the rainfall of each month to be stored in memory
    rainfall = []
    #for loop to iterate throuigh months to get rainfall input for each month
    for month in months:
        amount = float(input("Please enter the amount of rainfall for " + month + ": "))
        rainfall.append(amount)
##creates a total_rainfall varable to store all amounts of rainfall per month and have top total of them all in that value
    total_rainfall = 0
    for amount in rainfall:
        total_rainfall += amount
    #to find average we can use the total of all rainfall in all the months and divide by 12 to get avaaege per month
    average_rainfall = total_rainfall / 12.0
    #using max built in function to return the highst value in sequence(rainfall) so taking that highest rainfall amount 
    highest_rainfall = max(rainfall)
    #using min built in function to return the lowest  value in sequence(rainfall) so taking that lowest rainfall amount
    lowest_rainfall = min(rainfall)
    highest_month = months[rainfall.index(highest_rainfall)]
    lowest_month = months[rainfall.index(lowest_rainfall)]

# Prints total rainfall first by adding all the rainfall together and store it in total_rainfall
    print("The total rainfall for the year is:", total_rainfall)
    #prints average rainfall 
    print("The average rainfall is:", round(average_rainfall, 2))
    print("The name of the month with the highest rainfall is", highest_month)
    print("The name of the month with the lowest rainfall is", lowest_month)

main()
