def main():
   loop = 'True'
   while True:
    print("Welcome to the chaos program\n")

    x = eval(input("Please chose a number between 0 and 1: "))

    y = eval(input("Please chose a 2nd number between 0 and 1: "))

    n = eval(input("Please chose a number of iterations: "))

    for i in range (n):
        x = 3.0*x*(1-x)
        y = 3.0*y*(1-y)
        print(x,y)

main()