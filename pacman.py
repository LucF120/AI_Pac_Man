import gymnasium as gym
import ale_py
import numpy as np
from tqdm import tqdm
import hashlib
import random

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", render_mode="human", obs_type="grayscale")
obs, info = env.reset()
terminated = False
reward_array = []

unique_nums = []
def hash(obs):
    # Convert the observation array to bytes
    obs_bytes = obs.tobytes()

    # Hash the bytes using SHA-256
    obs_hash = hashlib.sha256(obs_bytes).hexdigest()

    return obs_hash



def Q_learning(num_episodes=10, gamma=0.9, epsilon=1, decay_rate=0.999):
    q_table = {}
    q_table_updates = {}

    for i in tqdm(range(num_episodes)):

        temp_reward = 0
        obs, info = env.reset()
        hashed_obs = hash(obs)

        while info['lives'] == 4:
            # env.render()  # This will open a window to show the environment running
            if hashed_obs not in q_table.keys():
                q_table[hashed_obs] = np.zeros(5)
                q_table_updates[hashed_obs] = np.zeros(5)


            possible_actions = q_table[hashed_obs]
            rand_int = random.uniform(0, 1)

            if rand_int <= epsilon:
                action = np.random.choice(len(possible_actions))
            else:
                action = np.argmax(possible_actions)


            new_obs, reward, terminated, truncated, info = env.step(action)
            hashed_new_state = hash(new_obs)
            if hashed_new_state not in q_table.keys():
                q_table[hashed_new_state] = np.zeros(5)
                q_table_updates[hashed_new_state] = np.zeros(5)

            eta = 1 / (1 + q_table_updates[hashed_obs][action])
            prev_q_opt = q_table[hashed_obs][action]
            action_reward = reward
            decayed_v_opt = gamma * np.max(q_table[hashed_new_state])

            q_table[hashed_obs][action] = (1 - eta) * prev_q_opt + eta * (action_reward + decayed_v_opt)
            q_table_updates[hashed_obs][action] += 1

            hashed_obs = hashed_new_state

        epsilon = epsilon * decay_rate

    #print(len(q_table.keys()))
    #print(q_table)
    #print("Average Reward:", average_reward)
    return q_table


def generate_q_table():
    decay_rate = 0.99999

    # 1000000
    Q_table = Q_learning(num_episodes=2000, gamma=0.9, epsilon=1, decay_rate=decay_rate)  # Run Q-learning

    with open('output.txt', 'w') as file:
        for key, values in Q_table.items():
            # Convert the list of values to a string and join them with commas
            values_str = ', '.join(map(str, values))
            # Write the key and values to the file
            file.write(f"{key}: {values_str}\n")

def play_with_q_table():
    q_table = {}
    with open('output.txt', 'r') as file:
        for line in file:
            # Remove the trailing newline character
            line = line.strip()

            # Split the line at the first colon to separate the key and values part
            key, values_str = line.split(':', 1)

            # Split the values part by commas and convert to a list of integers (or whatever type is needed)
            values = np.array(list(map(float, values_str.split(', '))))

            # Add the key and values to the dictionary
            q_table[key] = values

    obs, info = env.reset()
    hashed_obs = hash(obs)
    while info['lives'] == 4:
        if hashed_obs not in q_table:
            action = random.randint(0, 4)
            print("Obs not included")
        else:
            action = np.argmax(q_table[hashed_obs])
        new_obs, reward, terminated, truncated, info = env.step(action)

        hashed_obs = hash(new_obs)

if __name__ == '__main__':
    #generate_q_table()
    play_with_q_table()

env.close()
