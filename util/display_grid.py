import gymnasium as gym
import cv2
import numpy as np 
import ale_py
import matplotlib.pyplot as plt

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", obs_type="grayscale")

observation, info = env.reset()

cv2.imshow('Starting Position', observation)
observation = observation[20:200, 0:]
cv2.imshow('Cropped Starting Position', observation)

for i in range(0, 114):
    observation2, reward, terminated, truncated, info = env.step(2)
    observation2 = observation2[20:200, 0:]
cv2.imshow('Move', observation2)

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()

from PIL import Image
image = Image.fromarray(observation)
image.save('starting_position.png')

image2 = Image.fromarray(observation2)
image.save('first_movement.png')

np.save('starting_position.npy', observation)
np.save('first_movement.npy', observation2)

np.savetxt('starting_position.txt', observation, fmt='%d')
np.savetxt('first_movement.txt', observation2, fmt='%d')


unique_values = np.unique(observation)

print(f"Unique pixel values: {unique_values}")



# Define a custom colormap for visualizing the grid
cmap = plt.cm.get_cmap('tab10', 7)  # 7 distinct colors for 7 different values

# Create a figure with a larger size (e.g., 12 inches by 10 inches)
plt.figure(figsize=(12, 10))

# Create the plot
plt.imshow(observation, cmap=cmap, interpolation='nearest')

# Optionally, add a colorbar to show the mapping of values to colors
plt.colorbar()

# Set the ticks to show every 5 units on both axes
plt.xticks(np.arange(0, observation.shape[1], 5))  # x-axis ticks from 0 to width with step 5
plt.yticks(np.arange(0, observation.shape[0], 5))  # y-axis ticks from 0 to height with step 5


# Show the grid
plt.title("Visualized Pacman Grid")
plt.show()

coordinates = np.column_stack(np.where(observation == 223))

print("Coordinates of target color:", coordinates)

