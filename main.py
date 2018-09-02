"""
This file will be used to run the game.
"""
from ugraphic import *



width = 800
height = 600

def main():
    win = GraphWin("wildberry", width, height)
    rect = Rectangle(Point(0,0), Point(799, 599))
    rect.setFill("cyan")
    rect.draw(win)

    #img = Image(Point(0, 0), "images/blueberry.png") image wont draw
    #img.draw(win)




    play = True
    while play:
        k = win.checkKey()
        if k == 'Escape':
          break

    win.close()

main()