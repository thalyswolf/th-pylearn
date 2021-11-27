from src.common.contract.application.database_contract import DatabaseContract


class CSV(DatabaseContract):

    def __init__(self, data) -> None:
        self.data = data

    def extract_X(self) -> None:
        return [0,1,2,3]

    def extract_Y(self) -> None:
        return [[0,1,2,3], [0,1,2,3], [0,1,2,3]]

    def separate_base_learning_and_test(self, percent: int) -> None:
        pass

    def remove_line_if_null_params(self, pos: int) -> None:
        pass
