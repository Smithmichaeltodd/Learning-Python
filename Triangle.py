#triangle.py
#By Michael Smith

from graphics import*

def main():
    win = GraphWin("Draw a Triangle!")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5), "Click on three points!")
    message.draw(win)

    #Get a draw three vertices
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    #Use poltgon objet to draw triangle

    triangle = Polygon(p1,p2,p3)
    triangle.setFill('Black')
    triangle.setFill('Cyan')
    triangle.draw(win)

    #wait for another click to exit

    message.setText("Click anywhere to quit")
    win.getMouse()

main()