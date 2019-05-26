import datetime

def tellmeYourAge(yearBorn):
    #work out age from year of birth
    return datetime.date.today().year - yearBorn

def ask_yes_no(question):
    #ask a y/n question, if unsatisfactory response, will loop
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    if response=='y':
        return True
    else:
        return False

def askForInt(question):
    
    while True:
    #while True means it's an infinite loop.
    #Since True will always be True
        try:
            #store result of int(input(question)) as retInt.
            retInt = int(input(question))
            break
            #break if there is no error, and escape the while loop
        
        except:
            #if retInt results in an error,
            #aka retInt is NOT an integer,
            #the below code will happen
            print("Please enter a valid integer number")

    return retInt

def main_code():
    if ask_yes_no("Enter y or n:"):
#while ask_yes_no returns a True,
        yob = askForInt("which year u born")
    #string is ok because if you notice, the variable
    #is inside a input() so the string goes into the input bracket.
    #input("string ends up here")
    
        print("So you're {} y/o".format(tellmeYourAge(yob)))
    
    else:
        print("kays, have a good day.")

while True:
    main_code()
    print("Retry y/n?")
