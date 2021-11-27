from src.common.contract.application.pre_processing_contract import PreProcessingConfigContract
from src.common.entity.pre_processing_config import PreProcessingConfig
from src.application.pre_processing import PreProcessingApplication
from src.common.entity.pre_processing_response import PreProcessingResponse
from src.helpers.enum.database_types import DatabaseTypes

from src.helpers.errors import NotImplementedYetException
from src.factory import get_database_contract
from src.infra.encoder import Encoder
from src.infra.scaler import Scaler
from src.infra.splitter import Splitter

class ThPyLearn():
    def __init__(self) -> None:
        raise NotImplementedYetException

class ThPreProcessing():
    def __init__(self, 
                pre_processing_config: PreProcessingConfigContract = PreProcessingConfig(), 
                database_type: int = DatabaseTypes.DEFAULT_DATABASE_TYPE, 
                database_data={}):

        self.database_type = database_type
        self.database_contract = get_database_contract(self.database_type, database_data)
        self.pre_processing_config = pre_processing_config

    def pre_processing(self, start_predictor_index: int, end_predictor_index: int, classifier_index: int) -> PreProcessingResponse:
        encoder, scaler, splitter = Encoder, Scaler, Splitter

        return PreProcessingApplication(self.pre_processing_config, 
                                        self.database_contract,
                                        encoder, 
                                        scaler, 
                                        splitter
                                        )\
                                        .execute(start_predictor_index, end_predictor_index, classifier_index)

