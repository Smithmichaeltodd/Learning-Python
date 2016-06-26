#Slope.py
# #This program is used to solve the slope of a line
#By Michael Smith

import math #Makes math library available
def main():
    print('Welcome to the slope solver V1.0')
    print('This program finds the slope of a line')
    print()

    x1, y1 = eval(input('Please input the coordinates of the first point (x1, y1): '))
    x2, y2 = eval(input('Please input the coordinates of the second point (x2, y2): '))
    S = (y2-y1)/(x2-x1)

    print()
    print('The slope of the line is: ', round(S, 3))


main()
