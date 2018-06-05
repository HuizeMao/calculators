x1 = float(input("input x1 "))
y1 = float(input("input y1 "))
x2 = float(input("input x2 "))
y2 = float(input("input y2 "))
x3 = float(input("input x3 "))
y3 = float(input("input y3 "))

midpt_first_x = (x1+x2)/2
midpt_first_y = (y1+y2)/2
slope_first = (y3 - midpt_first_y) / (x3 - midpt_first_x)
b_of_first_equation = midpt_first_y - slope_first * midpt_first_x
first_equation = "your first equation is y = {}x + ({})".format(slope_first,b_of_first_equation)
print (first_equation)

midpt_second_x = (x2+x3)/2
midpt_second_y = (y2+y3)/2
slope_second = (y1 - midpt_second_y) / (x1 -midpt_second_x)
b_of_second_equation = midpt_second_y -  slope_second * midpt_second_x
second_equation = "your second equation is y = {}x + ({})".format(slope_second,b_of_second_equation)
print (second_equation)



final_answer_x = (b_of_second_equation - b_of_first_equation) / (slope_first - slope_second)
final_answer_y = (slope_second * final_answer_x) + b_of_second_equation
print ("this is x coodinate of circumcenter {}".format(final_answer_x))
print ("this is y coodinate of circumcenter {}".format(final_answer_y))
print (final_answer_x,final_answer_y)