from ghosts_ffn import GhostFNN
import torch
import torch.nn as nn
import torch.optim as optim
import sys
import os 
import numpy as np

sys.path.append(os.path.abspath("../Pacman_Training"))

from Pacman_reload_dqn import load_execution
from pacman_neural_network import DQN
from custom_pacman_env import PacmanEnv 


ghost_nn = GhostFNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(ghost_nn.parameters(), lr=0.01)

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

# Create the Pacman environment
env = PacmanEnv(render_mode="human")

# Training loop
total_rewards = []
for i_episode in range(1000):
    observation, info = env.reset() 
    total_reward = 0
    step_count = 0
    while True:
        step_count += 1
        blinky_coordinates = env.blinky["coordinates"][0]
        pacman_coordinates = env.pacman[0]
        inputs = np.array([blinky_coordinates[0], blinky_coordinates[1], pacman_coordinates[0], pacman_coordinates[1]])
        inputs = torch.tensor(inputs, dtype=torch.float)

        # Got help from GenAI to figure out how to pass in the target action 
        distances = []
        actions = [
        (blinky_coordinates[0] - 1, blinky_coordinates[1]),  # Move up
        (blinky_coordinates[0] + 1, blinky_coordinates[1]),  # Move down
        (blinky_coordinates[0], blinky_coordinates[1] - 1),  # Move left
        (blinky_coordinates[0], blinky_coordinates[1] + 1),  # Move right
        ]

        for action in actions:
            dist = abs(action[0] - pacman_coordinates[0]) + abs(action[1] - pacman_coordinates[1])
            distances.append(dist)
            
        target_action = distances.index(min(distances))
        target = torch.tensor([target_action], dtype=torch.long)

        # Forward pass
        outputs = ghost_nn(inputs)
        loss = criterion(outputs.unsqueeze(0), target)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        predicted_action = torch.argmax(outputs).item()
        actions = (predicted_action, 0, 0, 0)
        observation, reward, game_over = env.step(actions)
        total_reward += reward 
        if game_over:
            break
        if step_count % 100 == 0:
            print(f"Step count: {step_count}")

    print(f"Episode {i_episode}, Loss: {loss.item()},   Total Reward: {total_reward}")
    total_rewards.append(total_reward)

print("Training complete!")

