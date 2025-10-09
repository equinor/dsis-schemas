"""
Schema Utilities

Provides utilities for working with DSIS model schemas and metadata.
"""

from typing import Any, Dict, List, Optional, Type, get_type_hints, TYPE_CHECKING
import inspect

if TYPE_CHECKING:
    from pydantic import BaseModel


def get_model_schema(model_class: Type['BaseModel']) -> Dict[str, Any]:
    """
    Get the JSON schema for a DSIS model class.
    
    Args:
        model_class: DSIS model class
        
    Returns:
        JSON schema dictionary
    """
    return model_class.model_json_schema()


def get_field_info(model_class: Type['BaseModel'], field_name: str) -> Optional[Dict[str, Any]]:
    """
    Get information about a specific field in a DSIS model.
    
    Args:
        model_class: DSIS model class
        field_name: Name of the field
        
    Returns:
        Field information dictionary, or None if field doesn't exist
    """
    schema = get_model_schema(model_class)
    properties = schema.get('properties', {})
    
    if field_name not in properties:
        return None
    
    field_schema = properties[field_name]
    
    # Get additional info from model fields
    model_fields = model_class.model_fields
    field_info = model_fields.get(field_name)
    
    result = {
        'name': field_name,
        'type': field_schema.get('type'),
        'format': field_schema.get('format'),
        'description': field_schema.get('description'),
        'max_length': field_schema.get('maxLength'),
        'multiple_of': field_schema.get('multipleOf'),
        'required': field_name in schema.get('required', []),
    }
    
    if field_info:
        result['default'] = field_info.default
        result['annotation'] = field_info.annotation
    
    return result


def list_all_models() -> List[str]:
    """
    List all available DSIS model class names.
    
    Returns:
        List of model class names
    """
    from .. import models
    
    model_names = []
    for name in dir(models):
        obj = getattr(models, name)
        try:
            from pydantic import BaseModel as PydanticBaseModel
            if (inspect.isclass(obj) and
                issubclass(obj, PydanticBaseModel) and
                obj != PydanticBaseModel):
                model_names.append(name)
        except:
            pass

    return sorted(model_names)


def get_model_by_name(model_name: str) -> Optional[Type['BaseModel']]:
    """
    Get a DSIS model class by name.
    
    Args:
        model_name: Name of the model class
        
    Returns:
        Model class, or None if not found
    """
    from .. import models

    if hasattr(models, model_name):
        obj = getattr(models, model_name)
        try:
            from pydantic import BaseModel as PydanticBaseModel
            if inspect.isclass(obj) and issubclass(obj, PydanticBaseModel):
                return obj
        except:
            pass

    return None


def get_model_fields(model_class: Type['BaseModel']) -> Dict[str, Any]:
    """
    Get all fields for a DSIS model class.
    
    Args:
        model_class: DSIS model class
        
    Returns:
        Dictionary of field names to field information
    """
    schema = get_model_schema(model_class)
    properties = schema.get('properties', {})
    required_fields = set(schema.get('required', []))
    
    fields = {}
    for field_name, field_schema in properties.items():
        fields[field_name] = {
            'name': field_name,
            'type': field_schema.get('type'),
            'format': field_schema.get('format'),
            'description': field_schema.get('description'),
            'max_length': field_schema.get('maxLength'),
            'multiple_of': field_schema.get('multipleOf'),
            'required': field_name in required_fields,
        }
    
    return fields


def get_model_metadata(model_class: Type['BaseModel']) -> Dict[str, Any]:
    """
    Get metadata for a DSIS model class.
    
    Args:
        model_class: DSIS model class
        
    Returns:
        Dictionary of model metadata
    """
    return {
        'class_name': model_class.__name__,
        'schema_title': model_class.get_schema_title(),
        'schema_id': model_class.get_schema_id(),
        'sql_table_name': model_class.get_sql_table_name(),
        'field_count': len(get_model_fields(model_class)),
        'docstring': model_class.__doc__,
    }


def find_models_by_pattern(pattern: str) -> List[str]:
    """
    Find DSIS model classes whose names match a pattern.
    
    Args:
        pattern: Pattern to match (case-insensitive)
        
    Returns:
        List of matching model class names
    """
    all_models = list_all_models()
    pattern_lower = pattern.lower()
    
    matching_models = [
        model_name for model_name in all_models
        if pattern_lower in model_name.lower()
    ]
    
    return matching_models


def get_models_by_domain(domain: str) -> List[str]:
    """
    Get DSIS model classes by domain/category.
    
    Args:
        domain: Domain name (e.g., 'well', 'seismic', 'fault')
        
    Returns:
        List of model class names in the domain
    """
    domain_patterns = {
        'well': ['well', 'wellbore'],
        'seismic': ['seismic', 'seis'],
        'fault': ['fault'],
        'horizon': ['horizon'],
        'log': ['log'],
        'project': ['project', 'plan'],
        'reference': ['ref'],
        'geology': ['geological', 'lithology', 'stratigraphic'],
        'production': ['production'],
        'survey': ['survey'],
        'grid': ['grid'],
        'contour': ['contour'],
    }
    
    patterns = domain_patterns.get(domain.lower(), [domain.lower()])
    all_models = list_all_models()
    
    matching_models = []
    for model_name in all_models:
        model_name_lower = model_name.lower()
        if any(pattern in model_name_lower for pattern in patterns):
            matching_models.append(model_name)
    
    return matching_models


def validate_model_compatibility(model1: Type['BaseModel'], model2: Type['BaseModel']) -> Dict[str, Any]:
    """
    Check compatibility between two DSIS model classes.
    
    Args:
        model1: First model class
        model2: Second model class
        
    Returns:
        Dictionary with compatibility information
    """
    fields1 = set(get_model_fields(model1).keys())
    fields2 = set(get_model_fields(model2).keys())
    
    common_fields = fields1.intersection(fields2)
    unique_to_model1 = fields1 - fields2
    unique_to_model2 = fields2 - fields1
    
    return {
        'compatible': len(common_fields) > 0,
        'common_fields': sorted(common_fields),
        'unique_to_first': sorted(unique_to_model1),
        'unique_to_second': sorted(unique_to_model2),
        'similarity_ratio': len(common_fields) / len(fields1.union(fields2)) if fields1.union(fields2) else 0
    }
