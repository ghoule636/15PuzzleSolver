"""
# Gabriel Houle
# Programming Assignment 1
# TCSS 435 AI Spring 2016
"""

from graphics import *

class displayBoard:
    def __init__(self) :
        self.__window = GraphWin("15 Puzzle Solver", 200, 200)
        message = Text(Point(self.__window.getWidth()/2, 20), 'Click anywhere to close.')
        message.draw(self.__window)
        self.__window.getMouse()
        self.__window.close()


    def close(self) :
        self.__window.close()