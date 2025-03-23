# Tuning Strategy Selection Guide

## Algorithm Comparison
| Criteria        | Bayesian Optimization (BO) | Reinforcement Learning (RL) | Evolutionary Algorithms (EA) |
|-----------------|----------------------------|-----------------------------|------------------------------|
| Best For        | Low-dim params (<20)        | Dynamic environments        | Multi-objective optimization |
| Compute Cost    | Medium                     | High                        | High                         |
| Parallelization | Moderate                   | Limited                     | Excellent                    |
| Sample Eff.     | High                       | Low                         | Medium                       |

## Decision Tree
```mermaid
graph TD
    A[Start] --> B{Number of Parameters?}
    B -->|<=20| C{Need Multi-Objective?}
    B -->|>20| D[Use Evolutionary]
    C -->|Yes| E[NSGA-III]
    C -->|No| F[Bayesian Optimization]
    D --> G{Dynamic Environment?}
    G -->|Yes| H[PPO/Decision Transformer]
    G -->|No| I[CMA-ES]
```

## When to Use Which?
- **BO**: 
  - Hyperparameter tuning (learning rate, dropout)
  - Resource-constrained environments
- **RL**:
  - Neural architecture search
  - Concept drift adaptation
- **EA**:
  - Hardware-aware optimization (latency vs accuracy)
  - Dataset shift mitigation