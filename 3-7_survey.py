counts = [0,0,0,0]
#counts the number of responses with 4 slots
#since slots start from 0,
#they correspond to 0, 1, 2, 3 ratings respectively

response = []

thisOneSay = int (input("Like it??? 0 - 3, but -1 to end"))
while thisOneSay != -1:
    response.append(thisOneSay)
    counts[thisOneSay]+=1
    #so if the guy rates as 0, the counts array in position 0 will +1
    #if the guy rates as 1, the counts array in position 1 will +1
    
    thisOneSay = int (input("Like it??? 0 - 3, but -1 to end"))
for i in range(len(counts)):
    print("%d students grade the course as %d"%(counts[i],i))

print("\nAll raw data:\n")

z=0

for i in range(len(response)):
    print("%d"%response[i], end="\t") #after printing response, then jump
    if z==4:
        z=0
        print("\n")
    else:
        z+=1

#instead of using counts, you can use arrayName.count(i) so that
#python counts the number of responses that's 0, 1, 2, or 3
