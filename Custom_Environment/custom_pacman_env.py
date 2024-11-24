import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import ale_py

gym.register_envs(ale_py)

class PacmanEnv(gym.Env):
    def __init__(self):
        self.grid = (gym.make("ALE/Pacman-v5", obs_type="grayscale").reset()[0])[20:200, 0:]

        self.height, self.width = self.grid.shape
        
        self.ghost_action_space = gym.spaces.Discrete(4)  # 4 actions: up, right, left, down 
        self.pacman_action_space = gym.spaces.Discrete(5) # 5 actions: NOOP, up, right, left, down 


        self.pacman_pos = None
        self.ghost_positions = []
        self.pill_positions = []
        self.power_pellet_positions = []
        self._init_entities()

    def _init_entities(self):
        """Init entities."""
    def reset(self):
        """Reset the environment."""
        self._init_entities() 
        return self.grid

    def step(self, action):
        """Apply an action and return the new state, reward, and done status."""

    def render(self):
        """Render the environment."""
        plt.imshow(self.grid, cmap="gray", interpolation="nearest")
        plt.draw()
        plt.pause(0.00001)  # Pause for 0.1 seconds to show the update
        plt.clf()  # Clear the figure for the next frame

    def _is_free(self, pos):
        """Check if a move is legal"""
    def _check_game_over(self):
        """Check if Pacman is caught by a ghost."""

    def get_pacman_coordinates(self):
        return np.column_stack(np.where(self.grid == 223))
    def move_pacman(self, action):
        # 0 = NOOP: Do nothing

        # 1 = UP 
        if action == 1:
            for i in range(4):
                self.move_pacman_up()
        # 2 = Right 
        if action == 2:
            for i in range(4):
                self.move_pacman_right()
        # 3 = Left
        if action == 3:
            for i in range(4):
                self.move_pacman_left()
        # 4 = Down 
        if action == 4:
            for i in range(4):
                self.move_pacman_down()

        
    def move_pacman_left(self):
        updated_grid = np.copy(self.grid)
        pacman_coordinates = self.get_pacman_coordinates()
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[1]):
            if updated_grid[coordinate[0], coordinate[1] - 2] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] - 2] = 223
        # Update the grid after pacman moved left 
        self.grid = updated_grid
        self.render()

    def move_pacman_right(self):
        updated_grid = np.copy(self.grid)
        pacman_coordinates = self.get_pacman_coordinates()
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[1], reverse=True):
            if updated_grid[coordinate[0], coordinate[1] + 2] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] + 2] = 223
        
        # Update the grid after pacman moved right 
        self.grid = updated_grid
        self.render()


    def move_pacman_up(self):
        updated_grid = np.copy(self.grid)
        pacman_coordinates = self.get_pacman_coordinates()
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[0]):
            if updated_grid[coordinate[0] - 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] - 2, coordinate[1]] = 223

        # Update the grid after pacman moved up 
        self.grid = updated_grid
        self.render()
    
    def move_pacman_down(self):
        updated_grid = np.copy(self.grid)
        pacman_coordinates = self.get_pacman_coordinates()
        for coordinate in sorted(pacman_coordinates, key=lambda x: x[0], reverse=True):
            if updated_grid[coordinate[0] + 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0]):
                    # Return if the move is not legal 
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] + 2, coordinate[1]] = 223
        # Update the grid after pacman moved down 
        self.grid = updated_grid
        self.render()

    def is_valid_pip_location(self, x, y):
        if y >= 11 and y <= 14:
            return True
        elif y >= 33 and y <= 36:
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