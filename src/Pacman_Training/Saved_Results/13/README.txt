BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 20000    
TAU = 0.01
LR = 5e-4
REPLAY_MEMORY_CAPACITY = 10000

num_episodes = 5000
# This decides how many episodes until running save_execution() 
save_rate = 100