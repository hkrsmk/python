from coin_toss_object import *
#you can't start the name with a number.

my_coin = Coin()
print("First toss %r" %(my_coin.get_sideup()))

for i in range(1,100):
    my_coin.toss()
    print("Toss %d is %r" %(i+1, my_coin.get_sideup()))
