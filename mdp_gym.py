import numpy as np
import gym
from gym import spaces
import pacman
import random

class PacmanGameEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(PacmanGameEnv, self).__init__()
        # Again, this position is very very wrong. but will change once the grid is  set up. 
        self.pacman = {'lives': 3, 'position': (0, 0)}
        self.remaining_pellets = 244 # Also not sure if this is needed, might cause too many states.
        self.ghosts = {
            # States can either be alive or dead
            # If the ghost is alive, they should continue moving from where they are
            # If they are state dead they should be returned to start. (might need to add a delay on this to mirror actual pacman game)
            
            # Setting the positions to 0,0, but this is wrong.. will need to change this to the center pos
            # once the grid is fully set up . 
            'Blinky': {'name': 'Blinky', 'state': 'alive', 'position': (0, 0)}, 
            'Pinky': {'name': 'Pinky','state': 'alive', 'position': (0, 0)},
            'Inky': {'name': 'Inky', 'state': 'alive', 'position': (0, 0)},
            'Clyde': {'name': 'Clyde', 'state': 'alive', 'position': (0, 0)}
        }
        self.play_grid = [[""]
                          ]
        self.health_states =['Alive', 'Dead']

        self.rewards = {
            # needs one for pacman in normal form (combat win)
            # one for pacman in powered up form (combat loss)
            'Defeat': -10000, # one for when pacman gets all of the pellets (game loss [largest point loss])
            'Victory': 10000# one for when pacman loses all of his lifes (game win [largest point gain])
        }
        
        # load pacman env and define the maze grid


        #action space
        self.actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.action_space = spaces.Discrete(4)

        #observation space
        self.observation_shape = ()
        self.observation_space = spaces.Box(low=0, high=255, shape = self.observation_shape)

    # def create_ghost_model(self):
    
    def reset(self):
        state = self.pacman.reset()
        for ghost_name, ghost_data in self.ghosts.items():
            ghost_data['position'] = (random.randint(1, self.observation_shape[0] -1),
                                      random.randint(1, self.observation_shape[1] - 1))
            ghost_data['state'] = 'alive'
        return self._process_observation(state)
      
    def render(self, mode='human'):
        print(f"Current state: {self.current_state}")

    def is_terminal(self): 
        if self.pacman_lives <= 0:
            return 'Victory'
        if self.remaining_pellets == 0:
            return 'Defeat'
        return False

    # Moves pacman based on the given action, 
    def move_pacman(self, action):
        x, y = self.pacman['position']
        directions = {
            'UP': (x-1, y), 
            'DOWN': (x+1, y),
            'LEFT': (x, y-1),
            'RIGHT': (x, y+1)
        }
        # creates a new position based on action if valid action, or returns curr pos
        new_position = directions.get(action, self.pacman['position'])
        
        # This grid should be a state for the game as a whole, so that all 'players' can access it 
        grid = [[]]
        if grid[new_position[0]][new_position[1]] != 'X':
            self.pacman['position'] = new_position
            return f"Moved to {self.pacman['position']}", 0
        else:
            return "Out of bounds!", 0


    def move_ghosts(self, actions):
        grid = [[]]
        if len(actions) < 4:
            return None
        index = 0
        output = ""
        for ghost in self.ghosts:
            x, y = ghost['position']
            directions = {
                'UP': (x-1, y), 
                'DOWN': (x+1, y),
                'LEFT': (x, y-1),
                'RIGHT': (x, y+1)
            }
            new_position = directions.get(actions[index], ghost['position'])
            if grid[new_position[0]][new_position[1]] != 'X':
                ghost['position'] = new_position
                # im going to just append the result to a string and then return that at the end. 
    
    def get_observation(self):
        obs = {
            'pacman_position': self.current_state['pacman_position'],
            'remaining_pellets': self.remaining_pellets,
            'ghosts': {},
            "grid": np.zeros(self.observation_shape, dtype=np.int8)
        }
        x, y = self.pacman['position']
        obs['grid'][x,y] = 1

        ghost_id = 2
        for ghost_name, ghost_data in self.ghosts.items():
            gx, gy = ghost_data['position']
            if ghost_data['state'] == 'alive':
                obs['grid'][gx, gy] = ghost_id
            obs['ghosts'][ghost_name] = {
                "position": ghost_data['position'],
                "state": ghost_data['state']
            }
            ghost_id += 1
            
        return obs
    
    def calculate_reward(self, done):
        if done == 'Victory':
            return self.rewards['Victory']
        elif done == 'Defeat':
            return self.rewards['Victory']
        return 0

    def step(self, action):
        action_name = self.actions[action]
        action_map = {0: 'UP', 1: 'DOWN', 2:'LEFT', 3:'RIGHT'}
        result, reward = self.pacman.step(action_map[action])
    
        done = False
        terminal_state = self.is_terminal()
        if terminal_state == 'Victory':
            done = True
            result += f"Ghosts defeat pacman"
        if terminal_state == 'Defeat':
            done = True
            result += f"Pacman wins"

        observation = self.get_observation()
        info = {'result': result, 'action': action_name}
            
        return observation, reward, done, info
        
    def close(self):
        self.pacman_env.close()
