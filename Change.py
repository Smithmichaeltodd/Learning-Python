#Change.py
#A program to calculate the value of some change in dollars

def main():
    print('Change Counter V 1.0')
    print()
    print("Please enter the count of each coin type: ")
    halfdollars = eval(input('Half Dollars:  '))
    quarters = eval(input('Quarters:  '))
    dimes = eval(input('Dimes:  '))
    nickles = eval(input('Nickles:  '))
    pennies = eval(input('Pennies:  '))
    total = halfdollars*0.5 + quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    print()
    print('The total value of your change is $', total)

main()