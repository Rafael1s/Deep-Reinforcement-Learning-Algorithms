# Project - BipedalWalker with PPO, Vectorized Environment


### Introduction

Solving the environment require an average total reward of over 300 over 100 consecutive episodes.
Training of BipedalWalker is considered as [difficult task](https://ctmakro.github.io/site/on_learning/rl/bipedal.html), in particular, it is very difficult to train BipedalWalker by DDPG and PPO (with one agent). In this directory we solve the environment 
in **450** episodes by usage of the __PPO (with multi-agent)__ algorithm, see [Multi-Agent RL](https://bair.berkeley.edu/blog/2018/12/12/rllib/) or [Baseline doc](https://stable-baselines.readthedocs.io/en/master/modules/ppo2.html#note). Another solution (based on the single agent) is given in this repository is
[BipedalWalker-TD3](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/BipedalWalker-TwinDelayed-DDPG%20(TD3)). 

![](images/bwalker.png)

### Requirement

* [python 3.7](https://www.python.org) 
* [pytorch 1.0.1](https://pytorch.org/)
* [gym 0.13.1](https://github.com/openai/gym)

### Environment

The environment is simulated as list of 16 **gym** environments. They run in 16     
subprocesses adopted from [openai baseline](https://github.com/openai/baselines):

     num_processes=16
     envs = parallelEnv('BipedalWalker-v2', n=num_processes, seed=seed)       
     
### Hyperparameters

Agent uses the following hyperparameters:

_gamma=0.99_ # discount    
_epoch = 16_ # the parameter in the update mexanism of the PPO   
_mini_batch=16_ # optimizer and backward mechisms work after sampling BATCH elements   
_lr = 0.001_ # learning rate    
_eps=0.2_ # the clipping parameter using for calculation of the _action loss_   
     
