"""
Base Model for DSIS SDK

Provides the foundation for all generated model classes with common functionality
including validation, serialization, and metadata access.
"""

from typing import Any, Dict, Optional, Type, Union, get_type_hints
from datetime import datetime, date
from decimal import Decimal
import json
from pydantic import BaseModel as PydanticBaseModel, Field, validator
from pydantic.config import ConfigDict


class BaseModel(PydanticBaseModel):
    """
    Base class for all DSIS Common Model entities.

    Provides common functionality including:
    - JSON Schema validation
    - Serialization/deserialization
    - SQL type metadata
    - Field validation and transformation
    """

    model_config = ConfigDict(
        # Allow extra fields for forward compatibility
        extra='allow',
        # Validate assignment to catch errors early
        validate_assignment=True,
        # Use enum values instead of enum objects in serialization
        use_enum_values=True,
        # Allow population by field name or alias
        populate_by_name=True,
        # Validate default values
        validate_default=True,
        # JSON schema generation settings
        json_schema_extra={
            "additionalProperties": True
        }
    )

    # Metadata about the schema
    _schema_title: Optional[str] = None
    _schema_id: Optional[str] = None
    _sql_table_name: Optional[str] = None

    def __init__(self, **data):
        """Initialize the model with data validation."""
        super().__init__(**data)

    @classmethod
    def get_schema_title(cls) -> Optional[str]:
        """Get the original JSON schema title."""
        return getattr(cls, '_schema_title', None)

    @classmethod
    def get_schema_id(cls) -> Optional[str]:
        """Get the original JSON schema ID."""
        return getattr(cls, '_schema_id', None)

    @classmethod
    def get_sql_table_name(cls) -> Optional[str]:
        """Get the SQL table name this model represents."""
        return getattr(cls, '_sql_table_name', None)

    def to_dict(self, exclude_none: bool = True, by_alias: bool = False) -> Dict[str, Any]:
        """
        Convert the model to a dictionary.

        Args:
            exclude_none: Whether to exclude None values
            by_alias: Whether to use field aliases instead of field names

        Returns:
            Dictionary representation of the model
        """
        return self.model_dump(
            exclude_none=exclude_none,
            by_alias=by_alias,
            mode='python'
        )

    def to_json(self, exclude_none: bool = True, by_alias: bool = False, indent: Optional[int] = None) -> str:
        """
        Convert the model to JSON string.

        Args:
            exclude_none: Whether to exclude None values
            by_alias: Whether to use field aliases instead of field names
            indent: JSON indentation level

        Returns:
            JSON string representation of the model
        """
        return self.model_dump_json(
            exclude_none=exclude_none,
            by_alias=by_alias,
            indent=indent
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseModel':
        """
        Create a model instance from a dictionary.

        Args:
            data: Dictionary containing model data

        Returns:
            Model instance
        """
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> 'BaseModel':
        """
        Create a model instance from a JSON string.

        Args:
            json_str: JSON string containing model data

        Returns:
            Model instance
        """
        return cls.model_validate_json(json_str)

    def is_valid(self) -> bool:
        """
        Check if the current model instance is valid.

        Returns:
            True if valid, False otherwise
        """
        try:
            self.model_validate(self.model_dump())
            return True
        except Exception:
            return False

    def get_validation_errors(self) -> Optional[str]:
        """
        Get validation errors for the current model instance.

        Returns:
            String describing validation errors, or None if valid
        """
        try:
            self.model_validate(self.model_dump())
            return None
        except Exception as e:
            return str(e)

    def __str__(self) -> str:
        """String representation of the model."""
        class_name = self.__class__.__name__
        if hasattr(self, 'native_uid') and self.native_uid:
            return f"{class_name}(native_uid='{self.native_uid}')"
        elif hasattr(self, 'name') and self.name:
            return f"{class_name}(name='{self.name}')"
        else:
            return f"{class_name}(...)"

    def __repr__(self) -> str:
        """Detailed representation of the model."""
        return f"{self.__class__.__name__}({self.model_dump()})"
