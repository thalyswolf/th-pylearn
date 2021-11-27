from typing import List
from src.common.contract.application.scaler_contract import ScalerContract
from sklearn.preprocessing import StandardScaler

class Scaler(ScalerContract):

    @staticmethod
    def scale(params: List[List]) -> List[List]:
        return StandardScaler().fit_transform(params)