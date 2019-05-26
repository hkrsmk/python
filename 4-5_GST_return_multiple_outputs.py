def GST(AmtWithGST):
    amtb4g = AmtWithGST/107*100
    return amtb4g, AmtWithGST - amtb4g

amtB4G, GST = GST(107)
#store return value 1 (aka amtb4g) from GST() into amtB4G
#store return value 2 (aka AmtWithGST - amtb4g) from GST() into GST
#for stuff with >1 variable, need to store each return in different variables

print(" {0} is GST, {1} is before GST for {2}".format(GST, amtB4G, 107))
