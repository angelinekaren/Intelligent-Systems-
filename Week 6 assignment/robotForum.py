import numpy as np

# Define rewards graph 
R = np.matrix([[0,-0.04,0,0,-0.04,0,0,0,0,0,0],
               [-0.04,0,-0.04,0,0,0,0,0,0,0,0],
               [0,-0.04,0,-0.04,0,-0.04,0,0,0,0,0],
               [0,0,-0.04,0,0,0,-1.04,0,0,0,0],
               [0,0,0,0,0,0,0,-0.04,0,0,0],
               [0,0,0,0,0,0,-1.04,0,0,-0.04,0],
               [0,0,0,0,0,-0.04,0,0,0,0,0.96],
               [0,0,0,0,0,0,0,0,-0.04,0,0],
               [0,0,0,0,0,0,0,-0.04,0,-0.04,0],
               [0,0,0,0,0,0,0,0,-0.04,0,0.96],
               [0,0,0,0,0,0,0,0,0,0,-0.04]])

# Define Q-table for actions
Q=np.matrix(np.zeros([11,11]))

# Learning rate
alpha = 0.8

# Starting point -> state #0
initial_state=0

# Find all possible actions for a given state
def available_actions(state):
    curr_state_row = R[state,]
    # If current state row is not 0, it is possible to move
    av_act = np.where(curr_state_row!=0)[1]
    return av_act

# Store available actions in the current state
available_act = available_actions(initial_state)

# Select next action to take next from the available actions at random
def sample_next_action(available_act):
    # Choose 1 random choice from available actions
    next_action = int(np.random.choice(available_act,1))
    return next_action

# Sample next action
action = sample_next_action(available_act)

# Function to update Q-matrix
def update (current_state, action, alpha):
    # Store the indices (which will be the ‘action’ number) of the maximum values along that row (current state)
    max_index = np.where(Q[action,]==np.max(Q[action,]))[1]
    
    if (max_index.shape[0] > 1):
        # Randomly choose one among all possible actions from that row 'state' (current state) 
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    
    # Store the maximum value from row 'state' after taking action in Q-matrix 
    max_value = Q[action, max_index]

    # Q-learning formula
    Q[current_state,action] = R[current_state, action] + alpha*max_value

# Updates the Q-matrix with the path chosen
update(initial_state, action, alpha)

# TRAINING

# Train over 10000 iterations
for i in range (10000):
    current_state = np.random.randint(0,int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, alpha)

print("Trained Q matrix")
print(Q/np.max(Q)* 100)

# TESTING
# Goal state = 10

# Start from the state of the robot -> state #0
current_state = 0
steps = [current_state]

# Loop until the goal state is reached
while current_state != 10:
    next_step_index = np.where(Q[current_state,]==np.max(Q[current_state,]))[1]

    if next_step_index.shape[0] > 1:
        next_step_index=int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)

    # Store the path 
    steps.append(next_step_index)
    # Go to the next state and set that state as current state
    current_state  =  next_step_index

print("Selected path")
print(steps)

"""
Trained Q matrix
[[  0.          28.66         0.           0.          28.66
    0.           0.           0.           0.           0.
    0.        ]
 [ 18.76133333   0.          41.03333333   0.           0.
    0.           0.           0.           0.           0.
    0.        ]
 [  0.          28.66         0.          28.66         0.
   56.5          0.           0.           0.           0.
    0.        ]
 [  0.           0.          41.03333333   0.           0.
    0.         -28.33333333   0.           0.           0.
    0.        ]
 [  0.           0.           0.           0.           0.
    0.           0.          41.03333333   0.           0.
    0.        ]
 [  0.           0.           0.           0.           0.
  100.        ]
 [  0.           0.           0.           0.           0.
    0.           0.           0.           0.           0.
   -4.16666667]]
Selected path
[0, 4, 7, 8, 9, 10]
"""