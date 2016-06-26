#This program calculates pizza cost per square inch
#Program by Michael Smith

import math
def main():
    print("Welcome to Pizza Calculator!")
    print('This program calculates pizza cost per square inch!')
    print()
    D = eval(input('Please input the diameter of the pizza in inches: '))
    C = eval(input('Please input the cost of the pizza in USD: '))
    A = math.pi*((D/2)**2)
    CI = A/C
    print()
    print('Your pizza will cost $',round(CI, 2),'per square inch!')

main()