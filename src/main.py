from src.application.pre_processing import PreProcessingApplication
from src.common.entity.pre_processing_response import PreProcessingResponse
from src.helpers.enum.database_types import DatabaseTypes

from src.helpers.errors import NotImplementedYetException
from src.factory import get_database_contract

class ThPyLearn():
    def __init__(self) -> None:
        raise NotImplementedYetException

class ThPreProcessing():
    def __init__(self, database_type: int = DatabaseTypes.DEFAULT_DATABASE_TYPE):
        self.database_type = database_type
        self.database_contract = get_database_contract(self.database_type, {})

    def pre_processing(self) -> PreProcessingResponse:
        return PreProcessingApplication(self.database_contract).execute()
