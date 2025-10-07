"""
DSIS SDK Exceptions

Custom exception classes for the DSIS SDK.
"""


class DSISSDKError(Exception):
    """Base exception class for DSIS SDK errors."""
    pass


class ValidationError(DSISSDKError):
    """Raised when data validation fails."""
    
    def __init__(self, message: str, errors: list = None):
        super().__init__(message)
        self.errors = errors or []


class SerializationError(DSISSDKError):
    """Raised when serialization/deserialization fails."""
    pass


class ModelNotFoundError(DSISSDKError):
    """Raised when a requested model class is not found."""
    pass


class SchemaError(DSISSDKError):
    """Raised when there are issues with schema definitions."""
    pass


class FieldError(DSISSDKError):
    """Raised when there are issues with model fields."""
    pass
