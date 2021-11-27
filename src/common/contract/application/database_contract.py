from abc import ABC, abstractmethod
from typing import List


class DatabaseContract(ABC):

    @abstractmethod
    def extract_X(self, start_predictor_index: int, end_predictor_index: int) -> List[List]:
        pass

    @abstractmethod
    def extract_Y(self, classifier_index: int) -> List:
        pass

    @abstractmethod
    def separate_base_learning_and_test(self, percent: int) -> None:
        pass

    @abstractmethod
    def remove_line_if_null_params(self, pos: int) -> None:
        pass

