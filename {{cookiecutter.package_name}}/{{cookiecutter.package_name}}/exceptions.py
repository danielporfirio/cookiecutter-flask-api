class ValidationError(ValueError):

    def __init__(self, message):
        self.message = message
