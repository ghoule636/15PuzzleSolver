"""
# Gabriel Houle
# Programming Assignment 1
# TCSS 435 AI Spring 2016
"""

import sys
from collections import deque
import heapq
from functools import total_ordering
import time

def main():
    global endState1
    global endState2
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates
    global expanded
    global maxFringe
    global numCreated

    endState1 =  "123456789ABCDEF "
    endState2 =  "123456789ABCDFE "

    maxFringe = 0
    expanded = 0
    numCreated = 0
    visitedStates = set()
    validInput = True

    # Perform input validation
    if (len(sys.argv) < 3 or len(sys.argv) > 4) :
        print("Invalid Command Line Arguments!")
        validInput = False;
    else :
        initialState = sys.argv[1]
        searchMethod = sys.argv[2]
        if (not checkInitState(initialState)) :
            print("Invalid Initial State Example of valid input: \"123456789 ABCDEF\"")
            validInput = False
        elif (not checkSearchMethod(searchMethod)) :
            print("Invalid search method. Valid methods are: BFS, DFS, GBFS, ASTAR, DLS")
            validInput = False
        else : # Valid Initial State and search method here
            print("Initial State: ")
            outputPuzzle(initialState)
            print("Search Method: " + searchMethod.upper())
            if (len(sys.argv) == 4) :
                options = sys.argv[3]
                if (checkOptions(searchMethod, options)) :
                    print("Options: " + options)
                else :
                    print("Invalid option")
                    validInput = False
            elif (searchMethod.lower() == "astar" or searchMethod.lower() == "gbfs" or searchMethod.lower() == "dls") :
                print("These search methods require option h1 or h2 or size for dls")
                validInput = False
    if (validInput) :
        print("Valid Input!")
        #time.sleep(5)
        treeRoot = constructRoot()
        if (searchMethod.lower() == "bfs" or searchMethod.lower() == "dfs" or searchMethod.lower() == "dls") :
            BFSorDFS(treeRoot)
        if (searchMethod.lower() == "gbfs" or searchMethod.lower() == "astar") :
            GBFSorASTAR(treeRoot)

# This function checks if the initial state input by the user is valid. 
def checkInitState(initState) :
    requiredChars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', ' '}
    result = True
    listState = list(initState)
    if (len(initState) != 16) :
        result = False
    index = 0
    for x in listState :
        if (listState[index].lower() not in requiredChars) :
            result = False
        else :
            requiredChars.remove(listState[index].lower())
            listState[index] = 'x'
        index += 1
    for x in listState :
        if (x != 'x') :
            result = False
    if (len(initState) == 9) :
        result = True
    return result

# This function checks if the search method input by the user is valid.
def checkSearchMethod(inputSearch) :
    searchMethods = {"bfs", "dfs", "gbfs", "astar", "dls"}
    result = True
    if (inputSearch.lower() not in searchMethods) :
        result = False
    return result

def checkOptions(searchMethod, options) :
    result = True
    if (searchMethod.lower() == "gbfs" or searchMethod.lower() == "astar") :
        if (options.lower() != "h1" and options.lower() != "h2") :
            result = False
    elif (searchMethod.lower() != "dls") :
        result = false
    return result

