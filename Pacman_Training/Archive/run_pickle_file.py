import numpy as np;
import gymnasium as gym
import ale_py
import hashlib

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", render_mode="human", obs_type="grayscale", mode=7)

def hashlib_hash(arr):
    # Convert the array to bytes
    arr_bytes = arr.tobytes()

    # Create a hash object
    hash_object = hashlib.sha256(arr_bytes)

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig


Q_table = np.load('Q_table.pickle', allow_pickle=True)
obs, info = env.reset()
total_reward = 0
terminated = False
while not terminated:
    state = hashlib_hash(obs)
    if(state not in Q_table.keys()):
        action = np.random.randint(0, 4)
    else:
        action = np.argmax(Q_table[state])
    obs, reward, terminated, truncated, info = env.step(action)
    total_reward += reward

print("Total reward:", total_reward)

# Close the
env.close() # Close the environment