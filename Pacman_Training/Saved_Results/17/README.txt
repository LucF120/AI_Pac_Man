#Doing 1 life per episode 
# Waiting 140 frames at the beginning, and not optimizing for those frames 


BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 200000    
TAU = 0.005
LR = 1e-5
REPLAY_MEMORY_CAPACITY = 100000

num_episodes = 2700
# This decides how many episodes until running save_execution() 
save_rate = 100