from src.helpers.enum.learning_algorithms import LearningAlgorithms
from src.common.entity import BayesianLearn

def get_learn_contract(learning_algorithm: int):
    
    if LearningAlgorithms.BAYESIAN_LEARNING == learning_algorithm:
        return BayesianLearn()
