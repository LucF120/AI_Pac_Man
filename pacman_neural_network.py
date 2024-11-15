import torch
import torchvision
import torchvision.transforms.v2 as transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# Generative AI used to assist with getting the DQN setup. 

class DQN(nn.Module):
    def __init__(self, num_actions):
        super(DQN, self).__init__()
        
        # Convolutional layers with kernel size and stride chosen to downsample the image
        self.conv1 = nn.Conv2d(1, 32, kernel_size=8, stride=4)  # Output size: (60, 40)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=4, stride=2)  # Output size: (28, 19)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=3, stride=1)  # Output size: (26, 17)
        
        # Fully connected layer
        # The output of the last convolution layer will have shape (64, 26, 17)
        self.fc1 = nn.Linear(64 * 19 * 16, 512)  # Flatten and pass through a dense layer
        self.fc2 = nn.Linear(512, 5)  # Output layer (for classification)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.relu(self.conv3(x))
        
        # Flatten the output for the fully connected layers
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        q_values = self.fc2(x)
        
        return q_values
