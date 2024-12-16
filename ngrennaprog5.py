#import random for random numbers
import random

#function that determines whether number is odd or even.(num) is what is holding even  or odd
def even_or_odd(num):
  #checks if even. Even is 0 remaninder
  if num % 2 == 0:
    #returns even 
    return "even"
  #checks if odd. Odd with one remainder. could of used else but this is more specific with no error
  elif num % 2 == 1:
      return"odd"
#even,odd,and count outside the while loop so they are initinalized    
even_total = 0
odd_total = 0
count = 0
#while loop that has the count starting at zero and going to 30
while(count < 30):
  #gives random int from 1 through 1000
  num = random.randint(1,1000)
  #stores even_or_odd in result
  result = even_or_odd(num)
  #prints out the random number and then is even/odd
  print(num, "is", result)

  
  #this is to see if number is odd or even then it will store in odd/even_total
  if result == 'odd':
   #this adds 1 to odd_total so we know out of 30 numbers how many are odd
    odd_total += 1
  else:
      #this adds 1 to even_total so we know out of 30 numbers how many are even
      even_total += 1
  #increments count by 1 so it stops at 30
  count +=1
#prints a new line and out of 30 numbers how many are odd and even  
print("\nOut of 30 random numbers,",odd_total,"were odd and", even_total, "were even.")
  
  
