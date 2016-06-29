#ArchersTarget.py
#By Michael Smith

from graphics import*

def main():
    win = GraphWin("Archers Target", 600, 600)
    win.setBackground("black")
    win.setCoords(-10 , -10, 10, 10)
    c1 = Circle(Point(0,0), 5)
    c1.setFill('white')
    c1.setOutline('white')
    c1.draw(win)
    c2 = Circle(Point(0, 0), 4)
    c2.setFill("black")
    c2.setOutline("black")
    c2.draw(win)
    c3 = Circle(Point(0, 0), 3)
    c3.setFill('blue')
    c3.setOutline('blue')
    c3.draw(win)
    c4 = Circle(Point(0, 0), 2)
    c4.setFill('red')
    c4.setOutline('red')
    c4.draw(win)
    c5 = Circle(Point(0, 0), 1)
    c5.setFill('yellow')
    c5.setOutline('yellow')
    c5.draw(win)

    win.getMouse()
    win.close()
main()
