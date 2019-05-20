import numpy as np
import random
import torch
import torch.nn as nn
import torch.optim as optim
from collections import namedtuple, deque
from model import PPO_Actor_Critic

BATCH_SIZE = 1024         # minibatch size
MIN_BATCH_NUM = 32        # the minimum number of batch in each learning epoch
GAMMA = 0.99              # discount factor
TAU = 0.99                # GAE factor (General advantage estimator)
LEARNING_RATE = 1e-4      # learning rate of the actor
EPSILON = 1e-5            # epsilon of Adam
WEIGHT_DECAY = 1e-4       # weight decay of Adam
PPO_CLIP = 0.2            # clip factor in ppo
CLIP_GRAD = 1             # clip factor of gradient
ENTROPY_COEFFICENT = 0.01 # coefficent of entropy
NOISE_REDUCE = 0.999      # reduce the threshold of std in action

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Agent():
    """Interacts with and learns from the environment."""
    def __init__(self, state_size, action_size, random_seed, n_agent, fc1_units=128, fc2_units=128):
        """Initialize an Agent object.
        
        Params
        ======
            state_size (int): dimension of each state
            action_size (int): dimension of each action
            random_seed (int): random seed
            n_agent (int): number of agents
        """
        self.state_size = state_size
        self.action_size = action_size
        self.seed = random.seed(random_seed)
        self.actor_critic = PPO_Actor_Critic(state_size, action_size, random_seed, \
                                             fc1_units=fc1_units, fc2_units=fc2_units).to(device)
        self.optimizer = optim.Adam(self.actor_critic.parameters(), 
                        lr=LEARNING_RATE, eps=EPSILON, weight_decay=WEIGHT_DECAY)
        self.trajectory = []
        self.n_agent = n_agent
        self.std_scale = 1.

        self.memory = ReplayBuffer(BATCH_SIZE, n_agent, random_seed)
    
    def act(self, states, scale=1.):
        """Returns actions for given states as per current policy.
        
        Returns
        ======
            action (Tensor): predicted action or inputed action
            log_prob (Tensor): log probability of current action distribution
            value (Tensor): estimate value function
        """
        states = torch.from_numpy(states).float().to(device)
        self.actor_critic.eval()
        if scale != 1.:
            self.std_scale = 0.
        with torch.no_grad():
            actions, log_probs, _, values = self.actor_critic(state=states, scale = self.std_scale)
            actions = actions.cpu().data.numpy()
        self.actor_critic.train()
        return actions, log_probs, _, values

    def save_step(self, trajectory):
        """Save each step to current trajectory."""
        self.trajectory.append(trajectory)

    def save_trajectory(self, states):
        pending_value = self.act(states)[-1]
        self.trajectory.append([states, pending_value, None, None, None, None])

        processed_trajectory = [None] * (len(self.trajectory) - 1)
        advantages = torch.Tensor(np.zeros((self.n_agent, 1))).to(device)
        returns = pending_value.detach()
        
        for i in reversed(range(len(self.trajectory) - 1)):
            states, value, actions, log_probs, rewards, terminals = self.trajectory[i]
            terminals = torch.Tensor(terminals).unsqueeze(1).to(device)
            rewards = torch.Tensor(rewards).unsqueeze(1).to(device)
            actions = torch.Tensor(actions).to(device)
            states = torch.Tensor(states).to(device)
            next_value = self.trajectory[i + 1][1]
            returns = rewards + GAMMA * terminals * returns
            td_error = rewards + GAMMA * terminals * next_value.detach() - value.detach()
            advantages = advantages * TAU * GAMMA * terminals + td_error
            processed_trajectory[i] = [states, actions, log_probs, returns, advantages]
        self.memory.add(processed_trajectory)
        # reset trajectory
        self.trajectory = []

    def step(self, states):

        self.save_trajectory(states)

        if self.memory.__len__()*self.n_agent >= BATCH_SIZE * MIN_BATCH_NUM:

            for sampled_states, sampled_actions, sampled_log_probs_old, sampled_returns, sampled_advantages in self.memory.sample():

                _, log_probs, entropy_loss, values = self.actor_critic(state=sampled_states, action=sampled_actions)
                ratio = (log_probs - sampled_log_probs_old).exp()

                obj = ratio * sampled_advantages
                obj_clipped = ratio.clamp(1.0 - PPO_CLIP,
                                            1.0 + PPO_CLIP) * sampled_advantages
                policy_loss = -torch.min(obj, obj_clipped).mean(0) - ENTROPY_COEFFICENT * entropy_loss.mean()
                value_loss = 0.5 * (sampled_returns - values).pow(2).mean()

                self.optimizer.zero_grad()
                (policy_loss + value_loss).backward()
                nn.utils.clip_grad_norm_(self.actor_critic.parameters(), CLIP_GRAD)
                self.optimizer.step()

            # reset memory
            self.memory.reset()
        self.std_scale = self.std_scale * NOISE_REDUCE


class ReplayBuffer:
    """Fixed-size buffer to store experience tuples."""

    def __init__(self, batch_size, n_agent, seed):
        """Initialize a ReplayBuffer object.
        Params
        ======
            batch_size (int): size of each training batch
        """
        self.memory = []
        self.batch_size = batch_size
        self.seed = np.random.seed(seed*2018)
    
    def add(self, trajectories):
        """Add new trajectory to memory."""
        self.memory.extend(trajectories)
    
    def sample(self):
        """Randomly sample a batch of experiences from memory."""
        states, actions, log_probs_old, returns, advantages = map(lambda x: torch.cat(x, dim=0), zip(*self.memory))
        advantages = (advantages - advantages.mean()) / advantages.std()

        indices = np.arange(states.size()[0])
        np.random.shuffle(indices)
        indices = [indices[div*self.batch_size: (div+1)*self.batch_size] for div in range(len(indices) // self.batch_size + 1)]

        result = []
        for indice in indices:
            if len(indice) >= self.batch_size / 2:
                indice = torch.Tensor(indice).long().to(device)
                result.append([states[indice], actions[indice], log_probs_old[indice], returns[indice], advantages[indice]])
        return result

    def reset(self):
        self.memory = []
    
    def __len__(self):
        return len(self.memory)
