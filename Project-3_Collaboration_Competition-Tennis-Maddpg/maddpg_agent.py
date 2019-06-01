import copy
import os
import random
from collections import namedtuple, deque

import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim

from ddpg_agent import ddpg_agent, ReplayBuffer, device
from model import Actor, Critic

BUFFER_SIZE = int(1e6)          # replay buffer size
BATCH_SIZE = 512                # minibatch size
LEARNING_PERIOD = 2             # weight update frequency

class maddpg_agent:
    """Wrapper class managing different agents in the environment."""

    def __init__(self, num_agents=2, state_size=24, action_size=2):
        """Initialize a maddpg_agent wrapper.
        Params
        ======
            num_agents (int): the number of agents in the environment
            state_size (int): dimension of each state
            action_size (int): dimension of each action
        """
        self.num_agents = num_agents
        self.state_size = state_size
        self.action_size = action_size
        
        self.agents = [ddpg_agent(state_size, action_size, i+1, random_seed=0) for i in range(num_agents)]
        
        # Replay memory
        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, seed=0)
        
    def reset(self):
        """Resets OU Noise for each agent."""
        for agent in self.agents:
            agent.reset()
            
    def act(self, observations, add_noise=False):
        """Picks an action for each agent given."""
        actions = []
        for agent, observation in zip(self.agents, observations):
            action = agent.act(observation, add_noise=add_noise)
            actions.append(action)
        return np.array(actions)
    
    def step(self, states, actions, rewards, next_states, dones, timestep):
        """Save experience in replay memory."""
        states = states.reshape(1, -1)
        actions = actions.reshape(1, -1)
        next_states = next_states.reshape(1, -1)
        
        self.memory.add(states, actions, rewards, next_states, dones)
        
        # Learn, if enough samples are available in memory
        if len(self.memory) > BATCH_SIZE and timestep%LEARNING_PERIOD == 0:
            for a_i, agent in enumerate(self.agents):
                experiences = self.memory.sample()
                self.learn(experiences, a_i)
            
    def learn(self, experiences, agent_number):
        """ The critic takes as its input the combined observations and 
        actions from all agents. Collect actions from each agent for the 'experiences'. """
        next_actions = []
        actions_pred = []
        states, _, _, next_states, _ = experiences
        
        next_states = next_states.reshape(-1, self.num_agents, self.state_size)
        states = states.reshape(-1, self.num_agents, self.state_size)
        
        for a_i, agent in enumerate(self.agents):
            agent_id_tensor = self._get_agent_number(a_i)
            
            state = states.index_select(1, agent_id_tensor).squeeze(1)
            next_state = next_states.index_select(1, agent_id_tensor).squeeze(1)
            
            next_actions.append(agent.actor_target(next_state))
            actions_pred.append(agent.actor_local(state))
            
        next_actions = torch.cat(next_actions, dim=1).to(device)
        actions_pred = torch.cat(actions_pred, dim=1).to(device)
        
        agent = self.agents[agent_number]
        agent.learn(experiences, next_actions, actions_pred)
                
    def _get_agent_number(self, i):
        """Helper to get an agent's number as a Torch tensor."""
        return torch.tensor([i]).to(device)
