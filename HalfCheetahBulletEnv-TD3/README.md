# Project - HalfChhetahBulletEnv with Twin Delayed DDPG (TD3)

### Environment  

Solving the environment require an average total reward of over 3000 over 100 consecutive episodes.    
The environment is solved in __1588 episodes__ in 21 hour 18 min by usage of the __Twin Delayed DDPG (TD3)__ algorithm,    
see the basic paper [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477).    

![](images/hc_images.png)

For __Three TD3 tricks__, see [Walker2DBulletEnv-v0_TD3 Readme](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/edit/master/Walker2DBulletEnv-v0_TD3/README.md).

### Exploration noise

Exploration noise is the crucial parameterin in TD3. For this project, the parameter **std_noise** is choosed **0.05**.      
For details, see [Three aspects of Deep RL: noise, overestimation and exploration](https://towardsdatascience.com/three-aspects-of-deep-rl-noise-overestimation-and-exploration-122ffb4bb92b).    

### Training Score

![](images/plot_HalfCheetah_1588epis_sc3000.png)

### Other TD3 projects

* [BipedalWalker](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/BipedalWalker-TwinDelayed-DDPG%20(TD3))  
* [HopperBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/HopperBulletEnv_v0-TD3)   
* [Walker2DBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/Walker2DBulletEnv-v0_TD3)   
* [MountainCarContinuous](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/MountainCarContinuous-TD3)   
   
### Videos
See videos 
[Such a fast cheetah](https://www.youtube.com/watch?v=Q-FchLEZKRk) and    
[Chessboard chase with four Pybullet actors](https://www.youtube.com/watch?v=NXX4GTim_NM) on youtube.

### Credit

The source paper is [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477)  
by _Scott Fujimoto_ , _Herke van Hoof_, _David Meger_.
