def ok2Buy(day1, day2, day3):
    retv = False
    if day1 > day2:
        if day2 > day3:
            retv = True
        else:
            retv = False
    else:
        retv = False

    return retv

def askForAmt(question):
    while True:
        try:
            retFloat = float(input(question))
            break
        except:
            print("Please enter a valid number")
    return retFloat

d1 = askForAmt("Day 1 closing?")
d2 = askForAmt("Day 2 closing?")
d3 = askForAmt("Day 3 closing?")

if ok2Buy(d1, d2, d3):
    print("Go buy!!")
else:
    print("No buy!!")
