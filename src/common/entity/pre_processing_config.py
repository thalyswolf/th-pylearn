from typing import List
from src.helpers.enum.action_for_outliers_and_null_values import ActionForOutliersAndNullValues


class PreProcessingConfig():

    """ Percentage of data used for testing 0.00 - 1.00 """
    _percent_test: float = 0.15

    """ Action for handle outlier data """
    _action_for_outliers: int = ActionForOutliersAndNullValues.DEFAULT_VALUE

    """ Action for handle null data """
    _action_for_null_values: int = ActionForOutliersAndNullValues.DEFAULT_VALUE

    """ Keeping same scale on data values """
    _keep_same_scale: bool = True

    _encoder_columns: List[int] = []

    def get_percent_test(self) -> float:
        return self._percent_test

    def get_action_for_outliers(self) -> int:
        return self._action_for_outliers

    def get_action_for_null_values(self) -> int:
        return self._action_for_null_values

    def get_keep_same_scale(self) -> bool:
        return self._keep_same_scale

    def get_encoder_columns(self) -> List[int]:
        return self._encoder_columns

    def set_percent_test(self, percent_test: float):
        self._percent_test = percent_test

    def set_action_for_outliers(self, action_for_outliers: int):
        self._action_for_outliers = action_for_outliers

    def set_action_for_null_values(self, action_for_null_values: int):
        self._action_for_null_values = action_for_null_values

    def set_keep_same_scale(self, keep_same_scale: bool):
        self._keep_same_scale = keep_same_scale

    def set_encoder_columns(self, columns: List[int]):
        self._encoder_columns = columns

    def add_encoder_columns(self, index: int):
        self._encoder_columns.append(index)
