
[//]: # (Image References)
[image1]:cont_control.gif  "Trained Agent"

# Project 2: Continuous Control

### Introduction

For this project, we work with the [Reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#reacher) environment. The environment for this project involves controlling     
a **double-jointed arm**, to reach target locations.  A reward of +0.1 is provided for each step that the agent's hand         
is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many     
time steps as possible.  The accompanying research paper can be found [here](https://arxiv.org/pdf/1803.07067.pdf). For demonstrating the collective robot    
reinforcement learning see the [Googl AI Blog paper](https://ai.googleblog.com/2016/10/how-robots-can-acquire-new-skills-from.html).

![Trained Agent][image1]

The observation space (i.e., state space) has 33 dimensions corresponding to position, rotation, velocity, 
and angular velocities of the arm. The action space has 4 dimensions corresponding to torque applicable to two joints. 
Every entry in the action vector should be a number between -1 and 1.
