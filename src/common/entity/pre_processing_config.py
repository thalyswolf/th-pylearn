from src.helpers.enum.action_for_outliers_and_null_values import ActionForOutliersAndNullValues


class PreProcessingConfig():

    """ Percentage of data used for testing 0.00 - 1.00 """
    _percent_test: float = 0.15

    """ Action for handle outlier data """
    _action_for_outliers: int = ActionForOutliersAndNullValues.DEFAULT_VALUE

    """ Action for handle null data """
    _action_for_null_values: int = ActionForOutliersAndNullValues.DEFAULT_VALUE

    def get_percent_test(self):
        return self._percent_test

    def get_action_for_outliers(self):
        return self._action_for_outliers

    def get_action_for_null_values(self):
        return self._action_for_null_values

    def set_percent_test(self, percent_test: float):
        self._percent_test = percent_test

    def set_action_for_outliers(self, action_for_outliers: int):
        self._action_for_outliers = action_for_outliers

    def set_action_for_null_values(self, action_for_null_values: int):
        self._action_for_null_values = action_for_null_values
