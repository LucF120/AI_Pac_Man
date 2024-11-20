# Reinforcement Learning in Pac-Man
Allen Xu, Iba Baig, Luc Ferrara, Vishy Kamalapuram

---
### Project Overview
In this project, we aim to build an enhanced version of the Pac-Man game that combines reinforcement learning and neural networks to create a dynamic environment. The game will feature intelligent ghost agents that strategically target the Pac-Man player by utilizing deep reinforcement learning. This version of the game will allow for creative solutions combined with probabilistic inference, hopefully giving the agent and ghosts a fair chance of winning. This project will explore various AI learning techniques and game mechanisms to display real time decision making.

---
### Features
- Pacman AI
   - In order to train the ghosts, Pacman must be trained first
   - Utilizes the Pacman ALE enviornment to train with deep RL
   - Grayscale pixel representation of the enviornment fed into neural network to train Pacman
   - Ghosts then train off of the Pacman with these specific neural network weights
- Ghost AI
   - Custom built environment for ghosts to initally train off of Pacman using reinforcement learning
   - Player can also control Pacman to go against the ghost AI
   - Ghost AI will adapt to player controls as well

---
### Document Overview
- Pacman_reload_dqn.py: Saves and loads a state in the RL process
- pacman.py: Initial RL implementation to train Pacman in the gym enviornment for 10,000 episodes
- pacman_dqn_implementation.py: DQN implementation of training Pacman
- pacman_neural_network.py: Defines the Deep Q Network with pytorch
- view_pacman_gym_env.py: Allows viewing of the enviornment

---
### Getting Started
#### Prereqs
- Python 3.11.5
- numpy
- pytorch
- pickle


---
### Acknowledgements
This project uses the following libraries and resources:
- [Pacman ALE Enviornment](https://ale.farama.org/environments/pacman/) for training pacman
-  



