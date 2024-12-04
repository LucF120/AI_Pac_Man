# Reinforcement Learning in Pac-Man
Allen Xu, Iba Baig, Luc Ferrara, Vishy Kamalapuram

---
### Project Overview
In this project, we aim to build an enhanced version of the Pac-Man game that combines reinforcement learning and neural networks to create a dynamic environment. The game will feature intelligent ghost agents that strategically target the Pac-Man player by utilizing deep reinforcement learning. This version of the game will allow for creative solutions combined with probabilistic inference, hopefully giving the agent and ghosts a fair chance of winning. This project will explore various AI learning techniques and game mechanisms to display real time decision making.

---
### Features
- Pacman AI
   - Trained with double-DQN algorithm and a convolution neural network
   - Utilizes the pre-existing Pacman ALE environment to train with deep RL
   - Run presaved neural networks against the ghosts
- Ghost AI
   - Custom built environment for ghosts to train
   - Trained using Deep Q-Network algorithm with a feed forward neural network
   - Run presaved neural networks of the ghosts against Pac-Man

---
### Document Overview
- src/Pacman_Training Directory:
  - Pacman_reload_dqn.py: Functions for saving/loading the policy network, target network, hyperparameters, and results. 
  - Test.py: Test running a Pac-Man policy against the default ghosts. 
  - pacman_dqn_implementation.py: DQN implementation of training Pacman
  - pacman_neural_network.py: The CNN used for the policy_net and target_net in the DQN. 
  - Saved_Results/: Contains a comprehensive history of training results. 
  - previous_run/: The location where saved results from running pacman_dqn_implementation.py are stored. 
  - Archive/: Contains old python files that were used to experiment with Deep Q-Learning and the ALE Gymnasium environment. 
- src/Custom_Environment Directory:
  - custom_pacman_env.py: Custom built pacman Gymnasium environment to train ghosts
  - ghosts_ffn.py: Feed forward neural network used in the RL implementation for ghosts. 
  - ghost_training.py: RL implementation for training ghosts. 
  - test_pacman_env.py: Test the ghosts policy against the existing Pac-Man policy. 
  - policy_net.pth: The policy which Pac-Man follows in the custom environment. 
  - Saved_Results/: Results from training the ghosts. 
  - util/: Contains the file display_grid.py, which was used to analyze the pixel values/locations of the observation space in order to design the custom gymnasium environment. 
  - resources/: Various resources used to analyze the state space for recreation. 
---
### Getting Started
1) Clone the repository:
`git clone https://github.com/allenyxu2004/CS4100_Pac_Man.git`

2) Navigate to project directory

3) Install Python version 3.11.5. 

4) Install required packages:
`pip install -r requirements.txt`

5) Running a saved Pac-Man model:
    - Upload saved policy_net.pth to src/Pacman_Training/previous_run, or use the pre-existing src/Pacman_Training/policy_net.pth file.
    - Run src/Pacman_Training/Test.py file

6) Running a saved Ghost model:
    - Upload saved ghost_policy_net.pth to src/Custom_Environment/previous_run, or use the pre-existing src/Custom_Environment/previous_run/ghost_policy_net.pth file.
    - Run src/Custom_Environment/test_pacman_env.py

7) Generating policy_net.pth files
    - Pacman policies are saved to src/Pacman_Training/previous_run after running src/Pacman_Training/pacman_dqn_implementation.py.
    - Ghost policies are saved to src/Custom_Environment/previous_run after running src/Custom_Environment/ghosts_training.py.

8) Training using a CUDA-enabled GPU 
    - See Cuda_Setup.md

---
### Acknowledgements
This project uses the following libraries and resources:
- Farama Foundation. 2024. Arcade Learning Environment: Pac-Man. Available at: https://ale.farama.org/environments/pacman/.
- FYT3RP4TIL. 2024. Deep Convolutional Q-Learning OpenAI Gymnasium Pac-Man. Available at: https://github.com/FYT3RP4TIL/Deep-Convolutional-Q-Learning-OpenAI-Gymnasium-Pac-Man/blob/main/Deep_Convolutional_Q_Learning_Pac_Man.ipynb.
- OpenAI. 2024. PyTorch Reinforcement Learning (Q-Learning) Tutorial. Available at: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html.
- PacmanCode. 2024. Pacmancode Repository. Available at: https://pacmancode.com/.



