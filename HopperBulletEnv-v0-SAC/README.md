# Project - HopperBulletEnv with Soft Actor-Critic (SAC)

### Environment  

Solving the environment require an average total reward of over **2500** on 100 consecutive episodes.    
Training of HopperBulletEnv is performed using the __Soft Actor-Critic (SAC)__ algorithm, see    
two basic papers [SAC: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor](https://arxiv.org/abs/1801.01290)     
and [SAC Algorithms and Applications](https://arxiv.org/abs/1812.05905). The HopperBulletEnv environment was solved   
in 2 experiments:  (I) in **7662 episodes**. ,  (II)  in **3814** episodes.     

![](images/Hopper_two_stages_2.png)

### Tips to class GaussianPolicy

#### Scale and Bias 

   The varaible _scale_ is the length of the interval [low, high]:     
     _scale = (action_space.high - action_space.low)/2_     
   
   The varaible  _bias_  is the center of  the interval [low, high]:    
    _bias =  (action_space.high + action_space.low)/2_   
    
   These values give the map  [low, high]  --> [(low - bias)/scale, (high - bias)/scale] = [-1,1].  
   
 #### Activation Function
 
 ![](images/hyb_tangent_with_sigmoid.png)
 
 The **hyperbolic tangent function** torch.tanh is very similar to  the [logistic sigmoid function]
 (https://en.wikipedia.org/wiki/Sigmoid_function) g(x) = 1/(1 + exp(-x)).    
 However, the range of _logistic sigmoid function_ is [0,1] and the range of _tanh_ is [-1,1].   
 Then _tanh_ is should be more efficient because it has a wider range, and derivative is more steep,       

 ![](images/sigm_hybtg_deriv.png)   

see [Comparison of Activation Functions for Deep Neural Networks](https://towardsdatascience.com/comparison-of-activation-functions-for-deep-neural-networks-706ac4284c8a). 
 
Actually,  _tanh_ is the rescaled logistic sigmoid function, namely,  _tanh(x) = 2g(2x) - 1_.    
We also note that  _(tanh(x))' = 1 - (tanh(x))^2_.    
            
 
 #### Reparameterization
 
 ![](images/reparameterization.png)
 
 see [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) by D.Kingma, M.Welling
       

### Training Score

i.  The score 2500 was achieved in the episode **7662** after training **89 hours 23 minutes**.    
Learning rate = **0.0001**.

![](images/plot_Hopper_SAC_7662epis.png)

ii.  The score 2500 was achieved in the episode **3814** after training **37 hours 58 minutes**.    
Here, learning rate = **0.0003**.

![](images/plot_Hopper_SAC_3814epis.png)


### Other Soft Actor-Critic  projects    

* [AntBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Ant-PyBulletEnv-Soft-Actor-Critic)   
* [BipedalWalker](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/BipedalWalker-Soft-Actor-Critic)
* [Walker2dBulletEnv](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Udacity/tree/master/Walker2DBulletEnv-v0_SAC)

### Video
See video [Lucky Hopper](https://www.youtube.com/watch?v=Ipctq89yLB0) on youtube.
