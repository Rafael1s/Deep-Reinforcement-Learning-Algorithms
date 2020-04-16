# Project - BipedalWalker with Twin Delayed DDPG (TD3)

### Environment  

Solving the environment require an average total reward of over **2500** over 100 consecutive episodes.  
Training of HopperBulletEnv is performed using the __Twin Delayed DDPG (TD3)__ algorithm, see    
the basic paper [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477).    
In this directory we solve the HopperBulletEnv environment in **3240 episodes** with the parameter **noise std = 0.03**,
and in **5438** episodes with **noise std = 0.01**.
