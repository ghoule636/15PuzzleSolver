import sys

def main():
    from collections import deque
    global endState 
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates

    endState =  "123456789ABCDEF "

    fringe = deque()
    visitedStates = set()
    validInput = True

    # Perform input validation
    if (len(sys.argv) < 3 or len(sys.argv) > 4) :
        print("Invalid Command Line Arguments!")
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
            print("Initial State: " + initialState)
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
        DFS(treeRoot)

def DFS(node) :
    checkRight = moveRight(node.data)
    if (checkRight != -1) :
        fringe.append(node)
        DFS(checkRight)
    else :
        print("not right")

# If the blank spot can be moved right then this will do so and return a new string with 
# the updated state.
# If the blank spot is as far right as it can go, then this will return
# -1
def moveRight(state) :
    currState = list(state)
    spaceIndex = currState.index(' ')
    print(spaceIndex)
    if (spaceIndex % 4 == 3) :
        print("Space Index modded", spaceIndex % 4)
        return -1
    else :
        swapChar = currState[spaceIndex + 1]
        currState[spaceIndex] = swapChar
        currState[spaceIndex + 1] = ' '
        result = Node()
        result.data = currState
        outputPuzzle(currState) # output
        return result

def moveDown(state) :
    currState = list(state)


    outputPuzzle(currState)

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