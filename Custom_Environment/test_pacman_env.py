from custom_pacman_env import PacmanEnv 

# Create the Pacman environment
env = PacmanEnv()

# # Test environment
# env.render()

# #Test moving right
# for i in range(20):
#     env.move_pacman(2)



# #Test moving left
# for i in range(50):
#     env.move_pacman(3)



# # Test moving up
# for i in range(20):
#     env.move_pacman(1)


# # Test moving down
# for i in range(20):
#     env.move_pacman(4)


#Test random movements
for i in range(100):
    env.move_pacman(env.pacman_action_space.sample())