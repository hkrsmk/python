#task: change grade to alphabet

conti = True

while conti:
    grade=int(input("what grade"))

    if abs(grade - 100)>100:
        print ("Huh?")
    elif grade >= 80:
            print("A")
    elif grade >= 70:
            print ("B")
    elif grade >=60:
            print ("C")
    elif grade >=50:
            print ("D")
    else:
            print ("F")
