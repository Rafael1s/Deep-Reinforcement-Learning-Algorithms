import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=64, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units) # first fully-connected layer fc1
        self.fc2 = nn.Linear(fc1_units, fc2_units)  # second fully-connected layer fc2
        self.fc3 = nn.Linear(fc2_units, action_size) # third fully-connected layer fc3

    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = self.fc1(state)
        x = F.relu(x) # 1-st rectified nonlinear layer, state_size = 8, fc1_units = 64, tensor x is 64x8 = 512 units 
        x = self.fc2(x)
        x = F.relu(x) # 2-st rectified nonlinear layer
        x = self.fc3(x)
        return x
