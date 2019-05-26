#discounts based on conditions
amount = float(input("How much is treatment?"))

#old=(input("elderly y/n?").upper()=='Y')

old=(eval(input("elderly age?")))
if old >= 65:
    old = True
    discount = 0.5

elif old <65:
    old = False
    tall=(input("Tall? y/n").upper()=='Y')
    heavy=(input("heavy? y/n").upper()=='Y')
 
    if (old==False) and tall and heavy:
        discount = 0.1
        #this case for young and also tall and also heavy

    else:
     discount = 0.2

#% forces the type of the variable to be a specific type
     
print("Amount payable %.2f"%(amount*(1-discount)))
print("Amount = {0:.2f}".format(amount*(1-discount)))
print("Discount entitled is {0:.2%}".format(discount))
