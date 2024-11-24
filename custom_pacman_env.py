import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import ale_py

gym.register_envs(ale_py)

# Define the Pacman environment
class PacmanEnv(gym.Env):
    def __init__(self):
        self.grid = (gym.make("ALE/Pacman-v5", obs_type="grayscale").reset()[0])[20:200, 0:]

        self.height, self.width = self.grid.shape
        
        # Define action space (e.g., up, down, left, right)
        self.action_space = gym.spaces.Discrete(5)  # 4 actions: up, down, left, right


        # Initial positions (these should be initialized based on your grid)
        self.pacman_pos = None
        self.ghost_positions = []
        self.pill_positions = []
        self.power_pellet_positions = []
        self._init_entities()

    def _init_entities(self):
        """Init entities."""
    def reset(self):
        """Reset the environment."""
        self._init_entities()  # Re-initialize the entities
        return self.grid

    def step(self, action):
        """Apply an action and return the new state, reward, and done status."""

    def render(self):
        """Render the environment."""
        plt.imshow(self.grid, cmap='gray', interpolation='nearest')
        plt.axis('off')  # Hide axis
        plt.show()

    def _is_free(self, pos):
        """Check if a move is legal"""
    def _check_game_over(self):
        """Check if Pacman is caught by a ghost."""

    def move_pacman_left(self):
        updated_grid = self.grid
        pacman_coordinates = np.column_stack(np.where(self.grid == 223))
        legal_move = True
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[1]):
            if updated_grid[coordinate[0], coordinate[1] + 1] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    legal_move = False
                    break
            self.grid[coordinate[0], coordinate[1]] = 64
            self.grid[coordinate[0], coordinate[1]-1] = 223
        if legal_move:
            self.grid = updated_grid

    def move_pacman_right(self):
        updated_grid = self.grid
        pacman_coordinates = np.column_stack(np.where(self.grid == 223))
        legal_move = True
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[1], reverse=True):
            if updated_grid[coordinate[0], coordinate[1] + 1] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    legal_move = False
                    break
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1]+1] = 223
        
        if legal_move:
            self.grid = updated_grid


    def move_pacman_up(self):
        pacman_coordinates = np.column_stack(np.where(self.grid == 223))
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[0]):
            self.grid[coordinate[0], coordinate[1]] = 64
            self.grid[coordinate[0]-1, coordinate[1]] = 223
    
    def move_pacman_down(self):
        pacman_coordinates = np.column_stack(np.where(self.grid == 223))
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[0], reverse=True):
            self.grid[coordinate[0], coordinate[1]] = 64
            self.grid[coordinate[0] + 1, coordinate[1]] = 223

    def is_valid_pip_location(self, x, y):
        if y >= 10 and y <= 15:
            return True
        elif y >= 32 and y <= 36:
            return True
        elif y >= 55 and y <= 58:
            return True
        elif y >= 77 and y <= 80:
            return True
        elif y >= 99 and y <= 102:
            return True
        elif y >= 121 and y <= 124:
            return True
        elif y >= 143 and y <= 146:
            return True
        elif y >= 165 and y <= 168:
            return True
        else:
            return False 
    
# Create the Pacman environment
env = PacmanEnv()

# Test environment
env.render()

#Test moving right
for i in range(30):
    env.move_pacman_right()
env.render()


#Test moving left
for i in range(30):
    env.move_pacman_left()
env.render()


# Test moving up
for i in range(30):
    env.move_pacman_up()
env.render()

# Test moving down
for i in range(30):
    env.move_pacman_down()
env.render()