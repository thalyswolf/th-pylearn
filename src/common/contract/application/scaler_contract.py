from abc import ABC, abstractmethod
from typing import List


class ScalerContract(ABC):

    @abstractmethod
    def scale(self, params: List[List]) -> List[List]:
        pass

