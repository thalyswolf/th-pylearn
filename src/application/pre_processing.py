from src.infra.encoder import Encoder
from src.infra.scaler import Scaler
from src.common.contract.application.pre_processing_contract import PreProcessingConfigContract
from src.common.entity.pre_processing_response import PreProcessingResponse
from src.common.contract.application.database_contract import DatabaseContract


class PreProcessingApplication():

    def __init__(self, pre_processing_config: PreProcessingConfigContract, 
                base_contract: DatabaseContract) -> None:

        self._base_contract = base_contract
        self._pre_processing_config = pre_processing_config

    def execute(self, start_predictor_index:int, end_predictor_index:int, classifier_index: int) -> PreProcessingResponse:
        
        response = PreProcessingResponse()
        response.X = self._base_contract.extract_X(start_predictor_index, end_predictor_index)
        response.Y = self._base_contract.extract_Y(classifier_index)

        if len(self._pre_processing_config.get_encoder_columns()):
            response.X = Encoder.encode(response.X, self._pre_processing_config.get_encoder_columns())

        if self._pre_processing_config.get_keep_same_scale():
            response.X = Scaler.scale(response.X)

        # response.Y_training = self._base_contract.extract_Y()
        # response.Y_test = self._base_contract.extract_Y()

        return response
