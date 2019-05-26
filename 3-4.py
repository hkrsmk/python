loanAmt = float (input("How much is your loan"))
noYears = int(input("years for loan repayment"))

everyYearPay = int(loanAmt/noYears)

firstYearPay = loanAmt - (everyYearPay * (noYears-1))

print("{:<40s}{:10.2f}".format("First Year",firstYearPay))

#-1 bcos no have 1st year
#i+2 because start from 0, but you want to start from year 2
for i in range(noYears-1):
    print("{:<40s}{:10.2f}".format("Year " + str(i+2), everyYearPay))
