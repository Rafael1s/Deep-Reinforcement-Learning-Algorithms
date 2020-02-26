# Project -  Cartpole with Doouble Deep Q-Learning (DDQN)

### Environment

Solving the environment require an average total reward of over **195** for _Cartpole-v0_  and **475** for _Cartpole-v1_      
over 100 consecutive episodes. A pole is attached by an joint to a cart, which moves along a track.    
The system is controlled by applying a force of +1 or -1 to the cart. The pendulum starts upright, and     
the goal is to prevent it from falling over. A reward of +1 is provided for every timestep that the pole remains upright.     
The episode ends when the pole > 15 degrees from vertical, or the cart moves > 2.4 units from the center.  

![](images/cartpole_3.png) {.center}

<center><img src="images/cartpole_3.png"></center>



For another solution, see    
* [CartPole-Policy-Based-Hill-Climbing](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/CartPole-Policy-Based-Hill-Climbing), or
*  [CartPole-Policy-Gradient-Reinforce](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/CartPole-Policy-Gradient-Reinforce), or      
* [Cartpole with Deep Q-Learning](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Cartpole-Deep-Q-Learning).         
### Training History

1.  For Cartpole-v0: Score **195** achieved in **246** episodes   

![](images/plot_v0_ddqn_246episodes.png)

2.  For Cartpole-v0: Score **195** achieved in **612** episodes   

![](images/plot_v0_ddqn_612epis.png)

Note that such a quick achievement (246 episodes) of threshold 195       
is a very rare case, the second example (612 episodes) is a much more typical result.    

3.  For Cartpole-v1: Score **475** achived in **1030** episodes   
     
![](images/plot_v1-ddqn_1030epis.png)
