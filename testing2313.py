outfile = open("number_list.txt",'w')

for number in range(1,101):
    outfile.write(str(number) + "\n")
outfile.close()

infile = open("number_list.txt",'r')
line = infile.readline()
while line != "":
    line = line.rstrip("\n")
    number = int(line)
    print(number)
    line = infile.readline()
infile.close()
