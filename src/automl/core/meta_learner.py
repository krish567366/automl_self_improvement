import torch  
import numpy as np  
from stable_baselines3 import PPO  
from stable_baselines3.common.vec_env import DummyVecEnv  
from typing import Dict, Any, Optional  
from pydantic import BaseModel  

class TrainingState(BaseModel):  
    dataset_embedding: np.ndarray  
    val_accuracy: float  
    latency: float  

class MetaLearner:  
    def __init__(  
        self,  
        env: DummyVecEnv,  
        policy: str = "MlpPolicy",  
        device: str = "cuda" if torch.cuda.is_available() else "cpu"  
    ):  
        self.model = PPO(  
            policy,  
            env,  
            device=device,  
            tensorboard_log="./logs",  
            verbose=1  
        )  
        self.best_config: Optional[Dict[str, Any]] = None  

    def train(self, timesteps: int = 1e4) -> None:  
        self.model.learn(total_timesteps=timesteps)  

    def recommend_config(self, state: TrainingState) -> Dict[str, Any]:  
        action, _ = self.model.predict(state.dataset_embedding)  
        return {  
            "learning_rate": 10 ** (-4 + 2 * action[0]),  # Scaled to [1e-4, 1e-2]  
            "batch_size": 32 * (2 ** int(action[1]))  
        }  