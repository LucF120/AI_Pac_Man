import gymnasium as gym
import numpy as np
import random
import matplotlib.pyplot as plt
import ale_py
import torch 
import sys
import os 
sys.path.append(os.path.abspath("../Pacman_Training"))

from Pacman_reload_dqn import load_execution
from pacman_neural_network import DQN

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)

gym.register_envs(ale_py)

# This class is a custom gynasium environment for Pacman.
# This is the environment where we train the ghosts against a pre-trained pacman.
class PacmanEnv(gym.Env):
    def __init__(self, render_mode=None):
        self.render_mode = render_mode
        self.grid = (gym.make("ALE/Pacman-v5", obs_type="grayscale").reset()[0])[20:200, 0:]

        self.width = 160
        self.height = 180
        
        self.ghost_action_space = gym.spaces.Discrete(4)  # 4 actions: up, right, left, down 
        self.pacman_action_space = gym.spaces.Discrete(5) # 5 actions: NOOP, up, right, left, down 

        # This stores the coordinates for all the pixels that belong to pacman. 
        # self.pacman must be updated in every move function 
        self.pacman = self.get_pacman_coordinates()

        # This stores the policy pacman uses to choose actions
        self.pacman_policy_net = self.load_pacman_policy()


        # This stores the coordinates for all the pixels that belong to blinky 
        # Also stores whether or not blinky left spawn, since blinky needs to phase through the wall at the beginning 
        # self.blinky must be updated in every move function 
        self.blinky = {
            "name": "blinky",
            "coordinates": self.get_ghost_coordinates(),
            "left_spawn": False
            }
        self.pinky = {
            "name": "pinky",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False
            }
        self.inky = {
            "name": "inky",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False  
            }
        self.clyde = {
            "name": "clyde",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False
            }
        
        # This keeps track of the number of ghost movements made. 
        # After 100 movements, pinky spawns
        # After 200 movements, inky spawns
        # After 300 movements, clyde spawns
        self.spawn_counter = 0
        
        # Tracks whether or not a ghost caught pacman 
        self.game_over = False
        # This stores pips that the ghost traveled over so they can be replaced later 
        self.pips_to_restore = []

    def reset(self):
        """Reset the environment."""
        self.grid = (gym.make("ALE/Pacman-v5", obs_type="grayscale").reset()[0])[20:200, 0:]
        self.pips_to_restore = []
        self.game_over = False
        self.blinky = {
            "name": "blinky",
            "coordinates": self.get_ghost_coordinates(),
            "left_spawn": False
        }
        self.pinky = {
            "name": "pinky",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False
            }
        self.inky = {
            "name": "inky",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False  
            }
        self.clyde = {
            "name": "clyde",
            "coordinates": None,
            "left_spawn": False,
            "spawned": False
            }
        self.pacman = self.get_pacman_coordinates()
        
        # Stores the number of lives left for pacman. Still need to configure this. 
        self.info = []
        return [self.grid, self.info]

    def step(self, action):
        """Apply an action and return the new state, reward, and done status."""
        # Taking random pacman action for now. Will incorporate the neural network policy soon. 
        pacman_action = self.select_pacman_action()
        self.move_pacman(pacman_action)
        reward = self.move_blinky(action)
        return [self.grid, reward, self.game_over]

    def render(self):
        """Render the environment."""
        # Only render the environment if render_mode is set 
        if self.render_mode == "human":
            plt.imshow(self.grid, cmap="gray", interpolation="nearest")
            plt.draw()
            plt.pause(0.00001)  # Pause for 0.1 seconds to show the update
            plt.clf()  # Clear the figure for the next frame
        
    def select_pacman_action(self):
        state = torch.tensor(self.grid, device=device, dtype=torch.float32).unsqueeze(0) / 255.0
        state = state.unsqueeze(1)
        return self.pacman_policy_net(state).max(1).indices.view(1, 1)

    # Loads the pacman policy. The policy_net.pth file should be in the same directory as this file. 
    def load_pacman_policy(self):
        n_actions = self.pacman_action_space.n
        pacman_policy_net = DQN(n_actions).to(device)
        load_execution(pacman_policy_net, only_policy_net=True, dirpath="")
        return pacman_policy_net

    # This function duplicates the last ghost, and assigns it to a ghost that hasn't spawned 
    def duplicate_ghost(self, old_ghost):
        coordinates = np.copy(old_ghost["coordinates"])

        if old_ghost["name"] == "blinky":
            self.pinky["coordinates"] = coordinates

        if old_ghost["name"] == "pinky":
            self.inky["coordinates"] = coordinates

        if old_ghost["name"] == "inky":
            self.clyde["coordinates"] = coordinates
            
        for coordinate in coordinates:
            self.grid[coordinate[0], coordinate[1]] = 183


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
        return self.move_ghost(self.blinky, action)

    # This function is used to move a ghost up, down, left, or right
    # It takes in a ghost as input, since there are 4 different ghosts. 
    # Helper functions are move_ghost_left, move_ghost_right,
    # move_ghost_down, and move_ghost_up
    # The way ghost movement works in each helper function:
    # - Make a copy of the grid
    # - Track whether or not the ghost left the spawn 
    # - Track pips/wall pixels that need to be restored after the ghost collides with them
    # - If ghost left spawn and collides with illegal wall, return
    # - If ghost didn't leave spawn and collided with a wall/pip, add it to pips_to_restore
    # - If the coordinate is still in the spawn, set left_spawn to false. This way, the ghost only leaves spawn if every single pixel is outside of spawn.
    # - Update the previous pixel to black (this can be changed to wall/pellet color in move if the pixel is in pips_to_restore)
    # - Update the pixel 2 to the left/right/up/down to the color of the ghost 
    # - Update the grid 
    # - Set ghost["left_spawn"] if it was determined that all pixels were outside of the spawn
    # - Add the pips that need to be restored to self.pips_to_restore (which will be used in move_ghost()
    # - Renders the grid 
    def move_ghost(self, ghost, action):
        # 0 = UP 
        if action == 0:
            for i in range(10):
                if self.game_over:
                    break
                self.move_ghost_up(ghost)
        # 1 = Right 
        if action == 1:
            for i in range(6):
                if self.game_over:
                    break
                self.move_ghost_right(ghost)
        # 2 = Left
        if action == 2:
            for i in range(6):
                if self.game_over:
                    break
                self.move_ghost_left(ghost)
        # 3 = Down 
        if action == 3:
            for i in range(10):
                if self.game_over:
                    break
                self.move_ghost_down(ghost)
        
        # Restore pips that the ghost deleted previously 
        for i in range(len(self.pips_to_restore) - 1, -1, -1): 
            coordinate = self.pips_to_restore.pop(i)
            if self.grid[(coordinate[0], coordinate[1])] != 183:
                self.grid[coordinate[0], coordinate[1]] = 192
            else:
                self.pips_to_restore.append(coordinate)
        
        # Increment the spawn counter
        self.spawn_counter += 1

        # Determine if ghosts should be spawned in
        # If they should, duplicate the last ghost. 

        if self.spawn_counter > 20 and not self.pinky["spawned"]:
            self.duplicate_ghost(self.blinky)
            self.pinky["spawned"] = True
        if self.spawn_counter > 30 and not self.inky["spawned"]:
            self.duplicate_ghost(self.pinky)
            self.inky["spawned"] = True
        if self.spawn_counter > 40 and not self.clyde["spawned"]:
            self.duplicate_ghost(self.inky)
            self.clyde["spawned"] = True

        self.render()

        # Return a reward of 10 if the ghost caught pacman, and -1 otherwise 
        if self.game_over:
            return 10
        else:
            return -0.01
        
    # Helper function for move_ghost 
    def move_ghost_left(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[1]):
            # Check if attempted movement is out of bounds
            if coordinate[1] -1 <= 0:
                return
            # Checks if the ghost caught pacman
            if updated_grid[coordinate[0], coordinate[1] - 1] == 223:
                self.game_over = True
            # Checks if the ghost is colliding with a wall only if they haven't left spawn yet 
            if updated_grid[coordinate[0], coordinate[1] - 1] == 192:
                if not self.is_valid_pip_location(coordinate[1] - 1, coordinate[0]) and ghost["left_spawn"] == True:
                    return
                # If the ghost collided with a pixel that is the same color as a wall/pellet legally, add it to pips_to_restore
                # to fix the grid after the ghost is finished moving 
                else:
                    pips_to_restore.append([coordinate[0], coordinate[1] - 1])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            if self.coord_in_spawn(coordinate[1], coordinate[0]):
                left_spawn = False
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] - 1] = 183
            new_ghost_coordinates.append([coordinate[0], coordinate[1] - 1])
        # Update the grid after ghost moved left 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        # If the ghost left the spawn, set it to true
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()

    # Helper function for move_ghost 
    def move_ghost_right(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[1], reverse=True):
            # Check if attempted movement is out of bounds
            if coordinate[1] + 1 >= self.width:
                return
            # Checks if the ghost caught pacman
            if updated_grid[coordinate[0], coordinate[1] + 1] == 223:
                self.game_over = True

            if updated_grid[coordinate[0], coordinate[1] + 1] == 192:
                if not self.is_valid_pip_location(coordinate[1] + 1, coordinate[0]) and ghost["left_spawn"] == True:
                    return
                else:
                    pips_to_restore.append([coordinate[0], coordinate[1] + 1])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            if self.coord_in_spawn(coordinate[1], coordinate[0]):
                left_spawn = False
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] + 1] = 183
            new_ghost_coordinates.append([coordinate[0], coordinate[1] + 1])
        # Update the grid after pacman moved right 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()

    # Helper function for move_ghost 
    def move_ghost_up(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[0]):
            # Check if attempted movement is out of bounds
            if coordinate[0] - 1 <= 0:
                return
            # Checks if the ghost caught pacman
            if updated_grid[coordinate[0] - 1, coordinate[1]] == 223:
                self.game_over = True

            if updated_grid[coordinate[0] - 1, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] - 1) and ghost["left_spawn"] == True:
                    return
                else:
                    pips_to_restore.append([coordinate[0] - 1, coordinate[1]])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            else:
                if self.coord_in_spawn(coordinate[1], coordinate[0]):
                    left_spawn = False
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] - 1, coordinate[1]] = 183
            new_ghost_coordinates.append([coordinate[0] - 1, coordinate[1]])
        # Update the grid after pacman moved up 
        self.grid = updated_grid
        ghost["coordinates"] = new_ghost_coordinates
        if left_spawn:
            ghost["left_spawn"] = True
        self.pips_to_restore.extend(pips_to_restore)
        self.render()
    
    # Helper function for move_ghost 
    def move_ghost_down(self, ghost):
        updated_grid = np.copy(self.grid)
        new_ghost_coordinates = []
        left_spawn = True
        pips_to_restore = []
        for coordinate in sorted(ghost["coordinates"], key=lambda x: x[0], reverse=True):
            # Check if attempted movement is out of bounds
            if coordinate[0] + 1 >= self.height:
                return
            # Checks if the ghost caught pacman
            if updated_grid[coordinate[0] + 1, coordinate[1]] == 223:
                self.game_over = True

            if updated_grid[coordinate[0] + 1, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] + 1) and ghost["left_spawn"] == True:
                    # Return if the move is not legal 
                    return
                else:
                    pips_to_restore.append([coordinate[0] + 1, coordinate[1]])
            # Checks if the coordinate is in the spawn. If it is, it sets left_spawn to false. 
            else:
                if self.coord_in_spawn(coordinate[1], coordinate[0]):
                    left_spawn = False
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] + 1, coordinate[1]] = 183
            new_ghost_coordinates.append([coordinate[0] + 1, coordinate[1]])
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
    # The way move_pacman works in each helper function:
    # - Make a copy of the grid 
    # - Keep track of pacman's new coordinates 
    # - If pacman bumps into a wall/pellet-colored pixel, check if the pixel is a pellet or not
        # - If it is a wall, return, and don't update the grid 
    # - Turn the pixel pacman just left black
    # - Turn the pixel pacman reaches to the same color as pacman
    # - Update the grid
    # - Update pacman's coordinates
    # - Render the board 
    def move_pacman(self, action):
        # 0 = NOOP: Do nothing
        if action == 0:
            return
        # 1 = UP 
        if action == 1:
            for i in range(10):
                if self.game_over:
                    break
                self.move_pacman_up()
        # 2 = Right 
        if action == 2:
            for i in range(6):
                if self.game_over:
                    break
                self.move_pacman_right()
        # 3 = Left
        if action == 3:
            for i in range(6):
                if self.game_over:
                    break
                self.move_pacman_left()
        # 4 = Down 
        if action == 4:
            for i in range(10):
                if self.game_over:
                    break
                self.move_pacman_down()
        
    def move_pacman_left(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[1]):
            # Check if attempted movement is out of bounds
            if coordinate[1] -1 <= 0:
                return
            if updated_grid[coordinate[0], coordinate[1] - 1] == 192:
                if not self.is_valid_pip_location(coordinate[1] - 1, coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] - 1] = 223
            new_pacman.append([coordinate[0], coordinate[1] - 1])
        # Update the grid after pacman moved left 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()

    def move_pacman_right(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[1], reverse=True):
            # Check if attempted movement is out of bounds
            if coordinate[1] + 1 >= self.width:
                return
            if updated_grid[coordinate[0], coordinate[1] + 1] == 192:
                if not self.is_valid_pip_location(coordinate[1] + 1, coordinate[0]):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0], coordinate[1] + 1] = 223
            new_pacman.append([coordinate[0], coordinate[1] + 1])
        
        # Update the grid after pacman moved right 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()


    def move_pacman_up(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[0]):
            # Check if attempted movement is out of bounds
            if coordinate[0] - 1 <= 0:
                return
            if updated_grid[coordinate[0] - 1, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] - 1):
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] - 1, coordinate[1]] = 223
            new_pacman.append([coordinate[0] - 1, coordinate[1]])

        # Update the grid after pacman moved up 
        self.grid = updated_grid
        self.pacman = np.array(new_pacman)
        self.render()
    
    def move_pacman_down(self):
        updated_grid = np.copy(self.grid)
        new_pacman = []
        for coordinate in sorted(self.pacman, key=lambda x: x[0], reverse=True):
            # Check if attempted movement is out of bounds
            if coordinate[0] + 1 >= self.height:
                return
            if updated_grid[coordinate[0] + 1, coordinate[1]] == 192:
                if not self.is_valid_pip_location(coordinate[1], coordinate[0] + 1):
                    # Return if the move is not legal 
                    return
            updated_grid[coordinate[0], coordinate[1]] = 64
            updated_grid[coordinate[0] + 1, coordinate[1]] = 223
            new_pacman.append([coordinate[0] + 1, coordinate[1]])
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

        # Check if y is aligned with pips (x has already been checked above) 
        if (y >= 6 and y <= 20) and not (x >= 60 and x <= 63) and not (x>=96 and x <=99):
            return True
        elif (y >= 27 and y <= 42) and not (x >=32 and x <=35) and not (x >= 124 and x <= 127):
            return True
        elif (y >= 49 and y <= 64) and not (x >= 60 and x <= 63) and not (x>=96 and x <=99):
            return True
        elif (y >= 71 and y <= 86) and not (x >=32 and x <=35) and not (x >= 124 and x <= 127):
            return True
        elif (y >= 93 and y <= 108) and not (x >= 60 and x <= 63) and not (x>=96 and x <=99):
            return True
        elif (y >= 115 and y <= 130) and not (x >=32 and x <=35) and not (x >= 124 and x <= 127):
            return True
        elif (y >= 137 and y <= 152) and not (x >= 60 and x <= 63) and not (x>=96 and x <=99):
            return True
        elif (y >= 159 and y <= 174) and not (x >=32 and x <=35) and not (x >= 124 and x <= 127):
            return True
        else:
            return False 