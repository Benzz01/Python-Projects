#def main(): #opens up notepad
 #   outfile = open('friends.txt','w')
  #  outfile.write("Noah\n")
   # outfile.write("Ben\n")
    #outfile.write("Cris\n")
    #outfile.close()
    
#main()


def main():
    myfile2 = open("friends.txt","r")
    file_contents = myfile2.read()
    myfile2.close()
    print(file_contents)
main()
                  
