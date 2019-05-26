import datetime
#amIoldenough.py
#input NRIC and check if person
#is old enough to buy stuff (>18 y/o)

nric = input("NRIC?")
if nric[0]=="S":
    cent = 1900
elif nric [0]=="T":
    cent=2000
else:
    cent=-1
if cent>0:
    cent +=int(nric[1:3])
    age=datetime.datetime.now().year-cent
    if age>=18:
        print("can buy")
    else:
        print("Sorry no")
else:
    print("no valid ic")
