# Project - AntBulletEnv with Soft Actor Critic (SAC)

### Introduction

Solving the environment require an average total reward of over 2500 over 100 consecutive episodes.   
We solve the environment  by usage of the __SAC__ algorithm, see the basic paper [SAC: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor](https://arxiv.org/abs/1801.01290/).  

![](images/Ant_two_stages.png)

### Requirement
* [python 3.7.3](https://www.python.org) 
* [pytorch 1.2.0](https://pytorch.org/)
* [gym 0.13.1](https://github.com/openai/gym)
* [pybullet 2.5.6](https://pypi.org/project/pybullet/)

### Environment parameters

max steps in episode:  1000   
state space dimension:  28   
action space dimension:  Box(8,)   

### Hyperparameters

batch size: 256    
learning rate:  0.0001

### Entropy regularization  

A central feature of SAC is [entropy regularization](https://spinningup.openai.com/en/latest/algorithms/sac.html).     
The major difference with common RL algorithms is training to maximize a trade-off between     
expected return and entropy, a measure of randomness in the policy. This has a close connection     
to the exploration-exploitation trade-off: increasing entropy results in more exploration,   
which can accelerate learning later on. It can also prevent the policy from prematurely    
converging to a bad local optimum.

### Reparameterization Trick

This trick makes training converge better due to lower variance. See function _sample()_ in the class  
_GaussianPolicy_ from _model.py_. The reparameterization trick allows us to rewrite the expectation over actions   
(which contains a pain point: the distribution depends on the policy parameters) into an [expectation over noise](https://spinningup.openai.com/en/latest/algorithms/sac.html).

### Training Score

The threshold score **2500** was achieved in the episode **1811**  after training **24 hours**.

![](images/plot_Ant_1811epis.png)

### Other SAC projects

* [BipedalWalker](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/BipedalWalker-Soft-Actor-Critic)
* [HopperBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/HopperBulletEnv-v0-SAC)
* [Walker2dBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/Walker2DBulletEnv-v0_SAC)

### Video
See video [Martian Ant](https://www.youtube.com/watch?v=s7aMZ1bbQgk&t=18s) on youtube.

### Credit
Most of the code is based on the Udacity code, and Pranjal Tandon's code (https://github.com/pranz24).
