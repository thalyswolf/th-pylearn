class UnsupportedDatabaseException(Exception):

    """ Exception raised when passed an invalid database param """

    def __init__(self, message="Unsupported database"):
        self.message = message
        super().__init__(self.message)