import torch
import torch.nn.functional as F
from torch.optim import Adam
from model import GaussianPolicy, QNetwork

def soft_update(target, source, tau):
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(target_param.data * (1.0 - tau) + param.data * tau)

def hard_update(target, source):
    for target_param, param in zip(target.parameters(), source.parameters()):
        target_param.data.copy_(param.data)


class soft_actor_critic_agent(object):
    def __init__(self, num_inputs, action_space, \
                 device, hidden_size, seed, lr, gamma, tau, alpha):

        self.gamma = gamma
        self.tau = tau
        self.alpha = alpha

        self.device = device 
        self.seed = seed
        self.seed = torch.manual_seed(seed)
        
        torch.cuda.manual_seed(seed)
        #torch.cuda.manual_seed_all(seed)
        #torch.backends.cudnn.deterministic=True

        self.critic = QNetwork(seed, num_inputs, action_space.shape[0], hidden_size).to(device=self.device)
        self.critic_optim = Adam(self.critic.parameters(), lr=lr)

        self.critic_target = QNetwork(seed, num_inputs, action_space.shape[0], hidden_size).to(self.device)
        hard_update(self.critic_target, self.critic)
        
        # Target Entropy = −dim(A) (e.g. , -6 for HalfCheetah-v2) as given in the paper
        self.target_entropy = -torch.prod(torch.Tensor(action_space.shape).to(self.device)).item()
        self.log_alpha = torch.zeros(1, requires_grad=True, device=self.device)
        self.alpha_optim = Adam([self.log_alpha], lr=lr)
        self.policy = GaussianPolicy(seed, num_inputs, action_space.shape[0], \
                                         hidden_size, action_space).to(self.device)
        self.policy_optim = Adam(self.policy.parameters(), lr=lr)

    def select_action(self, state, eval=False):
        state = torch.FloatTensor(state).to(self.device).unsqueeze(0)
        if eval == False:
            action, _, _ = self.policy.sample(state)
        else:
            _, _, action = self.policy.sample(state)
        return action.detach().cpu().numpy()[0]

    def update_parameters(self, memory, batch_size, updates):
        # Sample a batch from memory
        state_batch, action_batch, reward_batch, next_state_batch, mask_batch = memory.sample(batch_size=batch_size)

        state_batch = torch.FloatTensor(state_batch).to(self.device)
        next_state_batch = torch.FloatTensor(next_state_batch).to(self.device)
        action_batch = torch.FloatTensor(action_batch).to(self.device)
        reward_batch = torch.FloatTensor(reward_batch).to(self.device).unsqueeze(1)
        mask_batch = torch.FloatTensor(mask_batch).to(self.device).unsqueeze(1)

        with torch.no_grad():
            next_state_action, next_state_log_pi, _ = self.policy.sample(next_state_batch)
            Q1_next_target, Q2_next_target = self.critic_target(next_state_batch, next_state_action)
            min_q_next_target = torch.min(Q1_next_target, Q2_next_target) - self.alpha * next_state_log_pi
            next_q_value = reward_batch + mask_batch * self.gamma * (min_q_next_target)

        # Two Q-functions to mitigate positive bias in the policy improvement step
        Q1, Q2 = self.critic(state_batch, action_batch) 
        Q1_loss = F.mse_loss(Q1, next_q_value) 
        Q2_loss = F.mse_loss(Q2, next_q_value) 
  
        action_batch_pi, log_pi, _ = self.policy.sample(state_batch)

        Q1_pi, Q2_pi = self.critic(state_batch, action_batch_pi)
        min_q_pi = torch.min(Q1_pi, Q2_pi)

        policy_loss = ((self.alpha * log_pi) - min_q_pi).mean() 
        
        self.critic_optim.zero_grad()
        Q1_loss.backward()
        self.critic_optim.step()

        self.critic_optim.zero_grad()
        Q2_loss.backward()
        self.critic_optim.step()
        
        self.policy_optim.zero_grad()
        policy_loss.backward()
        self.policy_optim.step()

        alpha_loss = -(self.log_alpha * (log_pi + self.target_entropy).detach()).mean()

        self.alpha_optim.zero_grad()
        alpha_loss.backward()
        self.alpha_optim.step()

        self.alpha = self.log_alpha.exp()
        alpha_tlogs = self.alpha.clone() # For TensorboardX logs
        
        soft_update(self.critic_target, self.critic, self.tau)    

