"""
Serialization Utilities

Provides serialization and deserialization functions for DSIS models.
"""

import json
from typing import Any, Dict, List, Optional, Type, Union, TYPE_CHECKING
from datetime import datetime, date
from decimal import Decimal

if TYPE_CHECKING:
    from pydantic import BaseModel


def serialize_to_json(
    model: 'BaseModel',
    exclude_none: bool = True,
    by_alias: bool = False, 
    indent: Optional[int] = None
) -> str:
    """
    Serialize a DSIS model to JSON string.
    
    Args:
        model: DSIS model instance to serialize
        exclude_none: Whether to exclude None values
        by_alias: Whether to use field aliases
        indent: JSON indentation level
        
    Returns:
        JSON string representation
    """
    return model.to_json(exclude_none=exclude_none, by_alias=by_alias, indent=indent)


def serialize_to_dict(
    model: 'BaseModel',
    exclude_none: bool = True,
    by_alias: bool = False
) -> Dict[str, Any]:
    """
    Serialize a DSIS model to dictionary.

    Args:
        model: DSIS model instance to serialize
        exclude_none: Whether to exclude None values
        by_alias: Whether to use field aliases

    Returns:
        Dictionary representation
    """
    return model.to_dict(exclude_none=exclude_none, by_alias=by_alias)


def deserialize_from_json(json_str: str, model_class: Type['BaseModel']) -> 'BaseModel':
    """
    Deserialize JSON string to DSIS model instance.

    Args:
        json_str: JSON string to deserialize
        model_class: DSIS model class to deserialize to

    Returns:
        DSIS model instance
    """
    return model_class.from_json(json_str)


def deserialize_from_dict(data: Dict[str, Any], model_class: Type['BaseModel']) -> 'BaseModel':
    """
    Deserialize dictionary to DSIS model instance.

    Args:
        data: Dictionary to deserialize
        model_class: DSIS model class to deserialize to

    Returns:
        DSIS model instance
    """
    return model_class.from_dict(data)


def serialize_multiple_to_json(
    models: List['BaseModel'],
    exclude_none: bool = True,
    by_alias: bool = False,
    indent: Optional[int] = None
) -> str:
    """
    Serialize multiple DSIS models to JSON array string.
    
    Args:
        models: List of DSIS model instances to serialize
        exclude_none: Whether to exclude None values
        by_alias: Whether to use field aliases
        indent: JSON indentation level
        
    Returns:
        JSON array string representation
    """
    serialized_models = [
        model.to_dict(exclude_none=exclude_none, by_alias=by_alias) 
        for model in models
    ]
    return json.dumps(serialized_models, indent=indent, default=_json_serializer)


def serialize_multiple_to_dict(
    models: List['BaseModel'],
    exclude_none: bool = True,
    by_alias: bool = False
) -> List[Dict[str, Any]]:
    """
    Serialize multiple DSIS models to list of dictionaries.

    Args:
        models: List of DSIS model instances to serialize
        exclude_none: Whether to exclude None values
        by_alias: Whether to use field aliases

    Returns:
        List of dictionary representations
    """
    return [
        model.to_dict(exclude_none=exclude_none, by_alias=by_alias)
        for model in models
    ]


def deserialize_multiple_from_json(
    json_str: str,
    model_class: Type['BaseModel']
) -> List['BaseModel']:
    """
    Deserialize JSON array string to list of DSIS model instances.

    Args:
        json_str: JSON array string to deserialize
        model_class: DSIS model class to deserialize to

    Returns:
        List of DSIS model instances
    """
    data_list = json.loads(json_str)
    return [model_class.from_dict(data) for data in data_list]


def deserialize_multiple_from_dict(
    data_list: List[Dict[str, Any]],
    model_class: Type['BaseModel']
) -> List['BaseModel']:
    """
    Deserialize list of dictionaries to list of DSIS model instances.
    
    Args:
        data_list: List of dictionaries to deserialize
        model_class: DSIS model class to deserialize to
        
    Returns:
        List of DSIS model instances
    """
    return [model_class.from_dict(data) for data in data_list]


def _json_serializer(obj: Any) -> Any:
    """
    Custom JSON serializer for special types.
    
    Args:
        obj: Object to serialize
        
    Returns:
        JSON-serializable representation
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, bytes):
        # Encode bytes as base64 string
        import base64
        return base64.b64encode(obj).decode('utf-8')
    else:
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def convert_to_json_compatible(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert a dictionary to be JSON-compatible by handling special types.
    
    Args:
        data: Dictionary to convert
        
    Returns:
        JSON-compatible dictionary
    """
    converted = {}
    for key, value in data.items():
        if isinstance(value, datetime):
            converted[key] = value.isoformat()
        elif isinstance(value, date):
            converted[key] = value.isoformat()
        elif isinstance(value, Decimal):
            converted[key] = float(value)
        elif isinstance(value, bytes):
            import base64
            converted[key] = base64.b64encode(value).decode('utf-8')
        elif isinstance(value, dict):
            converted[key] = convert_to_json_compatible(value)
        elif isinstance(value, list):
            converted[key] = [
                convert_to_json_compatible(item) if isinstance(item, dict) else item
                for item in value
            ]
        else:
            converted[key] = value
    
    return converted
