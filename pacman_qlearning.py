import gymnasium as gym
import ale_py
import random 
from tqdm import tqdm
import numpy as np 

import hashlib
import numpy as np

gym.register_envs(ale_py)

env = gym.make("ALE/Pacman-v5", obs_type="grayscale", mode=7)


def hashlib_hash(arr):
    # Convert the array to bytes
    arr_bytes = arr.tobytes()

    # Create a hash object
    hash_object = hashlib.sha256(arr_bytes)

    # Get the hexadecimal representation of the hash
    hex_dig = hash_object.hexdigest()
    return hex_dig


def calculate_qopt(Q_table, state, reward, gamma, previous_state, previous_action, num_updates_matrix):
    if state not in Q_table.keys():
        Q_table[state] = np.zeros(5)
    if state not in num_updates_matrix.keys():
        num_updates_matrix[state] = np.zeros(5)
    eta = 1 / (1 + num_updates_matrix[previous_state][previous_action])
    vopt = np.max(Q_table[state])
    Q_table[previous_state][previous_action] = (1 - eta) * Q_table[previous_state][previous_action] + (eta * (reward + (gamma * vopt)))
    num_updates_matrix[previous_state][previous_action] += 1
 
def Q_learning(num_episodes=10000, gamma=0.9, epsilon=1, decay_rate=0.999):
	"""
	Run Q-learning algorithm for a specified number of episodes.

    Parameters:
    - num_episodes (int): Number of episodes to run.
    - gamma (float): Discount factor.
    - epsilon (float): Exploration rate.
    - decay_rate (float): Rate at which epsilon decays. Epsilon is decayed as epsilon = epsilon * decay_rate after each episode.

    Returns:
    - Q_table (dict): Dictionary containing the Q-values for each state-action pair.
    """
	Q_table = {}
	'''

	YOUR CODE HERE


	'''
	num_updates_matrix = {}

	for i in tqdm(range(0, num_episodes)):
		obs, info = env.reset()
		previous_state = -1
		previous_action = -1
		while True:
			state = hashlib_hash(obs)
			if previous_state != -1:
				calculate_qopt(Q_table, state, reward, gamma, previous_state, previous_action, num_updates_matrix)
			if np.random.rand() < epsilon:
				action = np.random.randint(0, 4)
			else: 
				action = np.random.randint(0, 4)
			obs, reward, terminated, truncated, info = env.step(action)
			if terminated or truncated:
				previous_state = state
				state = hashlib_hash(obs)
				calculate_qopt(Q_table, state, reward, gamma, previous_state, action, num_updates_matrix)
				break
			previous_state = state
			previous_action = action 
		epsilon *= decay_rate
	return Q_table

decay_rate = 0.99999

Q_table = Q_learning(num_episodes=100, gamma=0.9, epsilon=1, decay_rate=decay_rate) # Run Q-learning

print(len(Q_table.keys()))
