class FileProcessingError(Exception):
    """Base exception for file processing errors."""
    pass

class InvalidDataError(FileProcessingError):
    """Raised when data validation fails."""

    # Currently a placeholder
    def __init__(self, data):
        self.data = data
        super().__init__(f"Invalid data: {self.data}")

class MissingFieldError(FileProcessingError):
    """Raised when a required field is missing."""

    # Currently a placeholder
    def __init__(self, field):
        self.field = field
        super().__init__(f"Missing required field: {self.field}")