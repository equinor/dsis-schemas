"""
Type Mapping Utilities

Maps JSON Schema types to Python types for code generation and validation.
"""

from typing import Any, Dict, Optional, Type, Union
from datetime import datetime, date
from decimal import Decimal


def map_json_schema_type(
    json_type: str, 
    format_type: Optional[str] = None,
    sql_type: Optional[str] = None,
    max_length: Optional[int] = None
) -> str:
    """
    Map JSON Schema type to Python type string for code generation.
    
    Args:
        json_type: JSON Schema type (string, number, integer, boolean, etc.)
        format_type: JSON Schema format (date, time, float, binary, etc.)
        sql_type: SQL type information from schema
        max_length: Maximum length constraint
        
    Returns:
        Python type string suitable for type hints
    """
    # Handle different JSON Schema types
    if json_type == "string":
        if format_type == "date":
            return "Optional[date]"
        elif format_type == "time" or format_type == "date-time":
            return "Optional[datetime]"
        elif format_type == "binary":
            return "Optional[bytes]"
        else:
            return "Optional[str]"
    
    elif json_type == "number":
        if format_type == "float":
            return "Optional[float]"
        else:
            # Use Decimal for precise numeric values
            return "Optional[Decimal]"
    
    elif json_type == "integer":
        return "Optional[int]"
    
    elif json_type == "boolean":
        return "Optional[bool]"
    
    elif json_type == "array":
        return "Optional[list]"
    
    elif json_type == "object":
        return "Optional[Dict[str, Any]]"
    
    else:
        # Default to Any for unknown types
        return "Optional[Any]"


def get_python_type(
    json_type: str,
    format_type: Optional[str] = None,
    sql_type: Optional[str] = None
) -> Type:
    """
    Get the actual Python type object for runtime use.
    
    Args:
        json_type: JSON Schema type
        format_type: JSON Schema format
        sql_type: SQL type information
        
    Returns:
        Python type object
    """
    if json_type == "string":
        if format_type == "date":
            return date
        elif format_type == "time" or format_type == "date-time":
            return datetime
        elif format_type == "binary":
            return bytes
        else:
            return str
    
    elif json_type == "number":
        if format_type == "float":
            return float
        else:
            return Decimal
    
    elif json_type == "integer":
        return int
    
    elif json_type == "boolean":
        return bool
    
    elif json_type == "array":
        return list
    
    elif json_type == "object":
        return dict
    
    else:
        return Any


def get_pydantic_field_config(
    json_type: str,
    format_type: Optional[str] = None,
    max_length: Optional[int] = None,
    multiple_of: Optional[float] = None,
    sql_type: Optional[str] = None,
    description: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate Pydantic Field configuration from JSON Schema properties.
    
    Args:
        json_type: JSON Schema type
        format_type: JSON Schema format
        max_length: Maximum length constraint
        multiple_of: Multiple of constraint for numbers
        sql_type: SQL type information
        description: Field description
        
    Returns:
        Dictionary of Pydantic Field configuration
    """
    config = {}
    
    # Add description
    if description:
        config['description'] = description
    elif sql_type:
        config['description'] = f"SQL Type: {sql_type}"
    
    # Add length constraints for strings
    if json_type == "string" and max_length:
        config['max_length'] = max_length
    
    # Add numeric constraints
    if json_type in ("number", "integer") and multiple_of:
        config['multiple_of'] = multiple_of
    
    # Add format validation
    if format_type:
        if format_type == "date":
            config['pattern'] = r'^\d{4}-\d{2}-\d{2}$'
        elif format_type == "time":
            config['pattern'] = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
    
    # Store SQL type as extra metadata
    if sql_type:
        config['json_schema_extra'] = {'sql_type': sql_type}
    
    return config


def convert_schema_name_to_class_name(schema_name: str) -> str:
    """
    Convert JSON schema name to Python class name.
    
    Args:
        schema_name: Original schema name (e.g., "OpenWorksCommonModel.Well")
        
    Returns:
        Python class name (e.g., "Well")
    """
    # Remove the OpenWorksCommonModel prefix and get the entity name
    if "." in schema_name:
        entity_name = schema_name.split(".")[-1]
    else:
        entity_name = schema_name.replace("OpenWorksCommonModel_", "")
    
    # Convert to PascalCase if needed
    if "_" in entity_name:
        parts = entity_name.split("_")
        entity_name = "".join(word.capitalize() for word in parts)
    
    return entity_name


def convert_field_name_to_python(field_name: str) -> str:
    """
    Convert JSON schema field name to Python field name.
    
    Args:
        field_name: Original field name (e.g., "well_name")
        
    Returns:
        Python field name (snake_case, same as input for most cases)
    """
    # Field names are already in snake_case, so return as-is
    # Could add validation or transformation here if needed
    return field_name
