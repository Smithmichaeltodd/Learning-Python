#Draws investment
#By Michael Smith

from graphics import* #Imports graphics.py file

def main():
    print("This program plots the growth of a 10 year investment")



    #create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setCoords(-1.75, -6000, 11.5, 120000)


    # Get principal and interest rate

    Text(Point(1, 115000), "Principal:  ").draw(win)
    Text(Point(5, 115000), "APR(%):  ").draw(win)
    input1 = Entry(Point(2.4, 115000), 7)
    input1.setText("0.0")
    input1.draw(win)
    input2 = Entry(Point(6.4, 115000), 7)
    input2.setText("0.0")
    input2.draw(win)
    button = Text(Point(9,115000),"Calculate It!")
    button.draw(win)
    Rectangle(Point(8,112000), Point(10,118000)).draw(win)


    #Wait for mouse click
    win.getMouse()

    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 25000), ' 25K').draw(win)
    Text(Point(-1, 50000), ' 50K').draw(win)
    Text(Point(-1, 75000), ' 75K').draw(win)
    Text(Point(-1, 100000), ' 100K').draw(win)
    Text(Point(5, -4000), 'Years (1-10)').draw(win)

    # Evaluate Inputs
    p = eval(input1.getText())
    apr = eval(input2.getText())

    #Draw bar for intial principal
    bar = Rectangle(Point(0, 0), Point(1, p))
    bar.setFill("red")
    bar.setWidth(2)
    bar.draw(win)

    #Change button to quit!
    button.setText("Quit")

    #Draw vars fir successive years
    for year in range (1,11):
        p = p * (1 + (apr/100))
        #draw bar for this value
        bar = Rectangle(Point(year, 0), Point(year + 1, p))
        bar.setFill("red")
        bar.setWidth(5)
        bar.draw(win)
        bar.setOutline("black")

    win.getMouse()
    win.close()

main()
