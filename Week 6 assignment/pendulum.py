import numpy as np
import gym
import random

# Create Taxi environment
env = gym.make('Taxi-v3', render_mode='rgb_array')

# Initialize q-table
qtable = np.zeros([env.observation_space.n, env.action_space.n])

# Hyperparameters
learning_rate = 0.9
discount_rate = 0.8 # give more or less importance to the next reward
epsilon = 1.0 # explore or exploit
decay_rate= 0.005

# Training variables
num_episodes = 10000
max_steps = 1000 # per episode

# Training
for episode in range(num_episodes):

    # Reset the environment
    state = env.reset()
    done = False

    for s in range(max_steps):
        # Exploration-exploitation tradeoff
        if random.uniform(0,1) < epsilon:
            # Explore the action space
            action = env.action_space.sample()
        else:
            # Error handling
            # Check if state is an integer
            if isinstance(state, int):
                pass
            else:
                state = state[0]
            # Exploit learned values
            action = np.argmax(qtable[state,:])

        # Take action and observe reward
        new_state, reward, done, _, _ = env.step(action)

        if isinstance(state, int):
            pass
        else:
            state = state[0]

        # Q-learning algorithm
        qtable[state,action] = qtable[state,action] + learning_rate * (reward + discount_rate * np.max(qtable[new_state,:])-qtable[state,action])

        # Update state with the new state
        state = new_state

        # If done, finish episode (break the loop)
        if done == True:
            break

    # Decrease epsilon
    epsilon = np.exp(-decay_rate*episode)

print(f"Training completed over {num_episodes} episodes")
input("Press Enter to watch trained agent...")

# Watch trained agent
state = env.reset()
done = False
rewards = 0

for s in range(max_steps):
    print(f"TRAINED AGENT")
    print("Step {}".format(s+1))

    # Error handling
    if isinstance(state, int):
        pass
    else:
        state = state[0]

    # Choose the action with the max expected reward i.e. max Q-value
    action = np.argmax(qtable[state,:])
    new_state, reward, done, _, _ = env.step(action)
    rewards += reward
    env.render()
    print(f"score: {rewards}")
    state = new_state

    if done == True:
        print("Done")
        break

env.close()