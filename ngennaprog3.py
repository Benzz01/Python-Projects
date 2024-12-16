# colors of the pocket(Black, Green, Red)
#Enter a pocket number with range(0 - 36) to keyboard
pocket_number = int(input("Enter a pocket number: "))
#if the pocket number is out of range then it will print out of range
#assings color to invaild so theres no message error at end of running if out of the range(0-36)
#color = 'invaild'
if pocket_number < 0 or pocket_number > 36:
    print("You entered pocket #",pocket_number," and that number is out of the (0-36) range.")
#checks to see if pocket number is odd
#if pocket_number % 2 == 1:
 #   print("Odd")
    #checks if pocket number is even
#elif pocket_number % 2 == 0:
    #     print("Even")
#checks color if zero then color is assigned green
if pocket_number ==0:
    color = 'green'
 # checks pocket_number to check its inbetween 1 - 10        
if pocket_number >= 1 and pocket_number <= 10:
    #checks to see if its Odd and if so it prints Black
    if pocket_number % 2 == 1:
        color = 'black'
    #checks to see if its Even and if so it prints Red
    elif pocket_number % 2 == 0:
        color = 'red'
# checks pocket_number to check its inbetween 11 - 18       
elif pocket_number >= 11 and pocket_number <= 18:
    #checks if Odd 
    if pocket_number % 2 == 1:
       color = 'red'
    # checks if even
    elif pocket_number % 2 == 0:
       color = 'black'
        #checkss pocket numbers 10 - 28 
elif pocket_number >= 19  and pocket_number <= 28:
    #check if odd
    if pocket_number % 2 ==1:
        color = 'black'
    elif pocket_number % 2 ==0:
        color = 'red'
elif pocket_number >= 29 and pocket_number <= 36:
    if pocket_number %2 ==1:
        color = 'red'
    elif pocket_number %2 ==0:
        color = 'black'

#prints what pocket you entered and the color it is    
print("You entered pocket #",pocket_number,"and the color is", color,".")





