#Tis program determines the vale of the epact
#By Michael Smith

import math
def main():
    print('Gregorian epact calculator!')
    print()
    Y = eval(input('Please input a 4 digit year your would like to calculate for: '))
    C = Y//100
    epact = (8 + (C//4) - C + ((8*C + 13)//25) + 11*(Y%19))%30
    print('Your epact number is', epact)

main()