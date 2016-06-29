def main():
    import sys
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

        

main()