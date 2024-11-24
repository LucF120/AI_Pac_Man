import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import ale_py

gym.register_envs(ale_py)

# This class is a custom gynasium environment for Pacman.
# This is the environment where we train the ghosts against a pre-trained pacman.
class PacmanEnv(gym.Env):
    def __init__(self):
        self.grid = (gym.make("ALE/Pacman-v5", obs_type="grayscale").reset()[0])[20:200, 0:]

        self.height, self.width = self.grid.shape
        
        self.ghost_action_space = gym.spaces.Discrete(4)  # 4 actions: up, right, left, down 
        self.pacman_action_space = gym.spaces.Discrete(5) # 5 actions: NOOP, up, right, left, down 

        # This stores the coordinates for all the pixels that belong to pacman. 
        # self.pacman must be updated in every move function 
        self.pacman = self.get_pacman_coordinates()

        # This stores the coordinates for all the pixels that belong to blinky 
        # Also stores whether or not blinky left spawn, since blinky needs to phase through the wall at the beginning 
        # self.blinky must be updated in every move function 
        self.blinky = {
            "coordinates": self.get_ghost_coordinates(),
            "left_spawn": False
            }
        
        # This stores pips that the ghost traveled over so they can be replaced later 
        self.pips_to_restore = []
        
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


    def _check_game_over(self):
        """Check if Pacman is caught by a ghost."""

        
    # This function is used to get blinky's position at the beginning of the game 
    # Note that it can only be used at the beginning since power pellets are the same color as blinky,
    # so this function can only look at the exact location of blinky's spawn 
    def get_ghost_coordinates(self):
        all_coordinates = np.column_stack(np.where(self.grid == 183))
        filtered_coordinates = all_coordinates[
            (all_coordinates[:, 0] >= 65) & (all_coordinates[:, 0] <= 100)
        ]
        return filtered_coordinates

    # This function is used to move blinky, by calling the move_ghost function
    def move_blinky(self, action):
        self.move_ghost(self.blinky, action)

    # This function is used to move a ghost up, down, left, or right
    # Also, an input of 0 does nothing. 
    # It takes in a ghost as input, since there are 4 different ghosts. 
    # Helper functions are move_ghost_left, move_ghost_right,
    # move_ghost_down, and move_ghost_up
    def move_ghost(self, ghost, action):
        # 0 = UP 
        if action == 0:
            for i in range(8):
                self.move_ghost_up(ghost)
        # 1 = Right 
        if action == 1:
            for i in range(8):
                self.move_ghost_right(ghost)
        # 2 = Left
        if action == 2:
            for i in range(8):
                self.move_ghost_left(ghost)
        # 3 = Down 
        if action == 3:
            for i in range(8):
                self.move_ghost_down(ghost)
        
        # Restore pips that the ghost deleted previously 
        for i in range(len(self.pips_to_restore) - 1, -1, -1): 
            coordinate = self.pips_to_restore.pop(i)
            if self.grid[(coordinate[0], coordinate[1])] != 183:
                self.grid[coordinate[0], coordinate[1]] = 192
            else:
                self.pips_to_restore.append(coordinate)
        self.render()

    def move_ghost_left(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[1]):
            # Checks if the ghost is colliding with a wall only if they haven't left spawn yet 
            if updated_grid[coordinate[0], coordinate[1] - 2] == 192:
                if not self.is_valid_pip_location(coordinate[1] - 2, coordinate[0]) and ghost["left_spawn"] == True:
                    return
                else:
                    pips_to_restore.append([coordinate[0], coordinate[1] - 2])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            if self.coord_in_spawn(coordinate[1], coordinate[0]):
                left_spawn = False
            # Checks if the ghost is inside of the spawn wall. If they are, then the coord is replaced with 
            # a wall color (192) instead of 64 
            if self.coord_in_spawn_wall(coordinate[1], coordinate[0]):
                if ghost["left_spawn"] == True:
                    return
                updated_grid[coordinate[0], coordinate[1]] = 192
            else:
                updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] - 2] = 183
            new_ghost_coordinates.append([coordinate[0], coordinate[1] - 2])
        # Update the grid after ghost moved left 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        # If the ghost left the spawn, set it to true
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()

    def move_ghost_right(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[1], reverse=True):
            if updated_grid[coordinate[0], coordinate[1] + 2] == 192:
                if not self.is_valid_pip_location(coordinate[1] + 2, coordinate[0]) and ghost["left_spawn"] == True:
                    return
                else:
                    pips_to_restore.append([coordinate[0], coordinate[1] + 2])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            if self.coord_in_spawn(coordinate[1], coordinate[0]):
                left_spawn = False
            if self.coord_in_spawn_wall(coordinate[1], coordinate[0]):
                if ghost["left_spawn"] == True:
                    return
                updated_grid[coordinate[0], coordinate[1]] = 192
            else:
                updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] + 2] = 183
            new_ghost_coordinates.append([coordinate[0], coordinate[1] + 2])
        # Update the grid after pacman moved right 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()

    def move_ghost_up(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[0]):
            if updated_grid[coordinate[0] - 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] - 2) and ghost["left_spawn"] == True:
                    print(f"UP FAIL: {coordinate[0]}, {coordinate[1]}")
                    return
                else:
                    pips_to_restore.append([coordinate[0] - 2, coordinate[1]])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            else:
                if self.coord_in_spawn(coordinate[1], coordinate[0]):
                    left_spawn = False
            if self.coord_in_spawn_wall(coordinate[1], coordinate[0]):
                if ghost["left_spawn"] == True:
                    return
                updated_grid[coordinate[0], coordinate[1]] = 192
            else:
                updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] - 2, coordinate[1]] = 183
            new_ghost_coordinates.append([coordinate[0] - 2, coordinate[1]])
        # Update the grid after pacman moved up 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()
    
    def move_ghost_down(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[0], reverse=True):
            if updated_grid[coordinate[0] + 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] + 2) and ghost["left_spawn"] == True:
                    # Return if the move is not legal 
                    return
                else:
                    pips_to_restore.append([coordinate[0] + 2, coordinate[1]])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            else:
                if self.coord_in_spawn(coordinate[1], coordinate[0]):
                    left_spawn = False
            if self.coord_in_spawn_wall(coordinate[1], coordinate[0]):
                if ghost["left_spawn"] == True:
                    return
                updated_grid[coordinate[0], coordinate[1]] = 192
            else:
                updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] + 2, coordinate[1]] = 183
            new_ghost_coordinates.append([coordinate[0] + 2, coordinate[1]])
        # Update the grid after pacman moved down 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()


    # Helper function used to check if the coordinate is in the spawn wall.
    # Used to make sure that the wall is redrawn properly if the ghost passes through 
    def coord_in_spawn_wall(self, x, y):
        if x >=72 and x <= 75 and y >= 65 and y <=92:
            return True
        elif x >= 84 and x <=87 and y >= 65 and y <= 92:
            return True
        elif x >=72 and x <= 87 and y >= 65 and y <= 70:
            return True
        elif x >=72 and x <= 87 and y >=87 and y <=92:
            return True
        else:
            return False 
        
    # This helper function simply returns true if the coordinate is within the spawn (either the wall or between the walls)
    def coord_in_spawn(self, x, y):
        return x >=72 and x <= 87 and y>=65 and y<=92 
    



    # This function is used in the init function to get pacman's initial coordinates. 
    # Afterwards, his coordinates are updated by the move functions. 
    def get_pacman_coordinates(self):
        return np.column_stack(np.where(self.grid == 223))
    
    # This function is used to move pacman up, down, left, or right. 
    # Also, an input of 0 does nothing. 
    # Helper functions are move_pacman_left, move_pacman_right,
    # move_pacman_down, and move_pacman_up
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
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[1]):
            if updated_grid[coordinate[0], coordinate[1] - 2] == 192:
                if not self.is_valid_pip_location(coordinate[1] - 2, coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] - 2] = 223
            new_pacman.append([coordinate[0], coordinate[1] - 2])
        # Update the grid after pacman moved left 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()

    def move_pacman_right(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[1], reverse=True):
            if updated_grid[coordinate[0], coordinate[1] + 2] == 192:
                if not self.is_valid_pip_location(coordinate[1] + 2, coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] + 2] = 223
            new_pacman.append([coordinate[0], coordinate[1] + 2])
        
        # Update the grid after pacman moved right 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()


    def move_pacman_up(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[0]):
            if updated_grid[coordinate[0] - 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] - 2):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] - 2, coordinate[1]] = 223
            new_pacman.append([coordinate[0] - 2, coordinate[1]])

        # Update the grid after pacman moved up 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()
    
    def move_pacman_down(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[0], reverse=True):
            if updated_grid[coordinate[0] + 2, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] + 2):
                    # Return if the move is not legal 
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] + 2, coordinate[1]] = 223
            new_pacman.append([coordinate[0] + 2, coordinate[1]])
        # Update the grid after pacman moved down 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()

    # This function is used to check to see if pacman is bumping into a wall or a pip
    # It is needed because pips and walls are the same color in the observation. 
    # The function checks if the pip in question is at the same y level as a pip. If it is, then 
    # pacman is allowed to collide with it. 
    # Pacman is still not able to phase through walls because pacman is taller than the pips, so 
    # if there is an actual wall, the top of pacman's head will trigger this function to return false. 
    def is_valid_pip_location(self, x, y):
        # Check if the coordinate is in the spawn wall in the center of the map 
        if self.coord_in_spawn_wall(x, y):
            return False
        # Check if hitting left or right wall 
        if x <= 3 or x >= 156:
            return False
        # Check if hitting top or bottom wall 
        if (y <= 4 or y >= 175) and (x <= 75 or x >= 84):
            return False

        # Check if hitting walls that are aligned with pips 
        if (x >=32 and x <=35) or (x >= 124 and x <= 127):
            if (y >= 34 and y <= 35):
                return False
            if (y >= 78 and y <= 79):
                return False
            if (y >=122 and y <= 123):
                return False
            if (y >= 166 and y <= 167):
                return False
        if (x >= 60 and x <= 63) or (x>=96 and x <=99):
            if (y >= 12 and y <= 13):
                return False
            if (y >= 56 and y <= 57):
                return False
            if (y >=100 and y <= 101):
                return False
            if (y >= 144 and y <= 145):
                return False

        # Check if y is aligned with pips (x has already been checked above) 
        if y >= 5 and y <= 20:
            return True
        elif y >= 27 and y <= 42:
            return True
        elif y >= 49 and y <= 64:
            return True
        elif y >= 71 and y <= 86:
            return True
        elif y >= 93 and y <= 108:
            return True
        elif y >= 115 and y <= 130:
            return True
        elif y >= 137 and y <= 152:
            return True
        elif y >= 159 and y <= 174:
            return True
        else:
            return False 