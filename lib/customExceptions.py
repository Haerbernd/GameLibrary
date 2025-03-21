from lib.system_operations import OperatingSystem

class UnsupportedArgumentException(Exception):
    def __init__(self, message: str = 'Unsupported Argument used...', code: int = 1, details=None):
        super().__init__(message)  # Pass the message to the base class
        self.code = code  # Custom attribute
        self.details = details

class UnsupportedOperatingSystemException(Exception):
    def __init__(self, os: OperatingSystem, message: str = ""):
        if message == "":
            message = f"Unsupported Operating System {os}..."
        super().__init__(message)