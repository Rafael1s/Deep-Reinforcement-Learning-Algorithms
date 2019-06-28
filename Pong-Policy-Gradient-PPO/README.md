# Pong with PPO

### Introduction 

In this notebook, we implement an agent learning to play Pong with
algorithm PPO ([Proximal Policy Optimization](https://openai.com/blog/openai-baselines-ppo/)).  
As with the [REINFORCE version](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Pong-Policy-Gradient-REINFORCE), 
the model learns from pixels.

![](images/cat_pong_giphy.gif)

## Algorithm PPO 

I. Collect trajectories based on the policy \Pi(\theta'),  
initialize  \theta' = \theta.

II. Compute the gradient for the clipped surrogate function

![](images/L_CLIPPED.png)

III. Gradient ascent, update \theta':

![](images/gradient_ascent.png)

IV. The internal loop of the PPO training: Steps II and III are repeated _k_ times,      
i.e., every trajectory is used _k_ times before it is trown away. In our case, _k_ = 4.    
For the case REINFORCE, _k_ = 1. In the code,  _k_ = _SGD_\__epoch_,  see file _pong_\__utils.py_,    
function _clipped_\__surrogate_.

V. External loop: back to step 1. Set \theta=\theta',
 go to new epsodes with new trajectories.

## Credit       
Most of the code is based on the Udacity code for the PPO algorithm.  
