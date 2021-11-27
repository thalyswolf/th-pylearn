from src.helpers.enum.learning_algorithms import LearningAlgorithms

def get_learn_contract(learning_algorithm: int):
    if LearningAlgorithms.BAYESIAN_LEARNING == learning_algorithm:
        pass
