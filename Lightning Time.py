#This program calculates the distance of lightning strike
#Program by Michael Smith

import math
def main():
    print("Welcome to Lightning Strike Calculator!")
    print('This program calculates how far a lighting strike is away!')
    print()
    T = eval(input('Please input the seconds elapsed between the flash and the sound of thunder: '))
    F = (1100*T)/5280
    print()
    print('The lightning struck',round(F, 2),'miles away!')

main()