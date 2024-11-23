# This run did decently well upon testing, but it doesn't work after the next life. 
BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 1000    
TAU = 0.005
LR = 1e-5
REPLAY_MEMORY_CAPACITY = 10000

num_episodes = 5000
# This decides how many episodes until running save_execution() 
save_rate = 100