def BFSorDFS(node) :
    global endState1
    global endState2
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates
    global expanded
    global maxFringe
    global numCreated

    fringe = deque()
    checkUp = 1
    checkLeft = 1
    checkDown = 1
    checkRight = 1

    while (checkUp != -1 or checkLeft != -1 or checkDown != -1 or checkRight != -1 or len(fringe) > 0) :
        if (len(fringe) > maxFringe):
            maxFringe = len(fringe)
        visitedStates.add(node.data)
        while (searchMethod.lower() == "dls" and node.depth > int(options)) :
            if (len(fringe) != 0) :
                node = fringe.pop()
            else :
                return 0
        if (node.data == endState1 or node.data == endState2) :
            print("Puzzle complete")
            print("Depth: ", end='')
            print(node.depth)
            print("Nodes Created: ", end='')
            print(numCreated)
            print("Expanded: ", end='')
            print(expanded)
            print("Max Fringe Size: ", end='')
            print(maxFringe)
            
            return 1
        checkUp = moveUp(node.data)
        checkLeft = moveLeft(node.data)
        checkDown = moveDown(node.data)
        checkRight = moveRight(node.data)
        expanded += 1

        if (searchMethod.lower() == "dfs" or searchMethod.lower() == "dls") :
            if (checkUp != -1) :
                checkUp.depth = node.depth + 1
                fringe.append(checkUp)
                visitedStates.add(checkUp.data)
            if (checkLeft != -1) :
                checkLeft.depth = node.depth + 1
                fringe.append(checkLeft)
                visitedStates.add(checkLeft.data)
            if (checkDown != -1) :
                checkDown.depth = node.depth + 1
                fringe.append(checkDown)
                visitedStates.add(checkDown.data)
            if (checkRight != -1) :
                checkRight.depth = node.depth + 1
                fringe.append(checkRight)
                visitedStates.add(checkRight.data)
            if (len(fringe) != 0) :
                node = fringe.pop()
        elif (searchMethod.lower() == "bfs") :
            if (checkRight != -1) :
                checkRight.depth = node.depth + 1
                fringe.append(checkRight)
                visitedStates.add(checkRight.data)
            if (checkDown != -1) :
                checkDown.depth = node.depth + 1
                fringe.append(checkDown)
                visitedStates.add(checkDown.data)
            if (checkLeft != -1) :
                checkLeft.depth = node.depth + 1
                fringe.append(checkLeft)
                visitedStates.add(checkLeft.data)
            if (checkUp != -1) :
                checkUp.depth = node.depth + 1
                fringe.append(checkUp)
                visitedStates.add(checkUp.data)
            
            if (len(fringe) != 0) :
                node = fringe.popleft()

        outputPuzzle(node.data)

    print("Nodes Created: ", end='')
    print(numCreated)
    print("Expanded: ", end='')
    print(expanded)
    print("Max Fringe Size: ", end='')
    print(maxFringe)
    print("Depth: ", end='')
    print(node.depth)
    print("fringe len")
    print(len(fringe))

def GBFSorASTAR(node) :
    global endState1
    global endState2
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates
    global expanded
    global maxFringe
    global numCreated

    fringe = []

    node.totalCost = 0

    while (node.data != endState1 and node.data != endState2) :
        
        checks = [0 for i in range(4)] 
        checks[0] = moveUp(node.data)
        checks[1] = moveLeft(node.data)
        checks[2] = moveDown(node.data)
        checks[3] = moveRight(node.data)

        expanded += 1

        for i in range(len(checks)) :
            if (checks[i] != -1) :
                 if (searchMethod.lower() == "astar") :
                     if (options.lower() == "h1") :
                         addedValue = h1(node.data)
                     else :
                         addedValue = h2(node.data)
                     checks[i].totalCost = node.totalCost + addedValue
                 else :
                     checks[i].totalCost = 0
                 checks[i].depth = node.depth + 1
                 heapq.heappush(fringe, checks[i])
                 visitedStates.add(checks[i].data)
                   
        if (len(fringe) == 0) :
            print("No solution found")
            print("Depth: ", end='')
            print(-1)
            print("Nodes Created: ", end='')
            print(0)
            print("Expanded: ", end='')
            print(0)
            print("Max Fringe Size: ", end='')
            print(0)
            return
        if (len(fringe) > maxFringe):
            maxFringe = len(fringe)
        if (len(fringe) != 0) :
            node = heapq.heappop(fringe)
        #outputPuzzle(node.data)

        if (searchMethod.lower() == "gbfs") :
            fringe = []

    print("Puzzle complete")
    outputPuzzle(node.data)
    print("Depth: ", end='')
    print(node.depth)
    print("Nodes Created: ", end='')
    print(numCreated)
    print("Expanded: ", end='')
    print(expanded)
    print("Max Fringe Size: ", end='')
    print(maxFringe)


# This Heuristic uses the number of misplaced tiles as a measure of fitness.
def h1(state) :
    global endState1
    result = 0
    index = 0
    for x in state :
        if (x != endState1[index]) :
            result += 1
        index += 1
    return result

