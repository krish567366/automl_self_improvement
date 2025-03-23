# NSGA-II implementation
# src/automl/hyperparameters/evolutionary.py  
from pymoo.algorithms.moo.nsga3 import NSGA3  
from pymoo.optimize import minimize  
from pymoo.problems import get_problem  
from pymoo.operators.crossover.sbx import SBX  
from pymoo.operators.mutation.pm import PM  

class EvolutionaryOptimizer:  
    def __init__(self, n_dim=10, n_obj=2):  
        self.problem = get_problem("automl_problem")  # Custom problem class required  
        self.algorithm = NSGA3(  
            pop_size=100,  
            crossover=SBX(prob=0.9, eta=15),  
            mutation=PM(eta=20),  
            eliminate_duplicates=True  
        )  

    def optimize(self):  
        res = minimize(  
            self.problem,  
            self.algorithm,  
            ("n_gen", 50),  
            seed=42,  
            verbose=True  
        )  
        return res.X, res.F  