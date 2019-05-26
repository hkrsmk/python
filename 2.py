a = "weogiawr"
b = "awegarwhatjqtejqr"
c = 42
d = 13

print("""q|u|i|c|k|b|r|o|w|n|f|o|x|\
j|u|m|p|s|o|v|e|r|l|a|z|y|d|o|g|"""
      [::2])

print("{1}\n{0}".format(a,b))

print("{1:>40s}\n{0:<40s}\n{1:^40s}\n{2:5.2f}\n{3:1d}\n{2:5d}".format(a,b,c,d))
#> right justified, < left justified, ^ is center

bigcat = "Tiger"
smallcat = "cat"
tinycat = "kitty"
from random import randint

print(randint(0,1))
x= randint(0,1)
#print("{2} protect {1},{x} afraid of {1},{2} eat up {0}".format(smallcat,tinycat,bigcat))

#^ this doesn't work because randint got some problem with the code

#print("does it still run?")

#=====================print a display asking for bank stuff:

import datetime
daysAllowed=int((input("How long to repay, in days? ")))

print("{:^80s}".format("ABC Bank International"))

print("""
Date: {:2d}/{:2d}/{:2d}{:>60s}
""".format(datetime.date.today().day,
           datetime.date.today().month,
           datetime.date.today().year,
           "Page 1/3"))

dateConvert=datetime.timedelta(days=daysAllowed)
print("Please pay up by ", datetime.date.today()+dateConvert)

#====================print GST for a given price:

price=float(input("What's the price?"))
inclusive=input("Include GST y/n?")

#if inclusive.upper() == 'Y':
if inclusive.upper() != 'N':
    print("GST is {0:8.2f}"
      .format(price*7/107))
else:
    print("GST is {0:8.2f}"
      .format(price*0.07))

print ("Hello there, I'm me")
cont=input("say hi to me")
      
if cont.lower() == "hi":
    rate=int(input("Rate me from 1 to 5, 5 being excellent: "))
    if rate == 5:
      print("awesome!")
    elif rate == 1:
      print("ded")
    else:
        for rate in range(0,rate):
            print ("thanks!")
else:
      print("Goodbye")

#main lesson here is the indentation, will affect
#how the program runs

