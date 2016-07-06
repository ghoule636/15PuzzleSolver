from distutils import sys
def main():
    import sys
    from collections import deque

    global endState 
    global initialState
    global searchMethod
    global options
    global fringe
    global visitedStates
    fringe = deque()
    visitedStates = set()

    endState =  "123456789ABCDEF "

    if (len(sys.argv) < 3 or len(sys.argv) > 4) :
        print("Invalid Command Line Arguments!")
    else :
        initialState = sys.argv[1]
        searchMethod = sys.argv[2]
        print("Initial State: " + initialState)
        print("Search Method: " + searchMethod)
        if (len(sys.argv) == 4) :
            options = sys.argv[3]
            print("Options: " + options)


        # Everything is good!
        treeRoot = constructRoot()
        if (searchMethod.lower() == "bfs" or searchMethod.lower() == "dfs") :
            BFSorDFS(treeRoot)

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


def moveRight(state) :
    currState = list(state)
    outputPuzzle(currState)
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
        return result


def constructRoot():
    root = Node()
    root.data = initialState
    return root
    
class Node(object):
    def __init__(node):
        node.right = None
        node.ctrRight = None
        node.ctrLeft = None
        node.left = None
        node.data = None

def outputPuzzle(state) :
    import sys
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

main()