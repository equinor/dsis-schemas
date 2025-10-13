"""
Validation Utilities

Provides validation functions for DSIS models and data.
"""

from typing import Any, Dict, List, Optional, Type, Union, TYPE_CHECKING
from pydantic import ValidationError as PydanticValidationError

if TYPE_CHECKING:
    from pydantic import BaseModel


class ValidationError(Exception):
    """Custom validation error for DSIS SDK."""

    def __init__(self, message: str, errors: Optional[List[Dict[str, Any]]] = None):
        super().__init__(message)
        self.errors = errors or []


def validate_data(data: Dict[str, Any], model_class: Type['BaseModel']) -> 'BaseModel':
    """
    Validate data against a DSIS model class.
    
    Args:
        data: Dictionary containing data to validate
        model_class: DSIS model class to validate against
        
    Returns:
        Validated model instance
        
    Raises:
        ValidationError: If validation fails
    """
    try:
        return model_class(**data)
    except PydanticValidationError as e:
        error_details = []
        for error in e.errors():
            error_details.append({
                'field': '.'.join(str(loc) for loc in error['loc']),
                'message': error['msg'],
                'type': error['type'],
                'input': error.get('input')
            })
        
        raise ValidationError(
            f"Validation failed for {model_class.__name__}: {str(e)}",
            errors=error_details
        )


def validate_json_data(json_data: str, model_class: Type['BaseModel']) -> 'BaseModel':
    """
    Validate JSON string against a DSIS model class.
    
    Args:
        json_data: JSON string containing data to validate
        model_class: DSIS model class to validate against
        
    Returns:
        Validated model instance
        
    Raises:
        ValidationError: If validation fails
    """
    try:
        return model_class.from_json(json_data)
    except PydanticValidationError as e:
        error_details = []
        for error in e.errors():
            error_details.append({
                'field': '.'.join(str(loc) for loc in error['loc']),
                'message': error['msg'],
                'type': error['type'],
                'input': error.get('input')
            })
        
        raise ValidationError(
            f"JSON validation failed for {model_class.__name__}: {str(e)}",
            errors=error_details
        )


def validate_multiple(data_list: List[Dict[str, Any]], model_class: Type['BaseModel']) -> List['BaseModel']:
    """
    Validate multiple data items against a DSIS model class.
    
    Args:
        data_list: List of dictionaries containing data to validate
        model_class: DSIS model class to validate against
        
    Returns:
        List of validated model instances
        
    Raises:
        ValidationError: If any validation fails
    """
    validated_items = []
    validation_errors = []
    
    for i, data in enumerate(data_list):
        try:
            validated_item = validate_data(data, model_class)
            validated_items.append(validated_item)
        except ValidationError as e:
            validation_errors.append({
                'index': i,
                'data': data,
                'errors': e.errors
            })
    
    if validation_errors:
        raise ValidationError(
            f"Validation failed for {len(validation_errors)} out of {len(data_list)} items",
            errors=validation_errors
        )
    
    return validated_items


def is_valid_data(data: Dict[str, Any], model_class: Type['BaseModel']) -> bool:
    """
    Check if data is valid for a DSIS model class without raising exceptions.
    
    Args:
        data: Dictionary containing data to validate
        model_class: DSIS model class to validate against
        
    Returns:
        True if valid, False otherwise
    """
    try:
        validate_data(data, model_class)
        return True
    except ValidationError:
        return False


def get_validation_errors(data: Dict[str, Any], model_class: Type['BaseModel']) -> Optional[List[Dict[str, Any]]]:
    """
    Get validation errors for data without raising exceptions.

    Args:
        data: Dictionary containing data to validate
        model_class: DSIS model class to validate against

    Returns:
        List of validation errors, or None if valid
    """
    try:
        validate_data(data, model_class)
        return None
    except ValidationError as e:
        return e.errors


def validate_field_value(value: Any, field_name: str, model_class: Type['BaseModel']) -> bool:
    """
    Validate a single field value against a model's field constraints.
    
    Args:
        value: Value to validate
        field_name: Name of the field
        model_class: DSIS model class containing the field
        
    Returns:
        True if valid, False otherwise
    """
    try:
        # Create a minimal data dict with just this field
        test_data = {field_name: value}
        model_class(**test_data)
        return True
    except (PydanticValidationError, ValidationError):
        return False
