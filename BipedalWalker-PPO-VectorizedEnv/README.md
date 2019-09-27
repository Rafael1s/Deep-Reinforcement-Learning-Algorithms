# Project - BipedalWalker with PPO, Vectorized Environment


### Environment

Solving the environment require an average total reward of over 300 over 100 consecutive episodes.
Training of BipedalWalker is considered as [difficult task](https://ctmakro.github.io/site/on_learning/rl/bipedal.html), in particular, it is very difficult to train BipedalWalker by DDPG and PPO (with one agent). In this directory we solve the environment 
in **450** episodes by usage of the __PPO (with multi-agent)__ algorithm, see [Multi-Agent RL](https://bair.berkeley.edu/blog/2018/12/12/rllib/) or [Baseline doc](https://stable-baselines.readthedocs.io/en/master/modules/ppo2.html#note). Another solution (based on the single agent) is given in this repository is
[BipedalWalker-TD3](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/BipedalWalker-TwinDelayed-DDPG%20(TD3)). 

![](images/bwalker.png)
