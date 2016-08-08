I have added a graphical display of the solution to this program. The graphics window will open up after a solution has been found normally. Upon opening the window will trace the path to the solution performing around 1 move per second. The window can be closed using the q key. I used a third party graphics library to help graphics.py. If no solution is found the graphics window will not open.

Time comparisons: For the time comparisons I used a common puzzle. Due to DFS having trouble with any complicated puzzle I used a basic puzzle : (123456789ABC DEF) These times were all very similar due to the simplicity of the puzzle. In the individual results for each solution I have included additional time comparison information to supplement this table.

DFS		| 2.1377ms
BFS		| 2.2034ms
GBFS h1		| 1.9747ms
GBFS h2		| 2.1697ms
ASTAR h1	| 2.2502ms
ASTAR h2	| 1.8733ms
DLS		| 1.9813ms

Breadth First Search Output:
#1

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py FifteenProblem.py "12345678ACEB9DF " bfs
Initial State:
1  2  3  4
5  6  7  8
A  C  E  B
9  D  F

Search Method: BFS
Valid Input!
Puzzle complete
Depth: 12
Nodes Created: 24830
Expanded: 12375
Max Fringe Size: 12456
Time to complete:   180.9715ms

#2

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py FifteenProblem.py "123456789ABCD EF" bfs
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
D     E  F

Search Method: BFS
Valid Input!
Puzzle complete
Depth: 2
Nodes Created: 9
Expanded: 4
Max Fringe Size: 5
Time to complete:     4.2533ms

|==========================================================================================|

Depth First Output:

DFS would not finish any non-trivial puzzle, hence the simply test cases.

#1
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABCD EF" dfs
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
D     E  F

Search Method: DFS
Valid Input!
Puzzle complete
Depth: 2
Nodes Created: 5
Expanded: 2
Max Fringe Size: 3
Time to complete: 7.7922ms
#2

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABC DEF" dfs
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
   D  E  F

Search Method: DFS
Valid Input!
Puzzle complete
Depth: 3
Nodes Created: 6
Expanded: 3
Max Fringe Size: 3
Time to complete: 8.9360ms

|==============================================================================================|

Depth Limited Search
#1:

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABC DEF" dls 3
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
   D  E  F

Search Method: DLS
Options: 3
Valid Input!
Puzzle complete
Depth: 3
Nodes Created: 6
Expanded: 3
Max Fringe Size: 3
Time to complete: 9.7160ms

#2
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABC DEF" dls 2
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
   D  E  F

Search Method: DLS
Options: 2
Valid Input!
No solution found
Depth: -1
Nodes Created: 0
Expanded: 0
Max Fringe Size: 0
Time to complete: 0

|==============================================================================================|

Greedy Best First Search:
#1 Heuristic 1:
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789 ABCDEF" gbfs h1
Initial State:
1  2  3  4
5  6  7  8
9     A  B
C  D  E  F

Search Method: GBFS
Options: h1
Valid Input!
Puzzle complete
Depth: 27
Nodes Created: 57
Expanded: 27
Max Fringe Size: 4
Time to complete: 10.0937ms

#2 Heuristic 1:
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789A BCDEF" gbfs h1
Initial State:
1  2  3  4
5  6  7  8
9  A     B
C  D  E  F

Search Method: GBFS
Options: h1
Valid Input!
Puzzle complete
Depth: 26
Nodes Created: 54
Expanded: 26
Max Fringe Size: 4
Time to complete: 4.8510ms

#1 Heuristic 2:

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789A BCDEF" gbfs h2
Initial State:
1  2  3  4
5  6  7  8
9  A     B
C  D  E  F

Search Method: GBFS
Options: h2
Valid Input!
No solution found
Depth: -1
Nodes Created: 0
Expanded: 0
Max Fringe Size: 0
Time to complete: 5.5182ms

#2 Heuristic 2:


C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py FifteenProblem.py "123456789 ABCDEF" gbfs h2
Initial State:
1  2  3  4
5  6  7  8
9     A  B
C  D  E  F

Search Method: GBFS
Options: h2
Valid Input!
No solution found
Depth: -1
Nodes Created: 0
Expanded: 0
Max Fringe Size: 0
Time to complete:     2.8759ms

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABC DEF" gbfs h2
Initial State:
1  2  3  4
5  6  7  8
9  A  B  C
   D  E  F

Search Method: GBFS
Options: h2
Valid Input!
Puzzle complete
Depth: 3
Nodes Created: 7
Expanded: 3
Max Fringe Size: 3
Time to complete: 4.3305ms

|==============================================================================================|

AStar
#1 Heuristic 1

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789 ABCDEF" astar h1
Initial State:
1  2  3  4
5  6  7  8
9     A  B
C  D  E  F

Search Method: ASTAR
Options: h1
Valid Input!
Puzzle complete
Depth: 21
Nodes Created: 135863
Expanded: 68672
Max Fringe Size: 67192
Time to complete: 9620.0856ms

#2 Heuristic 1

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789A BCDEF" astar h1
Initial State:
1  2  3  4
5  6  7  8
9  A     B
C  D  E  F

Search Method: ASTAR
Options: h1
Valid Input!
Puzzle complete
Depth: 20
Nodes Created: 96164
Expanded: 48449
Max Fringe Size: 47716
Time to complete: 6320.5331ms

#1 Heuristic 2

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "1234567 89ABCDEF" astar h2
Initial State:
1  2  3  4
5  6  7
8  9  A  B
C  D  E  F

Search Method: ASTAR
Options: h2
Valid Input!
Puzzle complete
Depth: 34
Nodes Created: 3355614
Expanded: 1777594
Max Fringe Size: 1578021
Time to complete: 521597.7100ms

#2 Heuristic 2

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789 ABCDEF" astar h2
Initial State:
1  2  3  4
5  6  7  8
9     A  B
C  D  E  F

Search Method: ASTAR
Options: h2
Valid Input!
Puzzle complete
Depth: 21
Nodes Created: 39483
Expanded: 19822
Max Fringe Size: 19662
Time to complete: 4215.1201ms

|==============================================================================================|
