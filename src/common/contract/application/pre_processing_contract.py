from abc import ABC, abstractmethod
from typing import List


class PreProcessingConfigContract(ABC):

    @abstractmethod
    def get_percent_test(self) -> float:
        pass

    @abstractmethod
    def get_action_for_outliers(self) -> int:
        pass

    @abstractmethod
    def get_action_for_null_values(self) -> int:
        pass

    @abstractmethod
    def get_keep_same_scale(self) -> bool:
        pass

    @abstractmethod
    def get_encoder_columns(self) -> List[int]:
        pass

    @abstractmethod
    def set_percent_test(self, percent_test: float) -> None:
        pass

    @abstractmethod
    def set_action_for_outliers(self, action_for_outliers: int) -> None:
        pass

    @abstractmethod
    def set_action_for_null_values(self, action_for_null_values: int) -> None:
        pass

    @abstractmethod
    def set_keep_same_scale(self, keep_same_scale: bool) -> None:
        pass

    @abstractmethod
    def add_encoder_columns(self, index: int) -> None:
        pass

    @abstractmethod
    def set_encoder_columns(self, columns: List[int]) -> None:
        pass
