from src.helpers.enum.learning_algorithms import LearningAlgorithms
from src.helpers.errors import NotImplementedYetException

class ThPyLearn():

    learning_algorithm = LearningAlgorithms().get_default_learning_algorithm()

    def __init__(self, learning_algorithm: int = None):
        if learning_algorithm is not None:
            self.learning_algorithm = learning_algorithm

    def training():
        raise NotImplementedYetException

    def predict():
        raise NotImplementedYetException

    def generate_matrix_confustion():
        raise NotImplementedYetException
