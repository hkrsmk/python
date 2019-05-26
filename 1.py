deposit=input("deposit?")

annualfees=input("annual fee?")

months=input("which month?")

print("""
I gotta get a ${}
with fee ${}
with month {}
""".format(deposit,annualfees,months)
      )


print("""
I gotta get a ${1}
with fee ${0}
with month {2}
""".format(annualfees,deposit,months)
      )

#counting number starts from 0
#the 1, 0, 2 changes the sequence, so the above two coes
#have the same output

#for more formatting, gotta change type to float first
deposit=float(input("deposit?"))

annualfees=float(input("annual fee?"))

months=input("which month?")

print("""
I gotta get a ${1:8.2f}
with fee ${0:4.2f}
with month {2}
""".format(annualfees,deposit,months))

#8 spaces for numeric printout with 2 dp.
# 87654321
#     3.22
# the . and the dp counted too


deposit=input("deposit?")

annualfees=input("annual fee?")

months=input("which month?")

print("""
I gotta get a ${}
with fee ${}
with month {}
""".format(float(deposit),float(annualfees),float(months))
      )

print(deposit)

#for this above, the deposit won't change

currency = input("What currency u wan")
rate=float(input("what rate"))
amt=float(input("how much"))
convert=float((rate*amt))

print("S$\t{0} x\t{1} = {2} {3}".format(amt,rate,currency,convert) )
