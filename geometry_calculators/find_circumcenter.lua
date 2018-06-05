--ask for input
io.write("input x1: ")
x1 = io.read("*n")
io.write("input y1: ")
y1 = io.read("*n")
io.write("input x2: ")
x2 = io.read("*n")
io.write("input y2: ")
y2 = io.read("*n")
io.write("input x3: ")
x3 = io.read("*n")  
io.write("input y3: ")
y3 = io.read("*n")
--couple of functions which find midpt, slope.
function mid_pointx (x1,x2)
  ans = (x1 + x2)/2
  return ans
end
function mid_pointy(y1,y2)
  ans = (y1+y2)/2
  return ans
end
function slope(x1,x2,y1,y2)
  ans = -1 / ((y1-y2)/(x1-x2))
  return ans
end
-- find first equation
m1 = slope(x1,x2,y1,y2)
midx1 = mid_pointx(x1,x2)
midy1 = mid_pointy(y1,y2)
b_of_first_equation = midy1 - m1 * midx1
--print ("your equation of first line is y = " ..m1.. "x+" ..b_of_first_equation)
-- find second equation
m2 = slope(x2,x3,y2,y3)
midx2 = mid_pointx(x2,x3)
midy2 = mid_pointy(y2,y3)
b_of_second_equation = midy2 - m2 * midx2
--print ("your equation of second line is y = " ..m2.. "x+ " ..b_of_second_equation)
-- final solution
final_x = (b_of_second_equation - b_of_first_equation)/(m1 - m2)
final_y = (m2 * final_x + b_of_second_equation)
print ("\nThe circumcenter is: \n x = "..final_x.." \n y = "..final_y)
