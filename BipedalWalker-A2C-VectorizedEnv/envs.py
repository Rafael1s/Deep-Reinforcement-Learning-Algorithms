import gym
import numpy as np
import torch
from gym.spaces.box import Box

from init_vec_env import VecEnvWrapper
from dummy_vec_env import DummyVecEnv
from subproc_vec_env import SubprocVecEnv

class AddTimestep(gym.ObservationWrapper):
    def __init__(self, env=None):
        super(AddTimestep, self).__init__(env)
        self.observation_space = Box(
            self.observation_space.low[0],
            self.observation_space.high[0],
            [self.observation_space.shape[0] + 1],
            dtype=self.observation_space.dtype)

    def observation(self, observation):
        return np.concatenate((observation, [self.env._elapsed_steps]))
    
class VecPyTorch(VecEnvWrapper):
    def __init__(self, venv, device):
        """Return only every `skip`-th frame"""
        super(VecPyTorch, self).__init__(venv)
        self.device = device
        # TODO: Fix data types

    def reset(self):
        obs = self.venv.reset()
        obs = torch.from_numpy(obs).float().to(self.device)
        return obs

    def step_async(self, actions):
        actions = actions.squeeze(1).cpu().numpy()
        self.venv.step_async(actions)

    def step_wait(self):
        obs, reward, done, info = self.venv.step_wait()
        obs = torch.from_numpy(obs).float().to(self.device)
        reward = torch.from_numpy(np.expand_dims(np.stack(reward), 1)).float()
        return obs, reward, done, info
    

def make_env(env_id, seed, rank, log_dir, add_timestep, allow_early_resets):
    def _thunk():
        env = gym.make(env_id)
        env.seed(seed + rank)

        obs_shape = env.observation_space.shape

        if add_timestep and len(
                obs_shape) == 1 and str(env).find('TimeLimit') > -1:
            env = AddTimestep(env)

        #if log_dir is not None:
        #    env = bench.Monitor(env, os.path.join(log_dir, str(rank)),
        #                        allow_early_resets=allow_early_resets)

        # If the input has shape (W,H,3), wrap for PyTorch convolutions
        '''
        obs_shape = env.observation_space.shape
        if len(obs_shape) == 3 and obs_shape[2] in [1, 3]:
            env = TransposeImage(env)
        '''
        
        return env

    return _thunk

def make_vec_envs(env_name, seed, num_processes, gamma, log_dir, add_timestep, device, allow_early_resets):
    envs = [make_env(env_name, seed, i, log_dir, add_timestep, allow_early_resets) for i in range(num_processes)]

    if len(envs) > 1:
        envs = SubprocVecEnv(envs)
    else:
        envs = DummyVecEnv(envs)

    envs = VecPyTorch(envs, device)

    '''
    if len(envs.observation_space.shape) == 3:
        print('Creating frame stacking wrapper')
        envs = VecPyTorchFrameStack(envs, 4, device)
        #print(envs.observation_space)    '''
     
    return envs



