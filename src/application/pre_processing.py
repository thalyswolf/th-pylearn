from src.common.entity.pre_processing_response import PreProcessingResponse
from src.common.contract.application.database_contract import DatabaseContract


class PreProcessingApplication():

    def __init__(self, base_contract: DatabaseContract) -> None:
        self._base_contract = base_contract

    def execute(self) -> PreProcessingResponse:
        
        response = PreProcessingResponse()
        response.X = self._base_contract.extract_X()
        response.Y_training = self._base_contract.extract_Y()
        response.Y_test = self._base_contract.extract_Y()

        return response
