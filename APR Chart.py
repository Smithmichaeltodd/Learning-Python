#Draws investment
#By Michael Smith

from graphics import* #Imports graphics.py file

def main():
    print("This program plots the growth of a 10 year investment")

    #Get principal and interest rate
    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the APR: "))

    #create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), ' 10.0K').draw(win)

    #Draw bar for intial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)

    #Draw vars fir syccessuce tears
    for year in range (1,11):
        principal = principal * (1 + apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("red")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()