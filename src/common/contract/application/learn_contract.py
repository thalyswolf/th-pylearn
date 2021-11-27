from abc import ABC, abstractmethod


class LearnContract(ABC):

    @abstractmethod
    def training(self) -> None:
        pass
