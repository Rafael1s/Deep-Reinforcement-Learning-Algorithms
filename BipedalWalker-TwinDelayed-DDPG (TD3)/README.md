# Project - BipedalWalker with Twin Delayed DDPG (TD3)    

### Environment  

Solving the environment require an average total reward of over 300 over 100 consecutive episodes.  
Training of BipedalWalker is considered as [difficult task](https://ctmakro.github.io/site/on_learning/rl/bipedal.html), 
in particular, it is very difficult to train BipedalWalker by DDPG. In this directory we solve the environment in __1795 episodes__
by usage of the __Twin Delayed DDPG (TD3)__ algorithm, see [here](https://arxiv.org/abs/1802.09477).
For another solution (based on the single agent), see [BipedalWalker-Soft-Actor-Critic](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/BipedalWalker-Soft-Actor-Critic).

![](images/bipedalwalker.jpg)

### Three TD3 tricks   

A common failure mode for DDPG is that the learned Q-function begins to dramatically overestimate Q-values,      
which then leads to the policy breaking, because it exploits the errors in the Q-function.     
Twin Delayed DDPG (TD3) is an algorithm which addresses this issue by [introducing three critical tricks:](https://spinningup.openai.com/en/latest/algorithms/td3.html)

* **Trick One:** Clipped Double-Q Learning. TD3 learns two Q-functions instead of one (hence “twin”),        
and uses the smaller of the two Q-values to form the targets in the Bellman error loss functions.      

* **Trick Two:**  “Delayed” Policy Updates. TD3 updates the policy (and target networks) less frequently      
than the Q-function. The paper recommends one policy update for every two Q-function updates.   
See parameter **policy_freq**  in the function _train()_, _class TD3_.

* **Trick Three**: Target Policy Smoothing. TD3 adds noise to the target action, to make it harder   
for the policy to exploit Q-function errors by smoothing out Q along changes in action.   
See parameter **policy_noise**  in the function _train()_, _class TD3_.

            # Select action according to policy and add clipped noise 
            noise = torch.FloatTensor(u).data.normal_(0, policy_noise).to(device)
            noise = noise.clamp(-noise_clip, noise_clip)
            next_action = (self.actor_target(next_state) + noise).clamp(-self.max_action, self.max_action)

Together, these three tricks result in substantially improved performance over baseline DDPG.     

### Video

 See video [BipedalWalker by Training Stages](https://www.youtube.com/watch?v=g01mIFbxVns) demonstrating 5 different
 levels of the TD3 training. 

### Training History

1.  Score 293, Achieved in 2000 episodes   

![](plots/plot_2000epis_293.9score.png)

2.  Score 300.5, Achived in 1795 episodes   
     
![](plots/plot_1795epis_300.5score.png)

3. Score 304, Achieved in 1086 episodes

![](plots/plot_1086epis_304score.png)

More points in fewer episodes. It happens!


### Credit

The source paper is [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477)  
by _Scott Fujimoto_ , _Herke van Hoof_, _David Meger_.
