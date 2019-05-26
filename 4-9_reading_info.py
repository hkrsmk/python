infileName = "G:\school\Python\\forS4.txt"
infile = open(infileName,"r") #"r" for read
for i in range(1,1000):
    #1000 is arbitrary
    s = infile.readline()
    if s == "CompInfoStart|\n":
        s1 = infile.readline().split("|") #split at |
        #readline only reads for 1 line before the \n
        s2 = infile.readline().split("|")
        for j in range(len(s1)-1):
            print("{}: {}".format(s1[j],s2[j]))
            #break;
        break;
    
    #break (the second one)
    #helps the program to stop. since you already
    #found what you want,
    #you don't have to keep executing the code anymore.
    #otherwise, code will execute until i reaches 999

    elif s == "PurcDataStart|\n":
        s1 = infile.readline().split("|")
        s2 = infile.readline().split("|")
        while not s2[0].startswith("PurcDataEnd"):
            #need a second loop here, since you will break the loop
            #caused by i
            
            if s2[0] == "Storage Pte Ltd":
                #only takes data for Storage Pte Ltd

                print("{:20s}{:40s}{:10.2f}".format(s2[s1.index("InvoiceNo")],
                                                    s2[s1.index("ProductDescription")],
                                                    float(s2[s1.index("PurchaseValueSGD")])
                                                    )
                      )
                #print only 3 values, invoice, pdt descript, purchase value
                #print the s2 that has the same 'coordinate'
                #as the s1 InvoiceNo

                
                """for j in range(len(s1)-1):
                #the -1 is only to remove the last '|' and
                #not print it
                    print("{}: {}".format(s1[j], s2[j]))
                    """
                
            s2 = infile.readline().split("|")
        break;

    else:
        print(i)

#print(s1,"\n",s2)
infile.close()
