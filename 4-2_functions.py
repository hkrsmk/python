#functions - can return two variables at once which is
#pretty unique to python
#"""stuff in 3 inverted commas is like comments."""
#"""tells people what functions do"""

"""you can also write paragraphs of comments
like so"""

"""=========================CODE BLOCK===========================
def instructions():
    print("Yay")

def add2numbers_V0():
    x = int(input("number 1"))
    y = int(input("number 2"))
    #prints the string and also x+y. So print is a function
    #with any number of inputs I guess?
    print ("Sum = ", x+y, "yaz")

def add2numbers_V1():
    x=int(input("number 1"))
    y = int(input("number 2?"))
    return x+y


    ====================END CODE BLOCK==========================="""

#if variables are outside,
def add_v2(a,b):
    #check if can access the public variable
    print(x)
    print(y)
    #but you shouldn't do this thing above^ bcos will change the x and y
    #variable

    #x=1
    #if you do this above line of code,
    #that means locally within the function,
    #x=1
    #but globally the value still remains the same as the global variable
    
    return a+b

#call the function
#try not to name function the same as the file name

instructions()
add2numbers_V0()
print("da total! ",add2numbers_V1())


x=int(input("Namba 1"))
y=int(input("Namba 2"))

#below line will give you an error.
#print("da totals!",add_v2(x,y)," ",x," ",y)
