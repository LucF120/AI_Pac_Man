import sys
import os 

sys.path.append(os.path.abspath("../Pacman_Training"))

import torch

from Pacman_reload_dqn import load_execution
from pacman_neural_network import DQN
from custom_pacman_env import PacmanEnv 

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

# Create the Pacman environment
env = PacmanEnv()
# Uncomment to have a display
env = PacmanEnv(render_mode="human")

observation, info = env.reset()
total_reward = 0
num_steps = 0
while True:
    num_steps += 1
    blinky_action = env.ghost_action_space.sample()
    pinky_action = env.ghost_action_space.sample()
    inky_action = env.ghost_action_space.sample()
    clyde_action = env.ghost_action_space.sample()
    actions = (blinky_action, pinky_action, inky_action, clyde_action)
    observation, reward, game_over = env.step(actions)
    total_reward += reward 
    print(f"STEP: {num_steps}")
    if game_over:
        print(f"GAME OVER.   Total Reward: {total_reward}       Num Steps: {num_steps}")
        observation, info = env.reset()
        num_steps = 0
        total_reward = 0


# n_actions = env.pacman_action_space.n
# policy_net = DQN(n_actions).to(device)

# load_execution(policy_net, only_policy_net=True, dirpath="")

# def select_action(state):
#     return policy_net(state).max(1).indices.view(1, 1)


# # Test environment
# env.render()

# # Test moving right
# for i in range(20):
#     env.move_pacman(2)



# #Test moving left
# for i in range(50):
#     env.move_pacman(3)



# # Test moving up
# for i in range(20):
#     env.move_pacman(1)


# # Test moving down
# for i in range(20):
#     env.move_pacman(4)

# for i in range(100):
#     env.move_pacman(env.pacman_action_space.sample())

# for i in range(1000):
#     env.move_blinky(env.ghost_action_space.sample())

# state = env.grid 
# env.render()
# #Test random movements
# for i in range(100):
#     state = torch.tensor(state, device=device, dtype=torch.float32).unsqueeze(0) / 255.0
#     state = state.unsqueeze(1)
#     action = select_action(state)
#     print(f"Action: {action.item()}")
#     env.move_blinky(env.ghost_action_space.sample())
#     env.move_pacman(action.item())
#     env.render()
#     state = env.grid 
