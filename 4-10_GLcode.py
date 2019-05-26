GLcode = input("AccountID")
#asks for user to request an account ID

GLlines = []
#starts an empty array

infile = open("G:\school\Python\\ForS4.txt","r")
s = infile.readline()

readStage = 0 #not to read yet, just pass

while not s.startswith("GLDataEnd"):
    #while GLData hasn't ended yet,

    if s.startswith("GLDataStart"):
        readStage = 1 #standby for title read in
        
    elif readStage == 1:
        header = s.split("|")
        #read all the headers/titles and store in header[], then increment
        readStage += 1
        
    elif readStage > 1:
        GLlines.append(s)
        #add s to GLines

    s = infile.readline()
    #get a new s

    print(readStage)

for i in range(len(header)):
    print(header[i],end = "\t")
    #end with a \t each time instead of the default \n
    
print("\n")

for line in GLlines: 
    ss = line.split("|")
    #for everything inside GLData, store into an array ss
   
    if ss[header.index("AccountID")]==GLcode:
    #only print if ss fits the GLcode input by the user
        
        for i in range(len(ss)):
            print(ss[i], end = "\t")
        print("\n")

infile.close()
