from typing import List
import pandas as pd

from src.common.contract.application.database_contract import DatabaseContract


class CSV(DatabaseContract):

    def __init__(self, data) -> None:
        self.data = pd.read_csv(data)
        print(self.data.head())


    def extract_X(self, start_predictor_index: int, end_predictor_index: int) -> List[List]:
        return self.data.iloc[:, start_predictor_index:end_predictor_index].values

    def extract_Y(self, classifier_index:int) -> List:
        return self.data.iloc[:, classifier_index].values

    def separate_base_learning_and_test(self, percent: int) -> None:
        pass

    def remove_line_if_null_params(self, pos: int) -> None:
        pass
