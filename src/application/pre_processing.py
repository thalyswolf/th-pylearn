from src.common.contract.application.encoder_contract import EncoderContract
from src.common.contract.application.scaler_contract import ScalerContract
from src.common.contract.application.splitter_contract import SplitterContract
from src.infra.encoder import Encoder
from src.infra.scaler import Scaler
from src.common.contract.application.pre_processing_contract import PreProcessingConfigContract
from src.common.entity.pre_processing_response import PreProcessingResponse
from src.common.contract.application.database_contract import DatabaseContract


class PreProcessingApplication():

    def __init__(self, pre_processing_config: PreProcessingConfigContract, 
                base_contract: DatabaseContract,
                encoder: EncoderContract,
                scaler: ScalerContract,
                splitter: SplitterContract
                ) -> None:

        self._base_contract = base_contract
        self._pre_processing_config = pre_processing_config
        self._encoder = encoder
        self._scaler = scaler
        self._splitter = splitter

    def execute(self, start_predictor_index:int, end_predictor_index:int, classifier_index: int) -> PreProcessingResponse:
        
        response = PreProcessingResponse()
        response.X = self._base_contract.extract_X(start_predictor_index, end_predictor_index)
        response.Y = self._base_contract.extract_Y(classifier_index)

        if len(self._pre_processing_config.get_encoder_columns()):
            response.X = self._encoder.encode(response.X, self._pre_processing_config.get_encoder_columns())

        if self._pre_processing_config.get_keep_same_scale():
            response.X = self._scaler.scale(response.X)

        response.X, response.Y, response.X_training, response.Y_training = self._splitter(response.X, 
                                                                                        response.Y, 
                                                                                        self._pre_processing_config.get_percent_test())
       
        # TODO To implement auto detect outlier
        # TODO To implement auto isnull data

        return response
