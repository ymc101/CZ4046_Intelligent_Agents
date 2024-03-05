from algo.value_iteration import value_iteration
from algo.policy_iteration import policy_iteration
from utils.plot import plot
import os

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

    print("Running Value Iteration...")
    #run value iteration on maze and print out state utilities per iteration
    value_iteration_utilities_per_iteration, value_iteration_optimal_actions = value_iteration(reward, maze_length, discount_factor)

    #save optimal policy in txt file in results directory
    filepath = os.getcwd() + '/results/value_iteration_optimal_policy.txt' 
    f = open(filepath, "w")
    f.write("Optimal Policy obtained using Value Iteration:\n")
    for i in range(maze_length):
        for j in range(maze_length):
            #print(f"({i}, {j}) : {value_iteration_optimal_actions[i][j]}")
            f.write(f"({i}, {j}) : {value_iteration_optimal_actions[i][j]}\n")
    f.close()

    #plot results, save as png in results directory
    plot(value_iteration_utilities_per_iteration, "Value Iteration")

    print("Value Iteration successfully concluded!")
    print("Running Policy Iteration...")

    #run policy iteration on maze and print out state utilities per iteration
    policy_iteration_utilities_per_iteration, policy_iteration_optimal_actions = policy_iteration(reward, maze_length, discount_factor)

    #save optimal policy in txt file in results directory
    filepath = os.getcwd() + '/results/policy_iteration_optimal_policy.txt' 
    f = open(filepath, "w")
    f.write("Optimal Policy obtained using Policy Iteration:\n")
    for i in range(maze_length):
        for j in range(maze_length):
            #print(f"({i}, {j}) : {policy_iteration_optimal_actions[i][j]}")
            f.write(f"({i}, {j}) : {policy_iteration_optimal_actions[i][j]}\n")
    f.close()
    
    #plot results
    plot(policy_iteration_utilities_per_iteration, "Policy Iteration")

    print("Policy Iteration successfully concluded!")
    print("end of program")
    

if __name__ == "__main__":
    main()

