# src/automl/core/meta_env.py  
import gym  
import numpy as np  
from gym import spaces  

class AutoMLEnv(gym.Env):  
    def __init__(self, dataset_embedding):  
        self.action_space = spaces.Dict({  
            "lr": spaces.Box(1e-6, 1e-2, shape=(1,)),  
            "batch_size": spaces.Discrete(4)  # 32, 64, 128, 256  
        })  
        self.observation_space = spaces.Box(low=-1, high=1, shape=dataset_embedding.shape)  
        self.dataset_embedding = dataset_embedding  

    def step(self, action):  
        # Train model with action config, return reward  
        accuracy = self._train_model(action)  
        reward = accuracy - 0.1 * action["lr"]  # Penalize large lr  
        return self.dataset_embedding, reward, True, {}  

    def reset(self):  
        return self.dataset_embedding  