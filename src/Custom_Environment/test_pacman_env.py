import sys
import os 

sys.path.append(os.path.abspath("../Pacman_Training"))

import torch
import numpy as np 

from custom_pacman_env import PacmanEnv 
from ghosts_ffn import GhostFNN

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

# Create the Pacman environment
#env = PacmanEnv()
# Uncomment to have a display
env = PacmanEnv(render_mode="human")

#Load the ghosts policy
ghost_policy_net = GhostFNN().to(device)
ghost_policy_net.load_state_dict(torch.load(f"previous_run/ghost_policy_net.pth", weights_only=True, map_location=device))


# Helper function for getting the inputs for the neural network
def get_inputs():
    blinky_coordinates = env.blinky["coordinates"][0]
    if env.pinky["spawned"]:
        pinky_coordinates = env.pinky["coordinates"][0]
    else:
        pinky_coordinates = [80, 80]

    if env.inky["spawned"]:
        inky_coordinates = env.inky["coordinates"][0]
    else:
        inky_coordinates = [80, 80]

    if env.clyde["spawned"]:
        clyde_coordinates = env.clyde["coordinates"][0]
    else:
        clyde_coordinates = [80, 80]
    pacman_coordinates = env.pacman[0]
    inputs = np.array([
        blinky_coordinates[0] / 160.0, 
        blinky_coordinates[1] / 180.0, 
        pinky_coordinates[0] / 160.0, 
        pinky_coordinates[1] / 180.0, 
        inky_coordinates[0] / 160.0, 
        inky_coordinates[1] / 180.0, 
        clyde_coordinates[0] / 160.0, 
        clyde_coordinates[1] / 180.0, 
        pacman_coordinates[0] / 160.0, 
        pacman_coordinates[1] /180.0])
    inputs = torch.tensor(inputs, dtype=torch.float, device=device)
    return inputs

#Function for selecting a ghost action from the policy 
def select_ghost_action():
    inputs = get_inputs()
    outputs = ghost_policy_net(inputs)

    blinky_valid_actions = env.get_legal_moves(env.blinky)
    pinky_valid_actions = env.get_legal_moves(env.pinky)
    inky_valid_actions = env.get_legal_moves(env.inky)
    clyde_valid_actions = env.get_legal_moves(env.clyde)

    blinky_probs = torch.argsort(torch.softmax(outputs[0:4], dim=0), descending=True)  # Probabilities for Blinky's actions
    pinky_probs = torch.argsort(torch.softmax(outputs[4:8], dim=0), descending=True)   # Probabilities for Pinky's actions
    inky_probs = torch.argsort(torch.softmax(outputs[8:12], dim=0), descending=True)   # Probabilities for Inky's actions
    clyde_probs = torch.argsort(torch.softmax(outputs[12:16], dim=0), descending=True) # Probabilities for Clyde's actions

     # Get the predicted action (the index with the highest probability) for each ghost
    # Makes sure that the action chosen is legal 
    for action in blinky_probs:
        if action.item() in blinky_valid_actions:
            blinky_predicted_action = action.item()
            break
    for action in pinky_probs:
        if action.item() in pinky_valid_actions:
            pinky_predicted_action = action.item()
            break
    for action in inky_probs:
        if action.item() in inky_valid_actions:
            inky_predicted_action = action.item()
            break
    for action in clyde_probs:
        if action.item() in clyde_valid_actions:
            clyde_predicted_action = action.item()
            break

    return (blinky_predicted_action, pinky_predicted_action, inky_predicted_action, clyde_predicted_action)

observation, info = env.reset()
total_reward = 0
num_steps = 0
while True:
    num_steps += 1
    # Commented out choosing random actions. Instead will use actions from the ghost policy
    # blinky_action = env.ghost_action_space.sample()
    # pinky_action = env.ghost_action_space.sample()
    # inky_action = env.ghost_action_space.sample()
    # clyde_action = env.ghost_action_space.sample()
    actions = select_ghost_action()
    observation, reward, game_over = env.step(actions)
    total_reward += reward 
    if game_over:
        print(f"GAME OVER.   Total Reward: {total_reward}       Num Steps: {num_steps}")
        observation, info = env.reset()
        num_steps = 0
        total_reward = 0
        break


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
