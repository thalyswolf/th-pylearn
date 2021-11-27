class InvalidLearningAlgorithmException(Exception):

    """ Exception raised when passed an invalid algorithm param """

    def __init__(self, message="You have input an invalid algorithm"):
        self.message = message
        super().__init__(self.message)