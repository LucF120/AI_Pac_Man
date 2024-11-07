import gymnasium as gym
import ale_py
import random 
from tqdm import tqdm

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", render_mode="human", obs_type="grayscale")

reward_list = []

for i in tqdm(range(10000)):
    observation, info = env.reset()
    total_rewards = 0
    while True:
        # Pick an action using the random Python module random until we have a valid action for that cell
        # Hint: use states_actions_map in conjunction with the random module
        random_action = random.randint(0, 4)
        
        # Get a new observation, reward, terminated and other information here using the env.step() function
        new_obs, reward, terminated, truncated, info = env.step(random_action)
        observation = new_obs
        # Update rewards
        total_rewards = total_rewards + reward

        # break this loop if we have reached an end state
        if terminated or truncated:
            obs, info = env.reset()
            break
    reward_list.append(total_rewards)
    print(total_rewards)
# calculate and print the average reward here
avg_reward = sum(reward_list) / len(reward_list)
print("Average reward obtained: ", avg_reward)