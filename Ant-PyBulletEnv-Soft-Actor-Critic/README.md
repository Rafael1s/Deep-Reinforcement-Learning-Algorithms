# Project - AntBulletEnv with Soft Actor Critic (SAC)

### Introduction

Solving the environment require an average total reward of over 2500 over 100 consecutive episodes.   
We solve the environment  by usage of the __SAC__ algorithm, see the basic paper [SAC: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor](https://arxiv.org/abs/1801.01290/).  

![](images/Ant_two_stages.png)

### Environment parameters

max steps in episode:  1000   
state space dimension:  28   
action space dimension:  Box(8,)   

### Hyperparameters

batch size: 256    
learning rate:  0.0001

### Learning Curve

The threshold score **2500** was achieved in the episode **1811**  after training **24 hours**.

![](images/plot_Ant_1811epis.png)

### Video
See video [Martian Ant](https://www.youtube.com/watch?v=s7aMZ1bbQgk&t=18s) on youtube.

### Credit
Most of the code is based on the Udacity code, and Pranjal Tandon's code (https://github.com/pranz24).
