def main():
    import sys
    # Perform input validation
    validInput = True
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

def constructTree(theInitialState):
    root = Node()
    root.data = theInitialState
    print(root.data)
    
class Node(object):
    def initNode(aNode):
        aNode.left = None
        aNode.right = None
        aNode.data = None

main()