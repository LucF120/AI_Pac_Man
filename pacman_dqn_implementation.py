from itertools import count
import matplotlib.pyplot as plt
import gymnasium as gym
import ale_py
import random 
import numpy as np 
import torch
from pacman_neural_network import DQN
from collections import namedtuple, deque
import math 
from torch import max
import cv2
import torchvision.transforms.v2 as transforms 
from Pacman_reload_dqn import load_execution, save_execution
# Referenced: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

print("Using the following device: ", device)


gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", obs_type="grayscale")

Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))


class ReplayMemory(object):

    def __init__(self, capacity):
        self.memory = deque([], maxlen=capacity)

    def push(self, *args):
        """Save a transition"""
        self.memory.append(Transition(*args))

    def sample(self, batch_size):
        return random.sample(self.memory, batch_size)

    def __len__(self):
        return len(self.memory)

# BATCH_SIZE is the number of transitions sampled from the replay buffer
# GAMMA is the discount factor as mentioned in the previous section
# EPS_START is the starting value of epsilon
# EPS_END is the final value of epsilon
# EPS_DECAY controls the rate of exponential decay of epsilon, higher means a slower decay
# TAU is the update rate of the target network
# LR is the learning rate of the ``AdamW`` optimizer
BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 40000    
TAU = 0.005
LR = 1e-5


num_episodes = 1000
# This decides how many episodes until running save_execution() 
save_rate = 100

# Get number of actions from gym action space
n_actions = env.action_space.n
# Get the number of state observations
state, info = env.reset()
policy_net = DQN(n_actions).to(device)
target_net = DQN(n_actions).to(device)
target_net.load_state_dict(policy_net.state_dict())

memory = ReplayMemory(10000)

optimizer = torch.optim.AdamW(policy_net.parameters(), lr=LR, amsgrad=True)

steps_done = 0

#Uncomment this to load from a previous execution 
# Note: The num_episodes must be set above. 
# BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TAU, LR, steps_done = load_execution(policy_net, target_net, memory)

def select_action(state):
    global steps_done
    sample = random.random()
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
        math.exp(-1. * steps_done / EPS_DECAY)
    steps_done += 1
    if sample > eps_threshold:
        with torch.no_grad():
            # t.max(1) will return the largest column value of each row.
            # second column on max result is index of where max element was
            # found, so we pick action with the larger expected reward.
            return policy_net(state).max(1).indices.view(1, 1)
    else:
        return torch.tensor([[env.action_space.sample()]], device=device, dtype=torch.long)

def optimize_model():
    if len(memory) < BATCH_SIZE:
        return 0
    transitions = memory.sample(BATCH_SIZE)
    # Transpose the batch (see https://stackoverflow.com/a/19343/3343043 for
    # detailed explanation). This converts batch-array of Transitions
    # to Transition of batch-arrays.
    batch = Transition(*zip(*transitions))

    # Compute a mask of non-final states and concatenate the batch elements
    # (a final state would've been the one after which simulation ended)
    non_final_mask = torch.tensor(tuple(map(lambda s: s is not None,
                                          batch.next_state)), device=device, dtype=torch.bool)
    non_final_next_states = torch.cat([s for s in batch.next_state
                                                if s is not None])
    state_batch = torch.cat(batch.state)
    action_batch = torch.cat(batch.action)
    reward_batch = torch.cat(batch.reward)

    # Compute Q(s_t, a) - the model computes Q(s_t), then we select the
    # columns of actions taken. These are the actions which would've been taken
    # for each batch state according to policy_net
    state_action_values = policy_net(state_batch).gather(1, action_batch)

    # Compute V(s_{t+1}) for all next states.
    # Expected values of actions for non_final_next_states are computed based
    # on the "older" target_net; selecting their best reward with max(1).values
    # This is merged based on the mask, such that we'll have either the expected
    # state value or 0 in case the state was final.
    next_state_values = torch.zeros(BATCH_SIZE, device=device)
    with torch.no_grad():
        next_state_values[non_final_mask] = target_net(non_final_next_states).max(1).values
    # Compute the expected Q values
    expected_state_action_values = (next_state_values * GAMMA) + reward_batch

    # Compute Huber loss
    criterion = torch.nn.SmoothL1Loss()
    loss = criterion(state_action_values, expected_state_action_values.unsqueeze(1))

    # Optimize the model
    optimizer.zero_grad()
    loss.backward()
    # In-place gradient clipping
    torch.nn.utils.clip_grad_value_(policy_net.parameters(), 100)
    optimizer.step()
    return loss.item()


total_rewards = []
for i_episode in range(num_episodes):
    # Save the execution every save_rate # of episodes 
    if(i_episode != 0 and i_episode % save_rate == 0):
        save_execution(target_net.state_dict(), policy_net.state_dict(), memory, BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TAU, LR, steps_done, total_rewards)
    
    running_loss = 0.0
    # Initialize the environment and get its state
    state, info = env.reset()
    #Crop out the score, and blank space at the top of the game 
    state = state[20:200, 0:]
    state = torch.tensor(state, device=device, dtype=torch.float32).unsqueeze(0) / 255.0
    state = state.unsqueeze(1)
    total_reward = 0
    previous_action = select_action(state)
    wait_until_frame = 0
    for t in count():
        current_frame = info['episode_frame_number']
        # Ignore the first 140 frames, since the game hasn't started yet 
        # Also, only choose an action every 4th frame
        #If Pacman previously died, wait 128 frames after they lost a life 
        if current_frame < 160 or current_frame % 4 != 0 or current_frame < wait_until_frame:
            action = previous_action 
        else:
            action = select_action(state)
            wait_until_frame = 0
        observation, reward, terminated, truncated, info = env.step(action.item())

        #Crop out the score, and blank space at the top of the game 
        observation = observation[20:200, 0:]
        
        # # Manually change the reward to -100 if pacman lost a life
        if info['lives'] < num_lives:
            reward = -100
            # Set the frame to wait until to 128 greater than now, since this is roughly how long it takes for pacman to respawn 
            wait_until_frame = current_frame + 128 
        done = terminated or truncated

        if terminated:
            next_state = None
            # Set the reward to -100 if pacman loses
            if info['lives'] == 0:
                reward = -1000
            else:
                # If pacman wins, give a huge reward
                reward = 100000
        else:
            next_state = torch.tensor(observation, dtype=torch.float32, device=device).unsqueeze(0) / 255.0
            next_state = next_state.unsqueeze(0)
        
        total_reward += reward
        reward = torch.tensor([reward], device=device)


        # Store the transition in memory
        memory.push(state, action, next_state, reward)

        # Move to the next state
        state = next_state

        # Perform one step of the optimization (on the policy network)
        
        running_loss += optimize_model()

        # Soft update of the target network's weights
        # θ′ ← τ θ + (1 −τ )θ′
        target_net_state_dict = target_net.state_dict()
        policy_net_state_dict = policy_net.state_dict()
        for key in policy_net_state_dict:
            target_net_state_dict[key] = policy_net_state_dict[key]*TAU + target_net_state_dict[key]*(1-TAU)
        target_net.load_state_dict(target_net_state_dict)

        if done:
            break
        num_lives = info['lives']
    print(f"Episode {i_episode} training loss: {running_loss}.          Total Reward: {total_reward}")
    total_rewards.append(total_reward)

# One final save before terminating 
save_execution(target_net.state_dict(), policy_net.state_dict(), memory, BATCH_SIZE, GAMMA, EPS_START, EPS_END, EPS_DECAY, TAU, LR, steps_done, total_rewards)
print('Complete')