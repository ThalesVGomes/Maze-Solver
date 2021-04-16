def read_maze(file_name):
    """Reads a .txt file that must have the following format:
    First line - number_of_lines number_of_columns
    Second line - line_of_origin_point column_of_origin_point
    Third line - line_of_destination_point column_of_destination_point
    Maze -> where 0 = empty space and -1 = wall

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
    """
    file = open(file_name, 'r')

    nlin, ncol = file.readline().split()
    # Reads the first line which contains the number of lines, columns in the maze
    nlin, ncol = int(nlin), int(ncol)

    lin_origin, col_origin = file.readline().split()
    # Reads the second line which contains the location of the starting point in the maze
    lin_origin, col_origin = int(lin_origin), int(col_origin)

    lin_end, col_end = file.readline().split()
    # Reads the third line which contains the location of the ending point in the maze
    lin_end, col_end = int(lin_end), int(col_end)

    maze = []
    line = [-1] * (ncol+2)
    for i in range(nlin+2):
        maze.append(line[:])

    for i in range(nlin):
        line = file.readline().split()
        line = [int(value) for value in line]
        maze[i + 1][1:-1] = line[:]

    maze[lin_end][col_end] = 1

    return maze, (lin_origin, col_origin), (lin_end, col_end)


def mark_maze(matrix, destination):
    """Marks the distance of the nodes in relation to the destination"""
    marks = [destination]
    start = end = 1

    while start <= end:

        line = marks[start - 1][0]
        column = marks[start - 1][1]

        num = matrix[line][column] + 1

        if matrix[line - 1][column] == 0:
            matrix[line - 1][column] = num
            marks.append((line - 1, column))

        if matrix[line + 1][column] == 0:
            matrix[line + 1][column] = num
            marks.append((line + 1, column))

        if matrix[line][column - 1] == 0:
            matrix[line][column - 1] = num
            marks.append((line, column - 1))

        if matrix[line][column + 1] == 0:
            matrix[line][column + 1] = num
            marks.append((line, column + 1))

        start += 1
        end = len(marks)
    return matrix


def solve_maze(matrix, origin, destination, export=False):
    """Find a path that links the origin with the destination
     in a maze in the format of a matrix"""
    path = [origin]
    origin_line, origin_col = origin[0], origin[1]
    destination_line, destination_col = destination[0], destination[1]
    last_value = matrix[origin_line][origin_col]
    while last_value > 1:

        line = path[-1][0]
        column = path[-1][1]

        if matrix[line - 1][column] == last_value - 1:
            last_value = matrix[line - 1][column]
            path.append((line - 1, column))

        elif matrix[line + 1][column] == last_value - 1:
            last_value = matrix[line + 1][column]
            path.append((line + 1, column))

        elif matrix[line][column - 1] == last_value - 1:
            last_value = matrix[line][column - 1]
            path.append((line, column - 1))

        elif matrix[line][column + 1] == last_value - 1:
            last_value = matrix[line][column + 1]
            path.append((line, column + 1))

    if len(path) == 1 or path[-1] != destination:  # No solution
        return None

    wall = 'X'
    solution = '+'

    for lin in range(len(matrix)):
        for col in range(len(matrix[lin])):
            if matrix[lin][col] == -1:
                matrix[lin][col] = wall
            elif matrix[lin][col] > -1:
                matrix[lin][col] = ' '

    for node in path:
        lin_node = node[0]
        col_node = node[1]
        matrix[lin_node][col_node] = solution

    matrix[origin_line][origin_col] = 'A'
    matrix[destination_line][destination_col] = 'B'

    if export:
        export_maze(matrix)

    return matrix


def export_maze(maze):
    """Export the maze solution to a .txt file"""
    file_name = input('Output file name: ')
    with open(file_name, 'w') as file:
        for line in maze:
            for pos, value in enumerate(line):
                if pos == len(line)-1:
                    file.write(value)
                else:
                    file.write(value + '\t')
            file.write('\n')


def color_path(point):
    return '\033[1;31;40m' + point + '\033[0m'  # Colors the terminal in red


def print_solution(solved_maze):
    """Prints the solved maze with a red path to the terminal"""
    for line in solved_maze:
        for pos, value in enumerate(line):
            if value == '+':
                print(color_path(value), end='\t')
            else:
                print(value, end='\t')
        print()


if __name__ == '__main__':
    import os

    maze_file = input('Path of the .txt containing the maze: ')
    file_extension = os.path.splitext(maze_file)[1]
    while not os.path.exists(maze_file) or file_extension != '.txt':
        if not os.path.exists(maze_file):
            print(f'There is no file with this path "{maze_file}"')
        else:
            print('Your file must be in .txt format!')
        print()
        maze_file = input('Path of the .txt containing the maze: ')

    maze, origin, destination = read_maze(maze_file)
    marked_maze = mark_maze(matrix=maze, destination=destination)
    solved_maze = solve_maze(matrix=marked_maze, origin=origin, destination=destination, export=False)
    if solved_maze:  # Check if there is a solution to the maze
        print_solution(solved_maze=solved_maze)
    else:
        print(f'There is no solution for the maze "{maze_file}".')
