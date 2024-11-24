# This file runs a pacman using the policynet 
from itertools import count
import gymnasium as gym
import ale_py
import random 
import time 
from pacman_neural_network import DQN
from Pacman_reload_dqn import load_execution, save_execution
import torch

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", render_mode="human", obs_type="grayscale")
print(env.spec)
print(env.metadata)
print(env.action_space)
print(env.observation_space)
n_actions = env.action_space.n
policy_net = DQN(n_actions).to(device)

# This always loads from the previous_run/ folder. Make sure the policy_net.pth file is located here. 
load_execution(policy_net, only_policy_net=True)

def select_action(state):
    return policy_net(state).max(1).indices.view(1, 1)


for i in range(10000):
    # Initialize the environment and get its state
    state, info = env.reset()
    #Crop out the score, and blank space at the top of the game 
    state = state[20:200, 0:]
    state = torch.tensor(state, device=device, dtype=torch.float32).unsqueeze(0) / 255.0
    state = state.unsqueeze(1)
    previous_reward = 0
    for t in count():
        action = select_action(state)
        observation, reward, terminated, truncated, info = env.step(action.item())
        if reward != previous_reward and reward != 0:
            print(f"Step {t} Reward: {reward}")

        #Crop out the score, and blank space at the top of the game 
        observation = observation[20:200, 0:]

        done = terminated or truncated

        if terminated:
            next_state = None
        else:
            next_state = torch.tensor(observation, dtype=torch.float32, device=device).unsqueeze(0) / 255.0
            next_state = next_state.unsqueeze(0)
        
        # Move to the next state
        state = next_state
        previous_reward = reward 
        if done:
            break
