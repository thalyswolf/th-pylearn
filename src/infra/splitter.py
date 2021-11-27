from typing import List
from src.common.contract.application.splitter_contract import SplitterContract
from sklearn.model_selection import train_test_split

class Splitter(SplitterContract):

    @staticmethod
    def split(x: List[List], y: List, percent: float) -> List[List]:
        return train_test_split(x, y, test_size=percent, random_state=0)
