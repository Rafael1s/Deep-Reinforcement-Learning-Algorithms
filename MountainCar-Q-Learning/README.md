# Project - MountainCar with Q-learning   
    
Mountain Car, is a problem in which an under-powered car must drive up a steep hill.   
    
![](images/two_diagr_mcar_0.5.png)

Since gravity is stronger than the car's engine, even at full throttle,    
the car cannot simply accelerate up the steep slope. The car is situated in a valley    
and must learn to leverage potential energy by driving up the opposite hill     
before the car is able to make it to the goal at the top of the rightmost hill.   
The domain has been used as a test bed in various Reinforcement Learning papers.   

### State and action spaces

The states are the position of the car in the horizontal axis on the range [-1.2, 0.6]      
and its velocity on the range [-0.07, 0.07]. The goal is to get the car to accelerate    
up the hill and get to the flag.  The possible actions are __(left, neutral, right)__.   
Thus, we have the two-dimensional continuous __state space__   [position x velocity].   
and one-dimensional discrete __action space__ with values (0,1,2).    

### Environment and reward threshold

Solving the environment require an average total reward of over __-110__ on 100 consecutive episodes.    
By using the __Q-learning__ algorithm we solve __MountainCar-v0__ environment in **283600 episodes**   
in **22 minutes !**.   

_Note that Q-learning is the core of the DQN (Deep Q-Network) algoritm, but it is not Deep Learning,   
since we do not use neural networks!_

### Discretization

The state space [position x velocity] is discretized into __12x12__  buckets.
![](images/discretize_function.png)




