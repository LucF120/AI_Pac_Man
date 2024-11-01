import gymnasium as gym
import ale_py

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", render_mode="human")
obs, info = env.reset()

for _ in range(100):
    env.render()  # This will open a window to show the environment running
    action = env.action_space.sample()  # Choose a random action
    env.step(action)

env.close()