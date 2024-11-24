import torch
import torch.nn as nn

class GhostFNN(nn.Module):
    def __init__(self):
        super(GhostFNN, self).__init__()
        self.fc1 = nn.Linear(4, 8)  # 4 inputs (for each direction the ghost can move) 
        self.fc2 = nn.Linear(8, 4)  
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.softmax(self.fc2(x), dim=-1)  # Probabilities for each of the 4 directions 
        return x