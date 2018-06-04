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
--functions find slopes, equations, and intersection
function slope(x1,x2,y1,y2)
  ans = -1 / ((y1-y2)/(x1-x2))
  return ans
end

m_x1_x2 = slope(x1,x2,y1,y2)
b_of_first_equation = y3 - m_x1_x2 * x3

m_x2_x3 = slope(x2,x3,y2,y3)
b_of_second_equation = y1 - m_x2_x3 * x1

final_x = (b_of_second_equation - b_of_first_equation) / (m_x1_x2 - m_x2_x3)
final_y = m_x1_x2 * final_x + b_of_first_equation
print ("\nthe orthocenter is "..final_x.." and "..final_y)                    
