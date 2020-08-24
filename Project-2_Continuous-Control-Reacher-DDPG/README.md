
[//]: # (Image References)
[image1]:cont_control.gif  "Trained Agent"

# Project 2: Continuous Control

### Introduction

For this project, we work with the [Reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#reacher) environment. The environment for this project involves controlling     
a **double-jointed arm**, to reach target locations.  A reward of +0.1 is provided for each step that the agent's hand         
is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many     
time steps as possible.  The accompanying research paper can be found [here](https://arxiv.org/pdf/1803.07067.pdf). For demonstrating the collective robot    
reinforcement learning see the [Googl AI Blog paper](https://ai.googleblog.com/2016/10/how-robots-can-acquire-new-skills-from.html).

![Trained Agent][image1]

The observation space (i.e., state space) has 33 dimensions corresponding to position, rotation, velocity, 
and angular velocities of the arm. The action space has 4 dimensions corresponding to torque applicable to two joints. 
Every entry in the action vector should be a number between -1 and 1.


### Environment

The environment is simulated by Unity application _Reacher_ lying in the subdirectory _Reacher_Windows_x86_64_.
We start the environment as follows:

      env = UnityEnvironment(file_name='Reacher_Windows_x86_64/Reacher.exe')

We are considering the version of the environment with 20 agents. After each episode, we add up the rewards received    
by each agent, to get a score for each agent. This yields 20 (potentially different) scores. We then take the     
**average score**  over all 20 agents. The environment is considered solved, when the average (over 100 episodes)      
of those average scores  is at least +30.    

### Prepare environment on the local machine

You need at least the following three packages:

1. **deep-reinforcement-learning  (DRLND)**        
   The instructions to set up the DRLND repository can be found [here](https://github.com/udacity/deep-reinforcement-learning#dependencies). This repository contains material related to Udacity's [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) program.

2. **ml-agents  (ML-Agents Toolkit)**
   To configure the ML-Agents Toolkit for Windows you need to complete the following steps:
    
    2.1  Creating a new Conda environment:
    
       conda create -n ml-agents python=3.6
       
    2.2 Activating ml-agents by the following command:
    
       activate ml-agents
       
    2.3 Latest versions of TensorFlow won't work, so you will need to make sure that you install version 1.7.1:
    
       pip install tensorflow==1.7.1
       
    For details on installing the ML-Agents Toolkit, see the instructions [here](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation-Windows.md).     
    
3. **Unity environment _Reacher_**

    For this project, we not need to install Unity because the environment already built. For 20 agents, the environment     
    can be downloaded as follows:

   Windows (64-bit), [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)    
   Windows (32-bit), [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)     

   Download this environment zip into  **p2_continuous-control/** folder, and unzip the file.

### Train the Agent

   Run the notebook _Continuous_Control.ipynb_
   
   [1] import UnityEnvironment    
   [2] env = UnityEnvironment(file_name='Reacher_Windows_x86_64/Reacher.exe')   # create environment      
   [3] Environments contain _brains_ which are responsible for deciding the actions of their associated agents. 
       We check for the first brain available.      
   [4] Examine the State and Action Spaces. We get the information frame as follows:   
       
     Number of agents: 20   
     Size of each action: 4    
     There are 20 agents. Each observes a state with length: 33   
     The state for the first agent looks like: [ 0.00000000e+00 -4.00000000e+00  0.00000000e+00  1.00000000e+00    
        -0.00000000e+00 -0.00000000e+00 -4.37113883e-08  0.00000000e+00    
         0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00    
         0.00000000e+00  0.00000000e+00 -1.00000000e+01  0.00000000e+00    
         1.00000000e+00 -0.00000000e+00 -0.00000000e+00 -4.37113883e-08    
         0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00    
         0.00000000e+00  0.00000000e+00  5.75471878e+00 -1.00000000e+00    
         5.55726624e+00  0.00000000e+00  1.00000000e+00  0.00000000e+00   
        -1.68164849e-01]    
   
   [5]  Create _env_info_ and _agent_:

     env_info = env.reset(train_mode=True)[brain_name]      
     agent = Agent(state_size=state_size, action_size=action_size, random_seed=15)     

   [6]  Define and run the main function _ddpg_ :
   
      scores = ddpg()

   The environment was solved in **195 episodes**, see _Continuous_Control.ipynb_ or _REPORT.ipynb_.     
      
   [7]  Print graph of scores over all episodes. 
        After the episode 143, the score achived the value 30.  
        
### Weights of the Trained Agent
  
  The **weights** of the trained agent are saved into the files _checkpoint_actor.pth_  and  _checkpoint_critic.pth_.

### Watch the Trained Agent

 Run the notebook _WatchAgent.ipynb_
 
 [1]  Start the Environment for Trained Agent   
 [2]  Prepare Player _play_   
 [3]  Play Before Training    
 
      play(agent, episodes=2)      
      
      Episode: 0 Average Score (over agents): 0.0      
      Episode: 1 Average Score (over agents): 0.0      
      
 [4] Load Trained Weights   
 [5] Play After Training    
 
     play(agent, episodes=3)
     
     Episode: 0 Average Score (over agents): 38.78149913316592   
     Episode: 1 Average Score (over agents): 38.71349913468585   
     Episode: 2 Average Score (over agents): 38.77949913321063   
     
### Deep Deterministic Policy Gradient (DDPG)

For other DDPG project, see [_LunarLanderContinuous_](https://github.com/Rafael1s/Deep-Reinforcement-Learning-Algorithms/tree/master/LunarLanderContinuous-v2-DDPG).

     
### Credit

Most of the code is based on the Udacity code for DDPG.     
Thanks to Amita K. from the Udacity Knowledge forum for the great tip cocerning the    
convergence of the algorithm, see ch. Hyperparameters in my Report file.  
