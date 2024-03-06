import random

def random_maze(maze_length = int):
    #input: maze_length: integer representing the length of maze, to produce a random maze of directions maze_length by maze_length
    maze = [[0.0 for i in range(maze_length)] for j in range (maze_length)] #initialize maze

    #randomly assign each state with 4 possible utility values: 1, -1, -0.04, 0(wall)
    for i in range(maze_length):
        for j in range(maze_length):
            utility = random.randrange(1, 5)
            if utility == 1:
                maze[i][j] = 1
            elif utility == 2:
                maze[i][j] = -1
            elif utility == 3:
                maze[i][j] = -0.04
            else: #utility == 4
                maze[i][j] = 0
    return maze