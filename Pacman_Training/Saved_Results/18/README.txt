# This was the first run where inputs were normalized (-1 for pacman dying, 0 for not collecting a pellet, and 1 for collecting pellets, powerpellets, and eating ghosts)
# This run did extremely well.

# For a future run, I think that adding a respawn timer would be beneficial.
# Also, decreasing the wait time for pacman spawning to 114 frames will likely improve results, since I had the wait time set too long

BATCH_SIZE = 64
GAMMA = 0.99
EPS_START = 1
EPS_END = 0.01
EPS_DECAY = 40000    
TAU = 0.005
LR = 1e-5
REPLAY_MEMORY_CAPACITY = 10000

