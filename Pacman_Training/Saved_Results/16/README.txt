BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 0.995    
epsilon = EPS_START
TAU = 0.005
LR = 1e-5
REPLAY_MEMORY_CAPACITY = 10000

num_episodes = 5000
# This decides how many episodes until running save_execution() 
save_rate = 100



        # # Manually change the reward to -100 if pacman lost a life
        if info['lives'] < num_lives:
            end_episode = True
            reward = -500
            # Set the frame to wait until to 128 greater than now, since this is roughly how long it takes for pacman to respawn 
            # end_episode = True
        done = terminated or truncated

        if reward == 0:
            reward = -1

        if reward == 1:
            reward = 10
        
        if reward == 5:
            reward = 50

        if reward == 20:
            reward = 100
