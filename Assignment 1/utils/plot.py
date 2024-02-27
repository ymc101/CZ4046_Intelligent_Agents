import matplotlib.pyplot as plt
import os

#plot results and save it as png file
def plot(grid_utilities, algoname: str):
    """
    function input:
    grid_utilities: {(x,y) : utility, ...}
    where (x,y) is the coordinate of a grid in the maze
    """
    #plt.figure(figsize = (16, 8))

    num_of_iterations = len(grid_utilities[0,0])
    x_values = list(range(1, num_of_iterations+1))

    for grid in grid_utilities:
        plt.plot(x_values, grid_utilities[grid], label = grid)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title('Utility Graph for ' + algoname)
    plt.xlabel('Iteration Count')
    plt.ylabel('Utility')


    plt.savefig(os.getcwd() + '/results/' + algoname + ' results graph.png')
    plt.show()
    return


#tester
"""
a = {(0,0):[1,2,3], (1,0):[2,3,4]}
plot(a, 'Value Iteration')
"""