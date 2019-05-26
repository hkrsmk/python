def areaCircle(r):
    return 3.1416 * r **2

def volCone(r, height):
    return areaCircle(r) * height/3

def volCylinder(r, height):
    return areaCirlce(r) * height

print("Area of circle of radius {} is {}".format(7,areaCircle(7)))
print("Vol of cone of radius {}, height {} is {}".format(7,10,volCone(7,10)))
