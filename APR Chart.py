#Draws investment
#By Michael Smith

from graphics import* #Imports graphics.py file

def main():
    print("This program plots the growth of a 10 year investment")

    #Get principal and interest rate
    principal = eval(input("Enter the intial principal: "))
    apr = eval(input("Enter the APR: "))

    #create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setCoords(-1.75, -600, 11.5, 10400)
    win.setBackground("white")
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), ' 10.0K').draw(win)
    Text(Point(5, -400),'Years (1-10)').draw(win)

    #Draw bar for intial principal
    height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)

    #Draw vars fir syccessuce tears
    for year in range (1,11):
        principal = principal * (1 + apr)
        #draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("red")
        bar.setWidth(5)
        bar.draw(win)
        bar.setOutline("black")

    input("Press <Enter> to quit")
    win.close()

main()
