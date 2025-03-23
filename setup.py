# PyPI packaging config
from setuptools import setup, find_packages  

setup(  
    name="automl_self_improvement",  
    version="0.1.0",  
    packages=find_packages(where="src"),  
    package_dir={"": "src"},  
    install_requires=[  
        "torch>=2.0.0",  
        "optuna>=3.0.0",  
        "fastapi>=0.85.0",  
        "stable-baselines3>=2.0.0"  
    ],  
    entry_points={"console_scripts": ["automl=automl.cli:main"]}  
)  