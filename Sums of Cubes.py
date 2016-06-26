#This program calculates the sum of cubes of the first n natural numbers
#By Michael Smith

import math
def main():
    n = eval(input("Please enter a whole number: "))
    fact = 0
    for factor in range (n,0,-1):
        fact = fact + (factor**3)
    print("The sum of the natural numbers of", n, "is", fact)

main()