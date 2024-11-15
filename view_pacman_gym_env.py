import gymnasium as gym
import ale_py
import numpy as np 
import cv2

# cv2 was used with the assistance of Gen AI 
# This file allowed me to experiment with cropping the grayscale image.

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", obs_type="grayscale", render_mode="human")

observation, _ = env.reset()

# Show the initial observation
cv2.imshow("Full Observation", observation)

cropped_image = observation[20:200, 0:]
cv2.imshow("Cropped Image", cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(cropped_image.shape)