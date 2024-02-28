from utils.mdp_utils import getBestAction
from utils.mdp_utils import getNewUtility


def value_iteration(reward, maze_length: int):
    '''
    input parameters:
        reward(2D list containing the reward at each grid)
        maze_length: length of x by x grid maze
    '''

    #initialize maze_length by maze_length 2D arrays to store new utilities and current utilities of states
    state_utilities = [[0.0 for i in range(maze_length)] for j in range(maze_length)]
    new_state_utilities = [[0.0 for i in range(maze_length)] for j in range(maze_length)]

    grid_utilities_per_iteration = {} #to store results of grid utilities in each iteration
    for i in range(maze_length):
        for j in range(maze_length):
            grid_utilities_per_iteration[(i,j)] = [0.0] 

    avg_utility_change = 1 #loop variable to determine if algorithm has converged
    sum_utility_change = 0

    while avg_utility_change > 0.001: 
        #iterate through every state and update state utilities based on optimal action 
        for i in range(maze_length):
            for j in range(maze_length):
                if reward[i][j] == 0: #if grid is a wall, skip
                    continue
                #else
                state = (i, j)
                best_action = getBestAction(reward, state, state_utilities) #calculate optimal action at current state
                new_state_utilities[i][j] = getNewUtility(reward, state, best_action, state_utilities) #get new utility with Bellman's Equation

                grid_utilities_per_iteration[state].append(new_state_utilities[i][j]) #append new utility to results

                sum_utility_change += abs(new_state_utilities[i][j] - state_utilities[i][j]) #get change in utility from previous iteration

        avg_utility_change = sum_utility_change/(maze_length**2) #average change in utility from previous iteration

        #update state utilities table with new values
        for i in range(maze_length):
            for j in range(maze_length):
                state_utilities[i][j] = new_state_utilities[i][j]   


    optimal_actions = [[0 for i in range(maze_length)] for j in range (maze_length)] #2D array storing optimal action at each grid

    for i in range(maze_length):
        for j in range(maze_length):
            state = (i, j)
            optimal_actions[i][j] = getBestAction(reward, state, state_utilities)
    '''
    return variables:
        grid_utilities_per_iteration: {(x,y) : utility, ...} where (x,y) is the coordinate of a grid in the maze
        optimal_actions: 2D array storing 
    '''
    return grid_utilities_per_iteration, optimal_actions