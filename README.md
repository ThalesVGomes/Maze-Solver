# Maze-Solver
### Just pure python with no external dependencies

Find a path (if exists) between two points in a maze.

The code reads a .txt file that must have the following format:
First line - number_of_lines number_of_columns
Second line - line_of_origin_point column_of_origin_point
Third line - line_of_destination_point column_of_destination_point
Maze -> 0 = empty space and -1 = wall

Example of file format:  
    6  11  
    1  1  
    6  11  
    0  0 -1 -1  0  0  0  0  0  0  0  
    0 -1  0 -1 -1  0 -1  0 -1 -1  0  
    0  0 -1  0  0  0 -1  0  0  0  0  
    0 -1  0 -1  0  0  0 -1 -1  0  0  
    0  0  0 -1  0 -1  0  0  0 -1  0  
    0 -1  0  0  0  0  0  0 -1  0  0  
    
After reading the file the algorithm finds a path between
the origin and the destination and prints it on screen.

You can save the solution in a .txt file changing the argument
'export' in the main function to True (run_maze_solver(export=True)).
