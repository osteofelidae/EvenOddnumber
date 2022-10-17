upTo = int(input("Input upper limit... "))
fileName = input("Input file name... ")
file = open(fileName + ".py", "w")

file.write("number = int(input('Input number... '))\n")

for number in range(int(upTo/2)):
    file.write("if number == " + str(number*2) + ":\n")
    file.write("\tprint('Number is even.')\n")
    file.write("\n")
    file.write("if number == " + str(number*2+1) + ":\n")
    file.write("\tprint('Number is odd.')\n")
    file.write("\n")
    
file.close()