# Project -  LunarLanderContinuous with DDPG

### Environment

Solving the environment require an average total reward of over **200** over 100 consecutive episodes.   
If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or   
comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main   
engine is -0.3 points each frame. Firing side engine is -0.03 points each frame.   
Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on   
its first attempt. Four discrete actions available:   

![](images/LunaLander_300.png)

### Deep Deterministic Policy Gradient (DDPG)

The main paper: [_Continuous control with Deep RL_](https://arxiv.org/abs/1509.02971)

For other DDPG project, see [_Reacher_](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Project-2_Continuous-Control-Reacher-DDPG).

### Training

1. Score **200** achieved in **2560** episodes.

![](images/plot-LLC-v2-DDPG-2_2560epis.png)

Learning rate for actor = 1e-3, for critic = 1e-3


1. Score **200** achieved in **746** episodes.

![](images/plot-LLC-v2-test-LR_ACTOR-0.001-DDPG_746epis.png)

Learning rate for actor = 1e-4, for critic = 1e-3












