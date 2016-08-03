Breadth First Search Output:
#1
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789 ABCDEF" bfs
Initial State:
1  2  3  4
5  6  7  8
9     A  B
C  D  E  F

Search Method: BFS
Valid Input!

1  2  3  4
5  6  7  8
9  A  B  C
D  F  E

Puzzle complete
Depth: 21
Nodes Created: 11039685
Expanded: 5836325
Max Fringe Size: 5203361

#2
C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789ABCD EF" bfs
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

|==========================================================================================|

Depth First Output:

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
Max Fringe Size: 

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

#2 Heuristic 2:

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

C:\Users\Gabriel\Source\Repos\15PuzzleSolver>py fifteenproblem.py "123456789AB CDEF" gbfs h2
Initial State:
1  2  3  4
5  6  7  8
9  A  B
C  D  E  F

Search Method: GBFS
Options: h2
Valid Input!
No solution found
Depth: -1
Nodes Created: 0
Expanded: 0
Max Fringe Size: 0

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

|==============================================================================================|
