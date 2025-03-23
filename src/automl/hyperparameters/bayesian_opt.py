import optuna  
from optuna.integration import PyTorchLightningPruningCallback  
from sklearn.model_selection import cross_val_score  
import numpy as np  

class BayesianOptimizer:  
    def __init__(self, meta_prior: Optional[Dict[str, float]] = None):  
        self.study = optuna.create_study(  
            direction="maximize",  
            sampler=optuna.samplers.TPESampler(prior=meta_prior)  
        )  

    def _objective(self, trial: optuna.Trial) -> float:  
        lr = trial.suggest_float("lr", 1e-5, 1e-2, log=True)  
        dropout = trial.suggest_float("dropout", 0.1, 0.5)  
        batch_size = trial.suggest_categorical("batch_size", [32, 64, 128])  

        model = create_model(lr, dropout)  
        score = cross_val_score(model, X, y, cv=5).mean()  
        return score  

    def optimize(self, n_trials=100) -> Dict[str, Any]:  
        self.study.optimize(self._objective, n_trials=n_trials)  
        return self.study.best_params  