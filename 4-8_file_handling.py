outfileName = "G:\school\Python\\4-8_output.txt"
#need 2 slash, since \ is a special character

outfile = open(outfileName,"a") #"a" for append, "w" for write (override)
outfile.write("This is a times table 5\n")
for i in range (1,13):
    outfile.write("{}x{}={}\n".format(i,5,i*5))
outfile.write("\n")
outfile.close()
