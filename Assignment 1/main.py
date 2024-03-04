from algo.value_iteration import value_iteration
from utils.plot import plot

def main():
    #initialize grids' reward function based on question
    reward = [[-0.04, -0.04, -0.04, -0.04, -0.04,     1],
              [-0.04,     0, -0.04, -0.04,    -1,     0],
              [-0.04,     0, -0.04,    -1, -0.04,     1],
              [-0.04,     0,    -1, -0.04,     1, -0.04],
              [-0.04,    -1, -0.04,     1,     0, -0.04],
              [-0.04, -0.04,     1, -0.04,    -1,     1]]
    #use 0 to represent walls
    #maze is skewed 90 degrees to the right so that reward[i][j] can map directly to conventional (x,y) coordinates

    #configs
    maze_length = 6
    discount_factor = 0.99

    #run value iteration on maze and print out state utilities per iteration
    value_iteration_utilities_per_iteration, value_iteration_optimal_actions = value_iteration(reward, maze_length, discount_factor)

    #show results
    for i in range(maze_length):
        for j in range(maze_length):
            print(f"({i}, {j}) : {value_iteration_optimal_actions[i][j]}")
    
    #plot results
    plot(value_iteration_utilities_per_iteration, "Value Iteration")

if __name__ == "__main__":
    main()

