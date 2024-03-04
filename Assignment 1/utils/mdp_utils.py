def getAdjStates(i, j, reward, maze_length):
    #determine coordinates for left, right, top, bottom states
    
    #left state is (i-1, j)
    if i == 0: # out of bounds
        left_state = (i,j)
    elif reward[i-1][j] == 0: #state is a wall
        left_state = (i,j)
    else:
        left_state = (i-1, j)

    #right state is (i+1, j)
    if i == maze_length-1: #out of bounds
        right_state = (i,j)    
    elif reward[i+1][j] == 0: #state is a wall
        right_state = (i,j)
    else:
        right_state = (i+1, j)

    #top state is (i, j+1)
    if j == maze_length-1: #out of bounds
        top_state = (i,j)
    elif reward[i][j+1] == 0: #state is a wall
        top_state = (i,j)
    else:
        top_state = (i, j+1)

    #bottom state is (i, j-1)
    if j == 0: #out of bounds
        bottom_state = (i,j)
    elif reward[i][j-1] == 0: #state is a wall
        bottom_state = (i,j)
    else:
        bottom_state = (i, j-1)

    return left_state, right_state, top_state, bottom_state

def getBestAction(reward, state, state_utilities, maze_length):
    '''
    inputs:
    reward: 2D list holding all the reward values at each state
    state: tuple (i,j) holding the coordinates of the state to be evaluated
    state_utilities: 2D list holding all state utilities in the current iteration
    maze_length: integer indicating length of maze
    '''
    i = state[0]
    j = state[1]
    if reward[i][j] == 0:
        return "Wall"
    
    best_action = ""
    utility = float(-99999.9)

    #determine coordinates for adjacent states
    left_state, right_state, top_state, bottom_state = getAdjStates(i, j, reward, maze_length)

    #calculate utilities for each action to get the action with the maximum utility
    up_action_utility = 0.8*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]]
    if up_action_utility > utility:
        utility = up_action_utility
        best_action = "Up"

    down_action_utility = 0.8*state_utilities[bottom_state[0]][bottom_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]]
    if down_action_utility > utility:
        utility = down_action_utility
        best_action = "Down"

    left_action_utility = 0.8*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]]
    if left_action_utility > utility:
        utility = left_action_utility
        best_action = "Left"

    right_action_utility = 0.8*state_utilities[right_state[0]][right_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]]
    if right_action_utility > utility:
        utility = right_action_utility
        best_action = "Right"

    #returns a string with value either "Up", "Down", "Left", "Right"
    return best_action

def getNewUtility(reward, state, action, state_utilities, maze_length, discount_factor, iteration_count):
    #implements the Bellman's Equation
    '''
    inputs:
    reward: 2D list holding all the reward values at each state
    state: tuple (i,j) holding the coordinates of the state to be evaluated
    action: string with value "Up", "Down", "Left" or "Right" to indicate the action that will be performed
    state_utilities: 2D list holding all state utilities in the current iteration
    maze_length: integer indicating length of maze
    '''
    
    i = state[0]
    j = state[1]
    if reward[i][j] == 0:
        return "Wall"
    
    new_utility = 0

    #determine coordinates for adjacent states
    left_state, right_state, top_state, bottom_state = getAdjStates(i, j, reward, maze_length)

    #calculate new utility using Bellman's Equation
    if action == "Up":
        new_utility = reward[i][j] + (discount_factor)*(0.8*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]])
        #new_utility = reward[i][j] + (discount_factor**iteration_count)*(0.8*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]])
    elif action == "Down":
        new_utility = reward[i][j] + (discount_factor)*(0.8*state_utilities[bottom_state[0]][bottom_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]])
        #new_utility = reward[i][j] + (discount_factor**iteration_count)*(0.8*state_utilities[bottom_state[0]][bottom_state[1]] + 0.1*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[right_state[0]][right_state[1]])
    elif action == "Left":
        new_utility = reward[i][j] + (discount_factor)*(0.8*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]])
        #new_utility = reward[i][j] + (discount_factor**iteration_count)*(0.8*state_utilities[left_state[0]][left_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]])
    elif action == "Right":
        new_utility = reward[i][j] + (discount_factor)*(0.8*state_utilities[right_state[0]][right_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]])
        #new_utility = reward[i][j] + (discount_factor**iteration_count)*(0.8*state_utilities[right_state[0]][right_state[1]] + 0.1*state_utilities[top_state[0]][top_state[1]] + 0.1*state_utilities[bottom_state[0]][bottom_state[1]])

    return new_utility