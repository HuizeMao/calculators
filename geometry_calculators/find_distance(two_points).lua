io.write("input x1: ")
x1 = io.read("*n")
io.write("input y1: ")
y1 = io.read("*n")
io.write("input x2: ")
x2 = io.read("*n")  
io.write("input y2: ")
y2 = io.read("*n")

answer = math.sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
io.write (answer)