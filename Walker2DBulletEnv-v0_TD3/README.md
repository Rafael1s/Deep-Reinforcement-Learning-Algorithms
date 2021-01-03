# Project - Walker2DBulletEnv with Twin Delayed DDPG (TD3)    

### Environment  

Solving the environment require an average total reward of over 2500 over 100 consecutive episodes.  
The environment is solved in __9361 episodes__
by usage of the __Twin Delayed DDPG (TD3)__ algorithm, see the basic paper [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477).

![](images/Walker2D_two_stages_0.7.png)

### Three TD3 tricks   

A common failure mode for DDPG is that the learned Q-function begins to dramatically overestimate Q-values,      
which then leads to the policy breaking, because it exploits the errors in the Q-function.     
Twin Delayed DDPG (TD3) is an algorithm which addresses this issue by [introducing three critical tricks:](https://spinningup.openai.com/en/latest/algorithms/td3.html)

* **Trick One:** Clipped Double-Q Learning. TD3 learns two Q-functions instead of one (hence the name “twin”),        
and uses the smaller of the two Q-values to form the targets in the Bellman error loss functions. 
TD3 maintains a **pair of critics** Q1 amd Q2 along with a **single actor**.

* **Trick Two:**  “Delayed” Policy Updates. TD3 updates the policy (and target networks) less frequently      
than the Q-function. The paper recommends one policy update (**actor**) for every two Q-function (**critic**) updates.   
See parameter **policy_freq**  in the function _train()_, _class TD3_.

* **Trick Three**: Target Policy Smoothing. TD3 adds noise to the target action, to make it harder   
for the policy to exploit Q-function errors by smoothing out Q along changes in action.   
See parameter **policy_noise**  in the function _train()_, _class TD3_.
TD3 uses Gaussian noise, not Ornstein-Uhlenbeck noise as in DDPG.

### Exploration noise 

Exploration noise is the crucial parameterin in TD3. For this project, the parameter **std_noise** is choosed **0.02**.      
For details, see [Three aspects of Deep RL: noise, overestimation and exploration](https://towardsdatascience.com/three-aspects-of-deep-rl-noise-overestimation-and-exploration-122ffb4bb92b).    

### Off-policy

TD3 is an **off-policy** algorithm. In other words, the TD3 algorithm allows reusing the already collected data.
In the **agent.train** we get the batch of (_state, action, next_state, done, reward_)  of the _length = batch_size_:  

            # Sample replay buffer 
            x, y, u, r, d = replay_buffer.sample(batch_size)
            state = torch.FloatTensor(x).to(device)
            action = torch.FloatTensor(u).to(device)
            next_state = torch.FloatTensor(y).to(device)
            done = torch.FloatTensor(1 - d).to(device)
            reward = torch.FloatTensor(r).to(device)
            
### Training Score

![](images/plot_Walker2D_9361epis.png)

### Other TD3 projects

* [BipedalWalker](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/BipedalWalker-TwinDelayed-DDPG%20(TD3))  
* [HalfCheetahBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/HalfCheetahBulletEnv-TD3)   
* [HopperBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/HopperBulletEnv_v0-TD3)   
* [MountainCarContinuous](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/MountainCarContinuous-TD3)   


### Credit

The source paper is [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477)  
by _Scott Fujimoto_ , _Herke van Hoof_, _David Meger_.
            
            
