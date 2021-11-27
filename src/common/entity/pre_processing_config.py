from src.helpers.enum.action_for_outliers_and_null_values import ActionForOutliersAndNullValues


class PreProcessingConfig():

    """ Percentage of data used for testing 0.00 - 1.00 """
    PERCENT_TEST: float = 0.15

    """ Action for handle outlier data """
    ACTION_FOR_OUTLIERS: int = ActionForOutliersAndNullValues.DEFAULT_VALUE

    """ Action for handle null data """
    ACTION_FOR_NULL_VALUES: int = ActionForOutliersAndNullValues.DEFAULT_VALUE
