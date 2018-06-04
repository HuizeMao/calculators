from math import sqrt
quadratic_formula_question_b = float((input("enter b of quadratic formula in order to solve quadratic formula ")))
quadratic_formula_question_c = float((input("enter c of quadratic formula in order to solve quadratic formula ")))
quadratic_formula_question_a = float((input("enter a of quadratic formula in order to solve quadratic formula ")))

def quadratic(b,a,c):
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  return (x1,x2)

print (quadratic(quadratic_formula_question_b, quadratic_formula_question_a, quadratic_formula_question_c))