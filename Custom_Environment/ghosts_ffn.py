import torch
import torch.nn as nn

class GhostFNN(nn.Module):
    def __init__(self):
        super(GhostFNN, self).__init__()
        self.fc1 = nn.Linear(10, 128)  # 10 inputs: the x y coordinates of every ghost and pacman's x y
        self.fc2 = nn.Linear(128, 16)  
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)  # 16 outputs: probabilities for the movement options for each ghost
        return x