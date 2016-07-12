import sys
from collections import deque

def main():
    global endState1
    global endState2
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates

    endState1 =  "123456789ABCDEF "
    endState2 =  "123456789ABCDFE "

    fringe = deque()
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
            print("Search Method: " + searchMethod)
            if (len(sys.argv) == 4) :
                options = sys.argv[3]
                if (checkOptions(searchMethod, options)) :
                    print("Options: " + options)
                else :
                    print("Invalid option")
                    validInput = False
            elif (searchMethod.lower() == "astar" or searchMethod.lower() == "gbfs") :
                print("These search methods require option h1 or h2")
                validInput = False
    if (validInput) :
        print("Valid Input!")
        treeRoot = constructRoot()
        if (searchMethod.lower() == "bfs" or searchMethod.lower() == "dfs") :
            BFSorDFS(treeRoot)

# This function checks if the initial state input by the user is valid. 
def checkInitState(initState) :
    requiredChars = {'1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', ' '}
    result = True
    listState = list(initState)
    if (len(initState) < 16) :
        result = False
    index = 0
    for x in listState :
        if (listState[index] == 'x' or listState[index].lower() not in requiredChars) :
            result = False
        else :
            listState[index] = 'x'
        index += 1
    return result

# This function checks if the search method input by the user is valid.
def checkSearchMethod(inputSearch) :
    searchMethods = {"bfs", "dfs", "gbfs", "astar", "id"}
    result = True
    if (inputSearch.lower() not in searchMethods) :
        result = False
    return result

def checkOptions(searchMethod, options) :
    result = True
    if (searchMethod.lower() == "gbfs" or searchMethod.lower() == "astar") :
        if (options != "h1" and options != "h2") :
            result = False
    else :
        result = False
    return result

def BFSorDFS(treeRoot) :
    visitedStates.add(treeRoot.data)
    if (searchMethod.lower() == "dfs") :
        DFS(treeRoot, 0)

def DFS(node, depth) :
    if (node.data == endState1 or node.data == endState2) :
        print("Puzzle complete")
        print(depth)
        return 1
    checkRight = moveRight(node.data)
    if (checkRight != -1) :
        outputPuzzle(checkRight.data)
        fringe.append(node)
        #print(checkRight.data)
        visitedStates.add(checkRight.data)
        #node.data = checkRight.data
        if (DFS(checkRight, depth + 1) == 1) :
            return 1
    checkDown = moveDown(node.data)
    if (checkDown != -1) :
        outputPuzzle(checkDown.data)
        fringe.append(node)
        visitedStates.add(checkDown.data)
        #node.data = checkDown.data
        if (DFS(checkDown, depth + 1) == 1) :
            return 1
    checkLeft = moveLeft(node.data)
    if (checkLeft != -1) :
        outputPuzzle(checkLeft.data)
        fringe.append(node)
        visitedStates.add(checkLeft.data)
        if (DFS(checkLeft, depth + 1) == 1) :
            return 1
    checkUp = moveUp(node.data)
    if (checkUp != -1) :
        outputPuzzle(checkUp.data)
        fringe.append(node)
        visitedStates.add(checkUp.data)
        if (DFS(checkUp, depth + 1) == 1) :
            return 1

    return


# If the blank spot can be moved right then this will do so and return a new string with 
# the updated state.
# If the blank spot is as far right as it can go, then this will return
# -1
def moveRight(state) :
    currState = list(state)
    spaceIndex = currState.index(' ')
    #print(spaceIndex)
    if (spaceIndex % 4 == 3) :
        #print("Space Index modded", spaceIndex % 4)
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
            #outputPuzzle(currState)
            return result

def moveLeft(state) :
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
            #outputPuzzle(currState)
            return result

def moveUp(state) :
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
            #outputPuzzle(currState)
            return result

def moveDown(state) :
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
            #outputPuzzle(currState)
            return result

# Constructs default tree root.
def constructRoot():
    root = Node()
    root.data = initialState
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
        node.ctrRight = None
        node.ctrLeft = None
        node.left = None
        node.data = None

main()