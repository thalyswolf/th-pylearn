from abc import ABC, abstractmethod


class DatabaseContract(ABC):

    @abstractmethod
    def extract_X(self) -> None:
        pass

    @abstractmethod
    def extract_Y(self) -> None:
        pass

    @abstractmethod
    def separate_base_learning_and_test(self, percent: int) -> None:
        pass

    @abstractmethod
    def remove_line_if_null_params(self, pos: int) -> None:
        pass

