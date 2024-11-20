# Reinforcement Learning in Pac-Man
Allen Xu, Iba Baig, Luc Ferrara, Vishy Kamalapuram

### Project Overview
In this project, we aim to build an enhanced version of the Pac-Man game that combines reinforcement learning and neural networks to create a dynamic environment. The game will feature intelligent ghost agents that strategically target the Pac-Man player by utilizing deep reinforcement learning. This version of the game will allow for creative solutions combined with probabilistic inference, hopefully giving the agent and ghosts a fair chance of winning. This project will explore various AI learning techniques and game mechanisms to display real time decision making.

### Features
- Pacman AI
   - In order to train the ghosts, Pacman must be trained first
   - Utilizes the Pacman ALE enviornment to train with deep RL
   - Grayscale pixel representation of the enviornment fed into neural network to train Pacman
   - Ghosts then train off of the Pacman with these specific neural network weights
- Ghost AI
   - Custom built enviornment for ghosts to initally train off of Pacman using reinforcement learning
   - Player can also control Pacman to go against the ghost AI
   - Ghost AI will adapt to player controls as well

### Document Overview
- Pacman_reload_dqn.py: Saves and loads a state in the RL process
- pacman.py: Initial RL implementation to train Pacman in the gym enviornment for 10,000 episodes
- pacman_dqn_implementation.py: DQN implementation of training Pacman
- pacman_neural_network.py: Defines the Deep Q Network with pytorch
- view_pacman_gym_env.py: Allows viewing of the enviornment

### Getting Started

##### Prerequisits
- Python 3.11.5
- numpy
- pytorch
- pickle

### 2	Related Work
Reinforcement learning has been done with Pac-Man for a few years now, however many implementations focus on improving the overall performance of Pac-Man. In our project, we aim to utilize reinforcement learning to improve the performance of the ghosts, while Pac-Man is controlled by a human.

One of the main focal points in using reinforcement learning in Pac-Man is the grid size limitation. In [Reinforcement Learning in Pac-Man 2017], the authors mention how Q-Learning becomes suboptimal in large grid layouts, and utilize Deep Q-Learning instead to extract only the important features. However, despite such implementations, they still found themselves limited by grid-size eventually. In our project, we aim to incorporate Alpha Beta Pruning in some way to further enhance the grid size capabilities and still continuously find the optimal solutions.

In [UC Berkeley CS188 Intro to AI], it is written how the game of Pac-Man was part of the course materials for a foundations course. The course overview outlines various topics that were taught using Pac-Man, such as informed search, probabilistic inference, and reinforcement learning. Some of the search algorithms employed for navigating were breadth-first, depth-first, uniform-cost, and A* search. In addition, multiagent minimax and expectimax algorithms were used as adversarial search algorithms. 

In [Contreras, 2021], the author discusses how a neural network and a Q-Learning algorithm were used to train Ms. Pac-man. Contreras explains how the algorithm is used to predict the expected outcome of taking each action with the current input. Despite the DQN-Agent being trained using this algorithm for 3 hours, Ms. Pac-man was among the lowest performers when compared to other Atari games that were also trained with a DQN.


### 3	Proposed Methods
In this project, we aim to use reinforcement learning to enhance the behavior of the ghost agents in Pac-Man, with the goal of making them better at defeating the player. As noted before, reinforcement learning in the context of Pac-Man has focused on improving Pac-Man’s performance, allowing it to collect more points. However we propose to use the DQN model that is suggested in the Contreras article, in which it will take multiple states of the game as an input, and produce an action as an output. This approach is designed to train the ghost agents to make more effective decisions, leading to a more difficult game of Pac-Man.

One of the main challenges of using reinforcement learning in Pac-Man is managing large grid sizes, particularly in complex environments. Previous works like [Reinforcement Learning in Pac-Man 2017] highlighted how DQL managed to improve the optimality of larger sized grids, enhancing the overall optimality of reinforcement learning outcomes. Building upon that research, we hypothesize that integrating Alpha Beta Pruning into this process can further enhance efficiency and scalability. Alpha Beta Pruning, which demonstrated its success at reducing complex game outcomes in areas such as chess, could also provide those same benefits to Pac-Man. By implementing this technique, we aim to explore its potential for improving the performance of reinforcement learning models, ultimately advancing grid size optimization in the Pac-Man environment.


### 4	Timeline
We expect to have a maze generation system implemented within 2 weeks along with a player within the environment with movement capabilities. We expect the game mechanics to take around 2-3 weeks to be ready (ghosts with random movement), and the remaining time will be allocated to improving the enemy ghost AI. Depending on how much time we have left, we will implement more improvements or further polish.







### References

Contreras, Jose Alberto Leyva. “How to Train MS-Pac-Man with Reinforcement Learning.” 
Medium, Analytics Vidhya, 27 May 2021, medium.com/analytics-vidhya/how-to-train-ms-pacman-with-reinforcement-learning-dea714a2365e. 

Ghosh, A., Kale, S., and McAfee, P. (2011). Who moderates the moderators?: crowdsourcing 
abuse detection in user-generated content. In Proceedings of the 12th ACM conference on Electronic commerce, pages 167–176. ACM. Retrieved from https://cs229.stanford.edu/proj2017/final-reports/5241109.pdf

Gnanasekaran, Abeynaya, Jordi Feliu Faba, and Jing An. (2024) Reinforcement Learning in 
Pacman. Stanford University, Retrieved from 
https://cs229.stanford.edu/proj2017/final-reports/5241109.pdf 

NVIDIA. (2020). GameGAN: The AI Model that Recreates PAC-MAN From Scratch—Just by 
Watching It Being Played. NVIDIA Blog. Retrieved from https://blogs.nvidia.com/blog/gamegan-research-pacman-anniversary/

UC Berkeley CS188 Intro to AI, ai.berkeley.edu/project_overview.html. Accessed 25 Sept. 2024. 




