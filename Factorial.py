# Factorial.py
# This program calculates the factorial of a number
# Accumulator with a loop

def main():
    n = eval(input('Please enter a whole number: '))
    fact = 1
    for factor in range(n,1,-1):
        fact = (fact*factor)
    print('The factoral of ', n, 'is', fact)

main()