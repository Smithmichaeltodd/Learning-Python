#Quadratic Solver.py
# #This program is used to solve a quadratic equation
#Note program will crash if no real roots are present
#By Michael Smith

import math #Makes math library available
def main():
    print('Welcome to the quadratic solver V1.0')
    print('This program finds real solutions to quadratic equations')
    print()

    a, b, c = eval(input('Please input the coefficients (a, b. c): '))

    discRoot = math.sqrt((b*b) - 4 * a * c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)


    print()
    print('The solutions are: ', root1, root2)


main()

