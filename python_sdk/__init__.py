"""
DSIS Common Model Python SDK

A Python SDK for the OpenWorks Common Model schemas, providing type-safe
data models and utilities for working with DSIS (Data Source Integration Service) data.

This SDK is automatically generated from JSON Schema definitions and provides:
- Pydantic-based data models with validation
- Type hints for better IDE support
- Serialization/deserialization utilities
- Integration with existing OData query builders

Example usage:
    from dsis_sdk.models import Well, Company
    from dsis_sdk.utils import validate_data, serialize_to_json
    
    # Create a well instance
    well = Well(
        native_uid="well_123",
        well_name="Test Well",
        well_uwi="12345678901234567890123456"
    )
    
    # Validate and serialize
    if well.is_valid():
        json_data = serialize_to_json(well)
"""

__version__ = "1.0.0"
__author__ = "DSIS Team"
__description__ = "Python SDK for OpenWorks Common Model schemas"

# Import main modules
from . import models
from . import utils
from . import exceptions

# Import commonly used classes
from .utils.validation import validate_data, ValidationError
from .utils.serialization import serialize_to_json, deserialize_from_json

__all__ = [
    "models",
    "utils",
    "exceptions",
    "validate_data",
    "ValidationError",
    "serialize_to_json",
    "deserialize_from_json",
]
