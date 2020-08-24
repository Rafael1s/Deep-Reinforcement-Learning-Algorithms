
[//]: # (Image References)
[image1]:images/Tennis.gif  "Trained Agent"
[image2]:images/plot_1600episodes.png "Plot_1600"
[image3]:images/plot_1700episodes.png "Plot_1700"

# Project 3: Collaboration and Competition

### Introduction

For this project, we work with the [Tennis](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#tennis) environment, where two agents control rackets to bounce ball over a net.     
If an agent hits a ball over net, the agent receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball   
out of bounds, the agent receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.    
The observation space is 24-dimensional consisting of 8 variables corresponding to the position and velocity  
of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding 
to movement toward (or away from) the net, and jumping. The accompanying research paper can be found [here](https://arxiv.org/pdf/1706.02275.pdf).

![Trained Agent][image1]


### Maddpg Environment

The environment is simulated by Unity application _Tennis.app_ lying in the subdirectory _Tennis_Windows_x86_64_.
We start the environment as follows:

      env = UnityEnvironment(seed=seed, file_name="Tennis_Windows_x86_64/Tennis.app")
      
The task is episodic, and in order to solve the environment, the agents must get an **average score** of +0.5 
(over 100 consecutive episodes, after taking the maximum over both agents).       

Let us compare multi-agent environment to single agent environments. It requires the training of two separate agents, 
and the agents need to collaborate under certain situations (like don’t let the ball hit the ground) 
and compete under other situations (like gather as many points as possible). Just doing a simple extension 
of single agent RL by independently training the two agents does not work very well because the agents 
are independently updating their policies as learning progresses. And this causes the environment to appear 
non-stationary from the viewpoint of any one agent. 

### Prepare environment on the local machine

You need at least the following three packages:

1. **deep-reinforcement-learning  (DRLND)**        
   The instructions to set up the DRLND repository can be found [here](https://github.com/udacity/deep-reinforcement-learning#dependencies). 
   This repository contains material related to Udacity's [Deep Reinforcement Learning Nanodegree](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893) program.

2. The project environment is similar to, but not identical to the _Tennis_ environment on the 
   [Unity ML-Agents GitHub page](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md).
   Instead this environment, the project works with the environment which is provided as a part of project
   (subdirectory 'python') 


3. **Unity environment _Tennis_**

    For this project, we not need to install Unity because the environment already built. The environment     
    can be downloaded as follows:

   Windows (64-bit), [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)    
   Windows (32-bit), [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)     

   Download this environment zip into  **p3_collab-compet/** folder, and unzip the file.

### Train the Agent

   Run the notebook _Tennis.ipynb_
   
   [1] import UnityEnvironment    
   [2] env = UnityEnvironment(seed=seed, file_name="Tennis_Windows_x86_64/Tennis.app")   # create environment        
   [3] Environments contain _brains_ which are responsible for deciding the actions of their associated agents.     
       We check for the first brain available.      
   [4] Examine the State and Action Spaces. We get the information frame as follows:   
       
     Number of agents: 2   
     Size of each action: 2   
     There are 2 agents. Each observes a state with length: 24    
     The state for the first agent looks like: 
     [ 0.          0.          0.          0.          0.          0.     
       0.          0.          0.          0.          0.          0.   
       0.          0.          0.          0.         -6.65278625 -1.5   
      -0.          0.          6.83172083  6.         -0.          0.        ]     
   
   [5]  Create _env_info_ and _maddpg agent_:

     env_info = env.reset(train_mode=True)[brain_name]      
     agent = maddpg_agent(num_agents=2, state_size=24, action_size=2)   

   [6]  Define and run the main function _train_ :
   
     scores_total, scores_global = train(maddpg, env, dir_chkpoints, n_episodes=1700)  
      
   [7]  Print graph of scores_total (blue bars) over all episodes, and  scores_global  
        (the line 'Avg on 100 episodes' - orange points)    
        The environment was solved in **1302 episodes**,  at this point the **Average Score** is achieved to **+0.5**,    
        see _Tennis.ipynb_ or _REPORT.ipynb_.   
        
        
### Train History

1. At **1600 episode** the **Average Score** is achived to **+1.14**.  
![Plot_1600][image2]

2. At **1700 episode** the **Average Score** is achived to **+1.42**.   
![Plot_1700][image3]

        
### Weights of the Trained Agent
  
  The **weights** of the trained agent are saved into files       
  
      checkpoint_actor_0.pth,  checkpoint_actor_1.pth,  checkpoint_critic_0.pth, checkpoint_critic_1.pth  
              
  into the directory 'dir_chk_1700d_episodes'

### Watch the Trained Agent

 Run the notebook _WatchAgent.ipynb_
 
 [1]  Start the Environment for Trained Agent  - Init Red and Blue Agents 
 [3]  Play Before Training    
        
      The result score (max over agents) almost for all games: 0.0  
        
 [2]  Load weights and Play: Prepare function _load_ and _play_   
 
      def load(dir) # input - directory containing checkpoint files
      play(agent, env, games) # agent is multi-agent ddpg     
            
 [4] Play after training in 1600 games 
 
      Game: 1, partial score: [1, 0],  Score #0: 2.60, Score #1: 2.60, Timesteps: 1000     
      Game: 2, partial score: [2, 0],  Score #0: 2.70, Score #1: 2.60, Timesteps: 1000     
      Game: 3, partial score: [3, 0],  Score #0: 0.20, Score #1: 0.19, Timesteps: 104     
      Game: 4, partial score: [3, 1],  Score #0: 0.09, Score #1: 0.10, Timesteps: 50     
      Game: 5, partial score: [4, 1],  Score #0: 2.60, Score #1: 2.60, Timesteps: 1000    
      
 [5] Play after Training in 1700 games   
 
     Game: 1, partial score: [1, 0],  Score #0: 2.70, Score #1: 2.60, Timesteps: 1000 
     Game: 2, partial score: [2, 0],  Score #0: 2.60, Score #1: 2.60, Timesteps: 1000 
     Game: 3, partial score: [3, 0],  Score #0: 0.10, Score #1: 0.09, Timesteps: 37 
     Game: 4, partial score: [3, 1],  Score #0: -0.01, Score #1: 0.10, Timesteps: 30 
     Game: 5, partial score: [4, 1],  Score #0: 2.60, Score #1: 2.60, Timesteps: 1000 
     
### Credit

Most of the code is based on Udacity's Mupti-agent DDPG code.
