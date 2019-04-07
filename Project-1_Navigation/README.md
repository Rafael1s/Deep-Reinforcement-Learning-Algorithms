[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"

# Project 1: Navigation

### Introduction

For this project, we will train an agent to navigate (and collect bananas!) in a large, square world.  

![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

### Completion criteria

The task is episodic, and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

### Environment

The environment is simulated by Unity application _Banana_ lying in the subdirectory _Banana_Windows_x86_64_
We start the environment as follows:

_env = UnityEnvironment(file_name="Banana_Windows_x86_64/Banana.exe")_

### Training sessions

We perform several training sessions in according  tothe variable _numb_of_trains_.
For each training, the result weights are saved into the file 'weights_'+str(train_numb)+'.trn'.
For example, if _numb_of_trains_ = 5, we get files:

   _weights_0.trn,  weights_1.trn,  weights_2.trn,  weights_3.trn, weights_0.trn._

For each training session we cocstruct new agent with different parameters
and launch the *Deep-Q-Network* procedure as follows:

  agent = **Agent**(state_size=37, action_size=4, seed=1, fc1_units=fc1_nodes, fc2_units=fc2_nodes)       
  scores, episodes = **dqn**(n_episodes = 2000, eps_start = epsilon_start, train_numb=i)  # train with current params

### Training parameters

We experience the following parameters:  _fc1_units_, _fc2_units_,  _eps_start_
At the end of each session these parameters together with the episode number (at which the training is finished) 
are saved into the corresponding lists. These lists are used on the step of testing of weights.

### Deep-Q-Network algorithm

The _Deep-Q-Network_ procedure **dqn** performs the **double loop**. External loop (by _epsodes_) is executed till 
the number of episodes reached the maximal number of episodes _n_episodes = 2000_ or the _completion criteria_ is executed.
For the completion criteria, we check  

  _np.mean(scores_window) >=13_,  

where _scores_window_ is the array of the type deque realizing  thw shifting window of length <= 100.
The element _scores_window[i]_ contains the _score_ achieved by the algorithm on the episode _i_.

The internal loop of **dqn** gets the current _action_ from the **agent**.
After that **dqn** gets _state_ and _reward_ from Unity environment.
Then, the **agent** accept params _state,action,reward,next_state, done_
to the next training step. The variable _score_ accumulate obtained rewards.



