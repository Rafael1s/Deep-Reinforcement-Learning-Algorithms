[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif 
"Trained Agent"

[image2]: layers_96x88_585ep.png  "im2_96x88_585ep"
[image3]: layers_48x32_579ep.png  "im3_48x32_579ep"
[image4]: layers_80x88_572ep.png  "im4_80x88_572ep"
[image5]: layers_64x56_590ep.png  "im5_64x56_590ep"
[image6]: layers_80x88_633ep.png  "im6_80x88_633ep"

# Project 1: Navigation

### Introduction

For this project, we will train an agent to navigate (and collect bananas!) in a large, square world.  

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting 
a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while 
avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

### Completion criteria

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 
over 100 consecutive episodes.

### Environment

The environment is simulated by Unity application _Banana_ lying in the subdirectory _Banana_Windows_x86_64_
We start the environment as follows:

_env = UnityEnvironment(file_name="Banana_Windows_x86_64/Banana.exe")_

### Training sessions

We run several training sessions in according  to the variable _numb_of_trains_.
For each training session, the obtained weights are saved into the file 'weights_'+str(train_numb)+'.trn'.
We get files: _weights_0.trn_,  _weights_1.trn_,  _weights_2.trn_,  etc.

For each training session, we construct the **agent** with different parameters
and we run the *Deep-Q-Network* procedure **dqn** as follows:

  agent = **Agent**(state_size=37, action_size=4, seed=1, fc1_units=fc1_nodes, fc2_units=fc2_nodes)       
  scores, episodes = **dqn**(n_episodes = 2000, eps_start = epsilon_start, train_numb=i)  
  
### Training parameters

We experience the following parameters:  _fc1_units_, _fc2_units_,  _eps_start_.
At the end of each session these parameters together with the episode number (at which the training is finished) 
are saved into the corresponding lists. These lists are used on the step of testing of weights.
For each training session, 
 * _eps_start_ is played out as a random value from 0.988 to 0.955 with step 0.001, 
 * _fc1_units_ is played out as a random value from 48 to 128 with step 16,
 * _fc2_inits_ is played out as a random value from fc1_units - 16 to fc1_units - 16 with step 8.

### Deep-Q-Network algorithm

The _Deep-Q-Network_ procedure **dqn** performs the **double loop**. 
External loop (by _episodes_) is executed till the number of episodes reached the maximal number 
of episodes _n_episodes = 2000_ or the _completion criteria_ is executed.
The environment _env_  is reset with the paarmeter _train_mode_=_True_.
For the completion criteria, we check  

  _np.mean(scores_window) >=13_,  

where _scores_window_ is the array of the type deque realizing  the shifting window of length <= 100.
The element _scores_window[i]_ contains the _score_ achieved by the algorithm on the episode _i_.


In the internal loop,  **dqn** gets the current _action_ from the **agent**.
By this _action_ **dqn** gets _state_ and _reward_ from Unity environment.
Then, the **agent** accept params _state,action,reward,next_state, done_
to the next training step. The variable _score_ accumulates obtained rewards.

### Agent

The class **Agent** is defined in _dqn_agent.py_. This is the well-known class implementing 
the following mechanisms:

* Two Q-Networks (local and target) using the simple neural network.
* Replay memory (using the class ReplayBuffer)
* Epsilon-greedy mechanism
* Q-learning, i.e., using the max value for all possible actions
* Computing the loss function by MSE loss
* Minimize the loss by gradient descend mechanism using the ADAM optimizer

### Model Q-Network

Both Q-Networks (local and target) are implemented by the class
**QNetwork** lying in the file _model.py_. This class implements the simple
neural network with 3 fully-connected layers and 2 
rectified nonlinear layers. This **QNetwork** is realized in the framework 
of package **PyTorch**. The number of neurons of the fully-connected layers are 
as follows:

 * Layer fc1,  number of neurons: _state_size_ x _fc1_units_, 
 * Layer fc2,  number of neurons: _fc1_units_ x _fc2_units_,
 * Layer fc3,  number of neurons: _fc2_units_ x _action_size_,
 
where _state_size_ = 37, _action_size_ = 8, _fc1_units_ and _fc2_units_
are the input params.
 
### Output of training

This is the typical output of training sessions:

 fc1_units:  96 , fc2_units:  88   
 train_numb:  0 eps_start:  0.99    
 Episode: 585, elapsed: 0:09:51.835191, Avg.Score: 13.02,  score 16.0, How many scores >= 13: 58, eps.: 0.09    
 terminating at episode : 585 avg.reward reached +13 over 100 episodes      
 ![im2_96x88_585ep][image2]      
 
 fc1_units:  48 , fc2_units:  32      
 train_numb:  1 eps_start:  0.992   
 Episode: 579, elapsed: 0:09:29.603803, Avg.Score: 13.00,  score 18.0, How many scores >= 13: 51, eps.: 0.10   
 terminating at episode : 579 avg.reward reached +13 over 100 episodes   
 ![im3_48x32_579ep][image3]   
 
 fc1_units:  80 , fc2_units:  88      
 train_numb:  2 eps_start:  0.992   
 Episode: 572, elapsed: 0:09:32.363203, Avg.Score: 13.00,  score 18.0, How many scores >= 13: 65, eps.: 0.10   
 terminating at episode : 572 avg.reward reached +13 over 100 episodes   
 ![im4_80x88_572ep][image4]   

 fc1_units:  64 , fc2_units:  56      
 train_numb:  3 eps_start:  0.994   
 Episode: 590, elapsed: 0:09:39.475603, Avg.Score: 13.02,  score 18.0, How many scores >= 13: 57, eps.: 0.09   
 terminating at episode : 590 avg.reward reached +13 over 100 episodes    
 ![im5_64x56_590ep][image5]   

 fc1_units:  80 , fc2_units:  88    
 train_numb:  4 eps_start:  0.989    
 Episode: 633, elapsed: 0:10:47.455223, Avg.Score: 13.06,  score 20.0, How many scores >= 13: 58, eps.: 0.08    
 terminating at episode : 633 ave reward reached +13 over 100 episodes   
 ![im6_80x88_633ep][image6]    

### Testing sessions

We run testing for each file _weights_i.trn_, where i = 0,1,2,...
The testing procedure is implemented by the function **checkWeights**.
**Important**: the function **checkWeights** constructs again the agent with 
the parameters _fc1_units_ and _fc2_units_ corresponding to the fiven weights file.
The environment _env_  is reset with the paarmeter _train_mode_=_False_.

### Test average score

The function **checkWeights** calculates the accumulated score for 
the episode generated by Unity environment _env_.
For each testing session, we run **checkWeights** several times (=6 in this version) 
to get the average score for the given set of parameters. 

### Output of testing 

=========================================================   
Train: 0, Test: 0, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 13.0   
Train: 0, Test: 1, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 16.0   
Train: 0, Test: 2, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 18.0   
Train: 0, Test: 3, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 14.0   
Train: 0, Test: 4, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 13.0   
Train: 0, Test: 5, Episode: 585, fc1_units: 96, fc2_units: 88, eps_start: 0.99, Score: 17.0   
       
    Average Score:  15.17      
       
=========================================================   
Train: 1, Test: 0, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 15.0   
Train: 1, Test: 1, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 9.0   
Train: 1, Test: 2, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 17.0   
Train: 1, Test: 3, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 17.0    
Train: 1, Test: 4, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 18.0   
Train: 1, Test: 5, Episode: 579, fc1_units: 48, fc2_units: 32, eps_start: 0.992, Score: 17.0   

    Average Score:  15.5     
    
=========================================================  
Train: 2, Test: 0, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 18.0   
Train: 2, Test: 1, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 11.0  
Train: 2, Test: 2, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 12.0   
Train: 2, Test: 3, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 10.0   
Train: 2, Test: 4, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 13.0  
Train: 2, Test: 5, Episode: 572, fc1_units: 80, fc2_units: 88, eps_start: 0.992, Score: 13.0  

    Average Score:  12.83  
    
=========================================================   
Train: 3, Test: 0, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 13.0   
Train: 3, Test: 1, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 20.0   
Train: 3, Test: 2, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 19.0   
Train: 3, Test: 3, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 16.0  
Train: 3, Test: 4, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 18.0  
Train: 3, Test: 5, Episode: 590, fc1_units: 64, fc2_units: 56, eps_start: 0.994, Score: 14.0 

   Average Score:  16.67 ( **the best result**)
   
=========================================================  
Train: 4, Test: 0, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 16.0  
Train: 4, Test: 1, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 15.0   
Train: 4, Test: 2, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 16.0   
Train: 4, Test: 3, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 14.0   
Train: 4, Test: 4, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 16.0   
Train: 4, Test: 5, Episode: 633, fc1_units: 80, fc2_units: 88, eps_start: 0.989, Score: 12.0   

   Average Score:  14.83

### Credit

Most of the code is based on Udacity's DQN code.

        
