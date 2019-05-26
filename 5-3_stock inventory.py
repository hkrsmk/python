#Stock inventory control system.

def menu():
    print("""1. Add New Stock
2. Update existing stock
3. Sell stock, even though 2 will work too
8. Display Inventory
9. Exit""")
    while True:
        try:
            choice = int(input("Please select an option"))
            break
        except:
            print("Invalid choice, please try again")
    return choice

#=======================================    1   ===========================
def newStock():
    newstock = input("Enter new stock name")
    if newstock in myStock:
        print("Stock already there")
    else:
        myStock[newstock]=0
        print("new stock", newstock.center(10, ' '), "added")

#=======================================    2   ===========================
def addVolume():
    stock_bought = input("Enter stock name you're buying")
    if stock_bought not in myStock:
        print("Stock ain't there. add first")
    else:
        while True:
            try:
                qty = int(input("How many? positive for buy. negative for sell"))
                myStock[stock_bought] += qty
                print(stock_bought, "is now", myStock[stock_bought])
                break
            except:
                print("Invalid quantity!")
    
#=======================================    3   ============================
def sell():
    selling = input("Stock name you're selling?")
    if selling not in myStock:
        print("You don't have this?")
    elif myStock[selling]<=0:
        print(selling.center(10, ' '), "outta stock")
    else:
        while True:
            try:
                qty = int(input("how many sold?"))
                if myStock[selling] < qty:
                    print("u selling > you have, not allowed!")
                    raise "Error"
                myStock[selling] -= qty
                print(selling, "is now", myStock[selling])
                break
            except:
                print("Invalid qty")
        

#main prog below
choice = 0
myStock = {}
#empty dictionary for myStock

try:
    infile = open("myStock.txt","r")
    read1LineStock = infile.readline()
    #read first line

    while read1LineStock !=" ":
    #while the file has not ended,
        
        myStock[read1LineStock.split(",")[0]] = int(read1LineStock.split(",")[1])
        read1LineStock = infile.readline()
        print(myStock)

    #place item 0 in the split up sentence as the name for the item for myStock,
    #and whatever number you can find in item 1 of the split up sentence (ignore '\n')
    #as the 'quantity' for myStock.
    #eg myStock['apple'] = '1'
    #then, read the next line.
        
    infile.close()
except:
    print("Welcome to the stock management system!")

while choice != 9:
    choice = menu()
    #rmb to return choice to the global choice.
    #the choice inside menu() is a LOCAL choice.
    
    if choice ==1:
        newStock()

    elif choice ==2:
        addVolume()

    elif choice ==3:
        sell()

#=======================================    8   ===========================        
    elif choice ==8:
        print(myStock)
        
#=======================================    9   ===========================    
print("Have a noice day")
