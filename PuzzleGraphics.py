"""
# Gabriel Houle
# Programming Assignment 1
# TCSS 435 AI Spring 2016
"""

from graphics import *
import threading

global stepNum
global isClosed
global timerThread

scale = 100
width = 400
height = 500
stepNum = 0
timerDelay = 1

class displayBoard:
    def __init__(self, path) :
        global isClosed
        isClosed = False
        self.__window = GraphWin("15 Puzzle Solver", width, height)
        self.__path = path
        self.startTimer()
        self.displayPath()

    def displayPath(self) :
        global stepNum
        global isClosed
        global timerThread
        while (self.__window.isOpen()) :
            if (self.__window.checkKey().lower() == 'q') :
                self.__window.close()
                timerThread.cancel()
                isClosed = True
                break
            self.__window.update()
            self.drawBoard(self.__path[stepNum].data)
            time.sleep(.01)

        isClosed = True
        timerThread.cancel()


    def drawBoard(self, state) :
        global stepNum
        self.__window.autoflush = False
        self.__window.clear()
        quitMessage = Text(Point(width/2, height - 30), "Press q to quit")
        border = Rectangle(Point(3, 3), Point(scale * 4 + 1, scale * 4 + 1))
        if (stepNum >= len(self.__path) - 1) :
            statusMessage = Text(Point(width/2, height - 50), "Simulation Complete; {0} move(s) completed.".format(stepNum))
        else :
            statusMessage = Text(Point(width/2, height - 50), "{0} move(s) completed.".format(stepNum))
        try :
            quitMessage.draw(self.__window)
            border.draw(self.__window)
            statusMessage.draw(self.__window)
        except GraphicsError as err:
            print("")
        counter = 0
        for i in range(4) :
            for j in range(4) :
                leftCorner = Point(j * scale, i * scale)
                box = Rectangle(leftCorner, Point(j * scale + scale, i * scale + scale))
                message = Text(Point(j * scale + scale/2, i * scale + scale/2), "{0}".format(state[counter]))
                try :
                    message.draw(self.__window)
                    box.draw(self.__window)
                except GraphicsError as err:
                    print("")
                counter += 1
        try :
            self.__window.flush()
        except GraphicsError as err:
            print("")
        self.__window.autoflush = True

    def timerAction(self) :
        global stepNum
        global isClosed
        global timerThread
        stepNum += 1
        if (not isClosed and stepNum < len(self.__path) - 1) :
            self.startTimer()

    def startTimer(self) :
        global timerThread
        timerThread = threading.Timer(timerDelay, self.timerAction)
        timerThread.start()
                    
