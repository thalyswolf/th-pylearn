from src.infra.databases.csv import CSV
from src.helpers.errors.unsupported_database import UnsupportedDatabaseException
from src.helpers.enum.database_types import DatabaseTypes

def get_database_contract(database_type: int, database_data):

    if DatabaseTypes.CSV == database_type:
        return CSV(database_data)

    raise UnsupportedDatabaseException()
