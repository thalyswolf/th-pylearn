from abc import ABC, abstractmethod

class ControllerContract(ABC):

    @abstractmethod
    def execute():
        pass
