#This program calculates the sum of the first n natural numbers
#By Michael Smith

import math
def main():
    n = eval(input("Please enter a whole number: "))
    fact = 0
    for factor in range (n,0,-1):
        fact = fact + factor
    print("The sum of the natural numbers of", n, "is", fact)

main()