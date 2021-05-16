import os
import numpy as np
import gym
from mujoco_py import load_model_from_path, MjSim, MjViewer


class MyRobotEnv(gym.Env):

    def __init__(self):
        self.model = load_model_from_path("my_envs/mujoco/assets/myrobot.xml")
        self.sim = MjSim(self.model)
        self.viewer = MjViewer(self.sim)

    
 
    '''
    def __init__(self):
        pass
    '''
    def step(self, action):
        pass
 
    def reset(self):
        pass
 
    
    def render(self, mode='human', close=False):
        t = 0

        while True:
 
            self.viewer.render()
            t += 1

