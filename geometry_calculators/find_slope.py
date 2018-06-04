x1 = float(input("what is point x1: "))
y1 = float(input("what is point y1: "))
x2 = float(input("what is point x2: "))
y2 = float(input("what is point y2: "))
slope2 = (y1 - y2)/(x1 - x2)
slope = float(slope2)

if x1 == x2: 
    print("the slope is undefined")
else:
    print ("The slope these two points make is {}".format(slope))