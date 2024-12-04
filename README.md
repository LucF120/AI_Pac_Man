# Reinforcement Learning in Pac-Man
Allen Xu, Iba Baig, Luc Ferrara, Vishy Kamalapuram

---
### Project Overview
In this project, we aim to build an enhanced version of the Pac-Man game that combines reinforcement learning and neural networks to create a dynamic environment. The game will feature intelligent ghost agents that strategically target the Pac-Man player by utilizing deep reinforcement learning. This version of the game will allow for creative solutions combined with probabilistic inference, hopefully giving the agent and ghosts a fair chance of winning. This project will explore various AI learning techniques and game mechanisms to display real time decision making.

---
### Features
- Pacman AI
   - Trained with double-DQN algorithm and a convolution neural network
   - Utilizes the pre-existing Pacman ALE enviornment to train with deep RL
   - Run presaved neural networks against the ghosts
- Ghost AI
   - Custom built environment for ghosts to train
   - Trained using Deep Q-Network algorithm with a feed forward neural network
   - Run presaved neural networks of the ghosts against Pac-Man

---
### Document Overview
- Pacman_Training Directory:
  - Pacman_reload_dqn.py: Saves and loads a state in the RL process
  - Test.py: Run test games against default ghosts with a saved neural network
  - pacman_dqn_implementation.py: DQN implementation of training Pacman
  - pacman_neural_network.py: Defines the Deep Q Network with pytorch
- Custom_Enviornment Directory:
  - custom_pacman_env.py: Custom built pacman enviornment to train ghosts
  - ghosts_ffn.py: Feed forward neural network for ghosts
  - ghost_training.py: Train ghosts in custom enviornment
  - test_pacman_env.py: Test pacman model against ghost model
---
### Getting Started
1) Clone the repository:
`git clone https://github.com/allenyxu2004/CS4100_Pac_Man.git`

2) Navigate to project directory

3) Install required packages:
`pip install -r requirements.txt`

4) Running a saved Pac-Man model:
    - Upload saved policy_net.pth to src/Pacman_Training/previous_run
    - Run src/Pacman_Training/Test.py file

5) Running a saved Ghost model:
    - Upload saved policy_net.pth to src/Custom_Enviornment
    - Run src/Custom_Enviornment/test_pacman_env.py

6) Generating policy_net.pth files
    - Pacman policies can be generated in src/Pacman_Training/pacman_dqn_implementation.py
    - Ghost policies can be generated in src/Custom_Enviornment/ghosts_training.py


---
### Acknowledgements
This project uses the following libraries and resources:
- Farama Foundation. 2024. Arcade Learning Environment: Pac-Man. Available at: https://ale.farama.org/environments/pacman/.
- FYT3RP4TIL. 2024. Deep Convolutional Q-Learning OpenAI Gymnasium Pac-Man. Available at: https://github.com/FYT3RP4TIL/Deep-Convolutional-Q-Learning-OpenAI-Gymnasium-Pac-Man/blob/main/Deep_Convolutional_Q_Learning_Pac_Man.ipynb.
- OpenAI. 2024. PyTorch Reinforcement Learning (Q-Learning) Tutorial. Available at: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html.
- PacmanCode. 2024. Pacmancode Repository. Available at: https://pacmancode.com/.



