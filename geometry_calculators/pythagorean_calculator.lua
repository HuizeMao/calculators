io.write("If you are trying to find the hypothenuse in a right triangle, enter 1. \nIf you are trying to find one leg in a right triangle, enter2: ")
choise = io.read("*n")
if choise == 1 then
    io.write("what is length of one leg: ")
    a = io.read("*n")
    io.write("what is length of the other leg: ")
    b = io.read("*n")
    hypo = math.sqrt(a^2+b^2)
    print( hypo)
else if choise == 2 then
    io.write("what is length of hypothenuse: ")
    hypo = io.read("*n")
    io.write("what is length of the other leg: ")
    leg = io.read("*n")
    ans = math.sqrt(hypo^2 - leg^2)
    print(ans)
end
end 