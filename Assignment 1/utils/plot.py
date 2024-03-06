import matplotlib.pyplot as plt
import os

#plot results and save it as png file
def plot(grid_utilities_per_iteration, algoname: str):
    """
    function input:
    grid_utilities_per_iteration: {(x,y) : utility, ...}
    where (x,y) is the coordinate of a grid in the maze
    """
    plt.figure(figsize = (16, 8))

    num_of_iterations = len(grid_utilities_per_iteration[0,0])
    x_values = list(range(1, num_of_iterations+1))

    for grid in grid_utilities_per_iteration:
        plt.plot(x_values, grid_utilities_per_iteration[grid], label = grid)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title('Utility Graph for ' + algoname)
    plt.xlabel('Iteration Count')
    plt.ylabel('Utility')

    algoname.replace(" ", "_")
    plt.savefig(os.getcwd() + '/results/' + algoname + '_utility_graph.png')
    #plt.show()
    return