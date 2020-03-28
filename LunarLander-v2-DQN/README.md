# Project -  LunarLander with DQN

### Environment

Solving the environment require an average total reward of over **200** over 100 consecutive episodes.   
If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or   
comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main   
engine is -0.3 points each frame. Firing side engine is -0.03 points each frame.   
Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on   
its first attempt. Four discrete actions available:   
* 0 - do nothing, 
* 1 - fire left orientation engine, direction = -1,
* 2 - fire main engine,   direction = 0,
* 3 - fire right orientation engine, direction = 1

![](images/LunaLander.png)

### Deep Q-Network (DQN)

For other DQN projects, see    
[_Navigation_](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Project-1_Navigation-DQN), 4 discrete actions are available:     
0 - move forward, 1 - move backward, 2 - turn left, 3 - turn right.    
[_Cartpole_](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/edit/master/Cartpole-Deep-Q-Learning), 2 discrete actions are available:  
0 - push cart to the left, 1 - push cart to the right.

# Training  

Score **200** achieved in **688** episodes  

![](images/plot-LunaLander-v2-DQN-688epis.png)


