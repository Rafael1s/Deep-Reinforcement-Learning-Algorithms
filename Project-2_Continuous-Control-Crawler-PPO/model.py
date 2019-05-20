import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1. / np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units, fc2_units):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): Number of nodes in first hidden layer
            fc2_units (int): Number of nodes in second hidden layer
        """
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1_bn = nn.BatchNorm1d(state_size)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2_bn = nn.BatchNorm1d(fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)

        self.fc2a_bn = nn.BatchNorm1d(fc2_units)
        self.fc2a = nn.Linear(fc2_units, fc2_units)

        self.fc3_bn = nn.BatchNorm1d(fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)
        self.reset_parameters()

    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))

        self.fc2a.weight.data.uniform_(*hidden_init(self.fc2a))

        self.fc3.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state):
        """Build an actor (policy) network that maps states -> actions."""
        x = F.relu(self.fc1(self.fc1_bn(state)))
        x = F.relu(self.fc2(self.fc2_bn(x)))

        x = F.relu(self.fc2a(self.fc2a_bn(x)))

        return F.tanh(self.fc3(self.fc3_bn(x)))


class Critic(nn.Module):
    """Critic (Value) Model."""

    def __init__(self, state_size, seed, fc1_units, fc2_units):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            seed (int): Random seed
            fcs1_units (int): Number of nodes in the first hidden layer
            fc2_units (int): Number of nodes in the second hidden layer
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1_bn = nn.BatchNorm1d(state_size)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2_bn = nn.BatchNorm1d(fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)

        self.fc2a_bn = nn.BatchNorm1d(fc2_units)
        self.fc2a = nn.Linear(fc2_units, fc2_units)

        self.fc3_bn = nn.BatchNorm1d(fc2_units)
        self.fc3 = nn.Linear(fc2_units, 1)
        self.reset_parameters()

    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))

        self.fc2a.weight.data.uniform_(*hidden_init(self.fc2a))

        self.fc3.weight.data.uniform_(-3e-3, 3e-3)

    def forward(self, state):
        """Build an critic (value) network that maps states -> value."""
        x = F.relu(self.fc1(self.fc1_bn(state)))
        x = F.relu(self.fc2(self.fc2_bn(x)))

        x = F.relu(self.fc2a(self.fc2a_bn(x)))

        return F.tanh(self.fc3(self.fc3_bn(x)))

class PPO_Actor_Critic(nn.Module):
    
#    def __init__(self, state_size, action_size, seed, fc1_units=1024, fc2_units=1024):
    def __init__(self, state_size, action_size, seed, fc1_units=128, fc2_units=128):
        super(PPO_Actor_Critic, self).__init__()
        self.actor = Actor(state_size, action_size, seed, fc1_units, fc2_units)
        self.critic = Critic(state_size, seed, fc1_units, fc2_units)  
        self.std = nn.Parameter(torch.ones(1, action_size)*0.15)

    def forward(self, state, action=None, scale=1.):
        """Build Policy.
        
        Returns
        ======
            action (Tensor): predicted action or inputed action
            log_prob (Tensor): log probability of current action distribution
            ent (Tensor): entropy of current action distribution
            value (Tensor): estimate value function
        """
        action_mean = self.actor(state)
        value = self.critic(state)
        
        dist = torch.distributions.Normal(action_mean, F.hardtanh(self.std, min_val=0.06*scale, max_val=0.6*scale))

        if action is None:
            action = dist.sample()
        log_prob = dist.log_prob(action)
        log_prob = torch.sum(log_prob, dim=1, keepdim=True)

        ent = dist.entropy().mean()

        return action, log_prob, ent, value
