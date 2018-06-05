askx1 = input("input x1.")
askx2 = input("input x2.")
askx3 = input("input x3.")
asky1 = input("input y1.")
asky2 = input("input y2.")
asky3 = input("input y3.")

def get_nagative_reciprocal_slope(x1,x2,y1,y2):
    slope = -1 / ((float(y2) - float(y1)) / (float(x2) - float(x1)))
    return slope

slope_of_line = get_nagative_reciprocal_slope(float(askx1),float(askx2),float(asky1),float(asky2))

def midpointx(x1,x2):
    midpointx = (float(x1) + float(x2))/2
    return midpointx

def midpointy(y1,y2):
    midpointy = (float(y1) + float(y2))/2
    return midpointy

mid_pointx = midpointx(float(askx1),float(askx2))
mid_pointy = midpointy(float(asky1),float(asky2))


b_of_equation = float(mid_pointy) - slope_of_line * float(mid_pointx)
first_line_equation = "y = %sx+%s"%(slope_of_line,b_of_equation )
print (first_line_equation)