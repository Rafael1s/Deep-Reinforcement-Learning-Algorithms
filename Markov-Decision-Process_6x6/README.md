## Environment World

  The environment _state space_ is the gridworld 6x6. The agent learns how to achieve the right down cell (green)      
  from any other cell. In the _rose cells_ (bad cells) the agent gets reward = -2, in the _yellow cells_ (usual cells)   
  the reward = -1,  in the single _green cell_ (**target**)  the reward = 10.
 
  ![](6x6_states.png)
  
## Actions

**_R_**: (0,1) =  **Right**,   
**_L_**: (0,-1) = **Left**,   
**_U_**: (-1,0) = **Up**,   
**_D_**: (1,0) =  **DOWN** 

## Transitions

Let the agent be in the cell (0,0), the  left-up cell. If the agent should get the action=**Up**, then he has 10%   
chance of going down, 10% of going left and 80% chance of remaining in place because the agent cannot    
go up from this cell. The same for the action=**Left** because the agent cannot go left from the cell=(0,0).   
Assume the agent is in the cell=(0,3), and the action=**Up**. Then the agent has 10% chance of going down,   
10% of going left, 10% of going right and 70% chance of remaining in place because the agent cannot go up   
from this cell. For the action=**Left** he has 10% chance of going down, of going right, of remaining in place    
and 70% chance of going left. For each action out {**Up**, **Left**, **Right**, **Down**}, the probabilties of going   
to one of 4 cells or of remaining in place are given in the picture below. Here, the transitions rules are   
given almost for any cell. For remaining cells, the transitions rules are similarly given.  

![](actions_from_cell.png)

## Credit

 Most of the code is based on the webinar code of Willian Paiva.
 
