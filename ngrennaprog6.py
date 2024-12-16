#Needed for the remove and rename functions
import os
# main function 
def main():
    #opens the 'grade.txt' file and reads from it
   grades_file = open('grades.txt','r')
   #opens and creates new text file named 'temp.txt' and writes to the file
   temp_file = open("temp.txt","w")
   #ask to input a last name to search for and stores the string into 'search' vairable
   search = input("What is your last name?: ")
   #Starts reading the'grades.txt' file and file starts at a lastname and reads it in
   last_name = grades_file.readline()
   #while loop last name does not equal a space, which does at the end of the name
   while last_name != '':
       #score in  'grades.txt' is read once there is a space
       grade_score = grades_file.readline()
       #copys the last name you write to file and takes off the new line 
       last_name = last_name.rstrip("\n")
       #if the lastname doesnt = the last name i put into input then it just skips over
       if last_name != search:
           #writes and keeps the same name to the temp file and adds a new line for score next
           temp_file.write(last_name + "\n")
           #writes the same score 
           temp_file.write(grade_score)
       #this is when the name is found 
       else:
           #will write the last name of your name and new line for the score
           temp_file.write(last_name + "\n")
           #will replace the zero and write 100 and new line for next names 
           temp_file.write("100\n")
        #when last name is found it will read though the lines still to end of file
       last_name = grades_file.readline()
   #using os function to close the file
   grades_file.close()
   #closeing the temp file as well
   temp_file.close()
    #removes the orignal grade.txt file that was only read from
   os.remove("grades.txt")
   #renames the temp file to grades.txt,the orignal file name that was written to and shows the 100 score under the last name
   os.rename("temp.txt",'grades.txt')
#calls main
main()
            
              
                      
    



