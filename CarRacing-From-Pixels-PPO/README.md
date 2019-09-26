# Project - CarRacing with PPO, Learning from Raw Pixels 

### Introduction

This is the continuous control task learning from pixels, a top-down racing environment. 
State consists of 96x96 pixels. Reward is -0.1 every frame and +1000/N for every track tile visited, 
where N is the total number of tiles in track. For example, if you have finished in 732 frames, 
your reward is 1000 - 0.1\*732 = 926.8 points. The indicators shown at the bottom of the window. 
CarRacing-v0 defines "solving" as getting average reward of 900 over 100 consecutive trials.

![](images/plot_Reward_200-1000.png)

### Environment
The environment is simulated by OpenAI package __gym__ as follows:

      env = gym.make('CarRacing-v0', verbose=0)
      
### Training the agent

We train the agent to understand that it can use information from its surroundings to inform the next best action.

### Hyperparameters

Agent uses the following hyperparameters:

**GAMMA=0.99** # discount, the coefficient related to the **next state**  

**EPOCH= 8** # the parameter in the update mexanism of the PPO  (beter than 10)

**MAX_SIZE = 2000** # the maximal size of the buffer used in the update mechanism

**BATCH=128**  # optimizer and backward mechisms work after sampling BATCH elements

**LEARNING_RATE = 0.001**

**EPS=0.1** # the clipping parameter using for calculation of the **action loss** in the update mechanism 

     surr1 = ratio * advantage
     surr2 = torch.clamp(ratio, 1.0 - EPS, 1.0 + EPS) * advantage
     action_loss = -torch.min(surr1, surr2)

### Neural Network Model

We use the CNN model with 6 levels Conv2d (torch.nn.Conv2d) and 6 ectified linear units ReLU (torch.nn.ReLU).
The rewards, target and advatage values are calculated by the model:

     target = r + GAMMA * net(next_state)
     advantage = target - self.net(state)
     
     

