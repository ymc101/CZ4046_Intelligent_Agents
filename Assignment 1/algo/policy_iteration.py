from utils.mdp_utils import getBestAction
from utils.mdp_utils import getNewUtility


def policy_iteration(reward, maze_length: int, discount_factor: float):
    '''
    input parameters:
        reward(2D list containing the reward at each grid)
        maze_length: length of x by x grid maze
        discount_factor: float indicating the discount factor gamma
    '''
    #initialize maze_length by maze_length 2D arrays to store new utilities and current utilities of states
    state_utilities = [[0.0 for i in range(maze_length)] for j in range(maze_length)]
    new_state_utilities = [[0.0 for i in range(maze_length)] for j in range(maze_length)]

    grid_utilities_per_iteration = {} #to store results of grid utilities in each iteration
    for i in range(maze_length):
        for j in range(maze_length):
            if reward[i][j] != 0: #if state is not a wall
                grid_utilities_per_iteration[(i,j)] = [0.0] 

    optimal_actions = [["" for i in range(maze_length)] for j in range (maze_length)] #2D array storing optimal action at each grid, to be updated each iteration

    new_policy = [["Up" for i in range(maze_length)] for j in range (maze_length)] #2D array storing the new policy at each new iteration

    for i in range(maze_length):
        for j in range(maze_length):
            if reward[i][j] == 0: #if state is a wall
                optimal_actions[i][j] = "Wall"
                new_policy[i][j] = "Wall"

    policy_unchanged_count = 0 #number of iterations where policy remains unchanged, to be used as convergence condition
    iteration_count = 1

    while policy_unchanged_count<20:
        #perform actions in new_policy and update utilities for each state
        for i in range(maze_length):
            for j in range(maze_length):
                if reward[i][j] == 0: #if grid is a wall, skip
                    continue
                #else
                state = (i, j)
                action = new_policy[i][j]
                new_state_utilities[i][j] = getNewUtility(reward, state, action, state_utilities, maze_length, discount_factor, iteration_count) #evaluate new utility with current policy

                grid_utilities_per_iteration[state].append(new_state_utilities[i][j]) #append new utility to results

        #update state utilities table with new values
        for i in range(maze_length):
            for j in range(maze_length):
                state_utilities[i][j] = new_state_utilities[i][j]  

        #update policy based on new utilities
        for i in range(maze_length):
            for j in range(maze_length):
                if reward[i][j] == 0: #if grid is a wall, skip
                    continue
                #else
                state = (i, j)
                new_policy[i][j] = getBestAction(reward, state, state_utilities, maze_length) #calculate optimal action at current state based on new utilities

        #update convergence variable and optimal policy
        if(new_policy == optimal_actions):
            policy_unchanged_count+=1
        else:
            policy_unchanged_count = 0
            for i in range(maze_length):
                for j in range(maze_length):
                    optimal_actions[i][j] = new_policy[i][j]


        iteration_count+=1

    '''
    return variables:
        grid_utilities_per_iteration: {(x,y) : utility, ...} where (x,y) is the coordinate of a grid in the maze
        optimal_actions: 2D array storing optimal action at each state
    '''
    return grid_utilities_per_iteration, optimal_actions