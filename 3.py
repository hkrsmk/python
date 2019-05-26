#accept number from user, then see if can divide by 29
xx = eval(input("Enter any number or -1 to end\n"))
#eval will make the input be treated as a number
while xx!=-1:
    if (xx%29==0):
        print("This is divisible by 29")
    #if not divisible, gimme next nearest number (both lower and higher)

    else:
        print("This is not divisible by 29")
        yy = xx - (xx%29)
        print(str(yy) + " is the nearest")
        print("The next is " + str(yy+29))
    xx = eval(input("Please enter any number or -1 to end\n"))

print("Have a nice weekend")

#for python, deal with the 'smallest' cases first. The
    #fewest cases will take up the most space
