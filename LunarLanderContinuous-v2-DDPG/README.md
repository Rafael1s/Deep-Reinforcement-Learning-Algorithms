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
