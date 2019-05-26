classList = []

score=0

score = int(input("Score? enter 0 - 100 or else, quit"))
#need this line, if not you got a lot more trouble down the road
#if I put it into the while loop, will have the sentinel value
#inside the array too
#so need to change all the len(classList) into len(classList) -1
#which is harder and more mafan

while score>=0 and score <=100:
    classList.append(score)
    score = int(input("Score? enter 0 - 100 or else, quit"))

print("{} students with average of {}"
      .format(len(classList),sum(classList)/len(classList))
      )

print("Score list is as follows:")

for s in classList:
      print(s)