# Manhattan distance heuristic
def h2(state) :
    result = 0
    result += state.index('1')
    result += abs(state.index('2') - 1)
    result += abs(state.index('3') - 2)
    result += abs(state.index('4') - 3)
    result += abs(state.index('5') - 4)
    result += abs(state.index('6') - 5)
    result += abs(state.index('7') - 6)
    result += abs(state.index('8') - 7)
    result += abs(state.index('9') - 8)
    result += abs(state.index('A') - 9)
    result += abs(state.index('B') - 10)
    result += abs(state.index('C') - 11)
    result += abs(state.index('D') - 12)
    result += abs(state.index('E') - 13)
    result += abs(state.index('F') - 14)
    result += abs(state.index(' ') - 15)

    return result


# If the blank spot can be moved right then this will do so and return a new string with 
# the updated state.
# If the blank spot is as far right as it can go, then this will return
# -1
def moveRight(state) :
    global visitedStates
    global numCreated

    currState = list(state)
    spaceIndex = currState.index(' ')
    #print(spaceIndex)
    if (spaceIndex % 4 == 3) :
        return -1
    else :
        swapChar = currState[spaceIndex + 1]
        currState[spaceIndex] = swapChar
        currState[spaceIndex + 1] = ' '
        if (''.join(currState) in visitedStates) :
            return -1
        else :
            result = Node()
            result.data = ''.join(currState)
            numCreated += 1
            #outputPuzzle(currState)
            return result

def moveLeft(state) :
    global visitedStates
    global numCreated

    currState = list(state)
    spaceIndex = currState.index(' ')
    if (spaceIndex % 4 == 0) :
        return -1
    else :
        swapChar = currState[spaceIndex - 1]
        currState[spaceIndex] = swapChar
        currState[spaceIndex - 1] = ' '
        if (''.join(currState) in visitedStates) :
            return -1
        else :
            result = Node()
            result.data = ''.join(currState)
            numCreated += 1
            #outputPuzzle(currState)
            return result

def moveUp(state) :
    global visitedStates
    global numCreated

    currState = list(state)
    spaceIndex = currState.index(' ')
    if (spaceIndex < 4) :
        return -1
    else :
        swapChar = currState[spaceIndex - 4]
        currState[spaceIndex] = swapChar
        currState[spaceIndex - 4] = ' '
        if (''.join(currState) in visitedStates) :
            return -1
        else :
            result = Node()
            result.data = ''.join(currState)
            numCreated += 1
            #outputPuzzle(currState)
            return result

def moveDown(state) :
    global visitedStates
    global numCreated

    currState = list(state)
    spaceIndex = currState.index(' ')
    if (spaceIndex >= 12) :
        return -1
    else :
        swapChar = currState[spaceIndex + 4]
        currState[spaceIndex] = swapChar
        currState[spaceIndex + 4] = ' '
        if (''.join(currState) in visitedStates) :
            return -1
        else :
            result = Node()
            result.data = ''.join(currState)
            numCreated += 1
            #outputPuzzle(currState)
            return result

# Constructs default tree root.
def constructRoot():
    root = Node()
    root.data = initialState
    root.depth = 0
    return root
    
# outputs the entire puzzle in an easier to read format to console.
def outputPuzzle(state) :
    currState = list(state)
    counter = 0
    for x in currState :
        if (counter % 4 == 3) :
            print(x)
        else :
            sys.stdout.write(x)
            sys.stdout.write("  ")
        counter += 1
    print()


# inner class used to represent nodes on tree
class Node(object):
    def __init__(node):
        node.right = None
        node.up = None
        node.down = None
        node.left = None
        node.data = None
        node.depth = None
        node.totalCost = None

    def __repr__(self) :
        if (searchMethod == "gbfs" or searchMethod == "astar") :
            if (options == "h1") :
                return "{" + self.data + "}" +  " H1 Value: " + str(h1(self.data))
            elif (options == "h2") :
                return "{" + self.data + "}" +  " H2 Value: " + str(h2(self.data))

    def __lt__(self, other) :
        if (searchMethod == "gbfs" or searchMethod == "astar") :
            if (options == "h1") :
                return h1(self.data) + self.totalCost < h1(other.data) + other.totalCost
            else :
                return h2(self.data) + self.totalCost < h2(other.data) + other.totalCost
        else :
            return 0


main()