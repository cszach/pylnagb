class DimensionError(Exception):
    def __init__(self, message="Dimension mismatch"):
        super(DimensionError, self).__init__(message)
