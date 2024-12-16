#def main():
 #   num_upper = 0
  #  num_lower = 0
   # num_space = 0
    #num_digits = 0
    #data = ''

    #infile = open('text.txt', 'r')
    #ata = infile.read()

    #for ch in data:
     #   if ch.isupper():
      #      num_upper +=1
       # if ch.islower():
        #    num_lower += 1
        #if ch.isdigit():
          #  num_digits += 1
        #if ch.isspace():
         #   num_space += 1
    #infile.close()

   # print("Uppercase letters:" , num_upper)
    #print("lowercase letters :" , num_lower)
    #print("digits ", num_digits)
    #print("Spaces: ", num_space)
#main()
#finds phone number in the ts=xt           
import re
text = "my phone number is 123-456-7890. Call me! or use this one 333-666-9999"

#formats to d X3 which is a digit
pattern = r'\d{3}-\d{3}-\d{4}'
matches = re.findall(pattern, text)
print(matches)
print (matches[0])
print (matches[1])
