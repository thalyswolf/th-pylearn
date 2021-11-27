from abc import ABC, abstractmethod
from typing import List


class SplitterContract(ABC):

    @abstractmethod
    def split(self, x: List[List], y: List, percent: float) -> List[List]:
        pass

