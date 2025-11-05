# python_scripts
Some Python scripts that I worked on, when I first started programming

Algorithms and Data Structures Mini-Projects

Collection of small Python scripts solving algorithmic and mathematical exercises.
Each file is self-contained and runnable from the command line.

Graph Algorithms
bipartie.py

Checks if an undirected graph is bipartite using DFS.
Input: node count, edge count, then edges.
Output: two partitions or Nelze if impossible.

Linear Algebra
Linear_equations.py

Gaussian elimination with partial pivoting to solve a linear system.
Input: augmented matrix rows.
Output: solution vector.

Number Theory & Arithmetic
second_try.py

Fast modular exponentiation to compute A^B mod 100, with B given in binary.

goodnumber.py

Counts integers ≤ N whose digits all divide the number and contain no zero.

bibi.py

Formats a rational number N/M in decimal with parentheses around repeating cycles.

fraction_class.py

Fraction class with normalized arithmetic. Supports + - * \ operations and fractional input parsing.

Arrays / Geometry / Searching
algorithm2.py

Counts occurrences of target values in a sorted list using binary search for first and last occurrences.

line_intersection.py

Determines if two line segments intersect using orientation tests. Outputs ANO/NE.

magicsquare.py

Brute-forces missing values in a partially filled square; checks if it can form a valid magic square.

chessboard.py

Counts horizontal and vertical placements of an N-length tile in a grid of 0 (free) and 1 (blocked).

1.py

Prints elements of a matrix in spiral order. Reads matrix from stdin.

Data Structures
circular_queue.py

Dynamically resizing circular queue. Supports enqueue/dequeue, count, and average.

tree_set.py

Binary search tree with add, remove, contains, min, max, size, and range count.

linked_list.py

Singly linked list with deletion, rotate-last-to-front, membership checks, and sublist checks.

BFS / Simulation / Logic
roooks.py

BFS to find the minimum number of rook moves on an 8×8 board with obstacles.

laybrinth.py

Simulates a right-hand rule walker in a maze, printing the maze after each movement.

triple.py

Binary tree traversal that returns the first value where a node and both children exist and have equal values.

File & String Utilities
merging_two_files.py

Merges two sorted text files into one. Optional -i for case-insensitive comparison.

cesaremethod.py

Simple Caesar cipher shifting alphabetic characters by a provided key.

Misc
train_wagons.py

Simulates wagons on a bridge to detect the first wagon index that breaks weight/length constraints. Sliding-window approach.

How to Run

Most scripts read from standard input:

python3 script_name.py < input.txt


Some expect command-line arguments (merging_two_files.py):

python3 merging_two_files.py [-i] file1 file2 output

Notes

Each script is stand-alone and meant as practice for algorithmic techniques.

No external libraries used beyond Python standard library (unless stated inside script).

Data structures implemented from scratch for learning.
