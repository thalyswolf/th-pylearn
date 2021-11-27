from abc import ABC, abstractmethod
from typing import List


class EncoderContract(ABC):

    @abstractmethod
    def encode(self, params: List[List]) -> List[List]:
        pass
