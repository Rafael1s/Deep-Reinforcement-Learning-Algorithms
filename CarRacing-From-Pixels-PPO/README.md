# Project - CarRacing with PPO, Learning from Pixels 

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
      
### Training sessions
We run several training sessions in according to the variable numb_of_trains. For each training session, the obtained weights are saved into the file 'weights_'+str(train_numb)+'.trn'. We get files: weights_0.trn, weights_1.trn, weights_2.trn, etc.      
