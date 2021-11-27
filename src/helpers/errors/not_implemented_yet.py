class NotImplementedYetException(Exception):

    """ Exception raised when something was not implemented """

    def __init__(self, message="Was not implemented yet"):
        self.message = message
        super().__init__(self.message)