from abc import ABC, abstractmethod

class LearnContract(ABC):

    @abstractmethod
    def training():
        pass

    @abstractmethod
    def predict():
        pass
