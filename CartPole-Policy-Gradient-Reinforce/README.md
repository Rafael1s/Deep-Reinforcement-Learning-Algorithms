## CartPole - known also as an Inverted Pendulum

## Power-Gradient Method - REINFORCE

REINFORCE algorithm is based on finding the **local maximum** of a function   
using a procedure known as **gradient ascent**.

![](gradient_ascent.jpg) 

## Other CartPole projects

* [CartPole-Policy-Based-Hill-Climbing](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/CartPole-Policy-Based-Hill-Climbing), or  
* [CartPole-Policy-Deep-Q_Learning](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/Cartpole-Deep-Q-Learning), or  
* [Cartpole with Double Deep Q-Learning](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/Cartpole-Double-Deep-Q-Learning)      
![](images/gif_cartpole.gif)

## Class Policy

This class implements the simple Convolution Neuron Network (CNN)
model containing only 2 fully-connected levels. In this CNN model, the
function __reinforce()__ approximizes the return value (= sum of all rewards with discounts).
The environment is solved in 791 episodes!

## Training log

Episode 100	Average Score: 34.47   
Episode 200	Average Score: 66.26   
Episode 300	Average Score: 87.82   
Episode 400	Average Score: 72.83   
Episode 500	Average Score: 172.00   
Episode 600	Average Score: 160.65    
Episode 700	Average Score: 167.15   

Environment solved in 791 episodes!	Average Score: 196.69   

## Credit

Most of the code is based on the Udacity code for the REINFORCE algorithm applied to CartPole.
