#!/usr/bin/env python3
"""
DSIS SDK Generator

Generates Python SDK from OpenWorks Common Model JSON schemas.
Creates Pydantic models with proper type hints, validation, and documentation.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import re
from datetime import datetime


class DSISSDKGenerator:
    """Generator for DSIS Python SDK from JSON schemas."""

    def __init__(self, schemas_dir: str = "common-model-json-schemas", output_dir: str = "python_sdk", model_group: str = "common"):
        self.schemas_dir = Path(schemas_dir)
        self.output_dir = Path(output_dir)
        self.model_group = model_group
        self.models_dir = self.output_dir / "models" / model_group
        self.generated_models = []
        
    def generate_sdk(self):
        """Generate the complete SDK."""
        print(f"🚀 Starting DSIS SDK generation for {self.model_group} models...")

        # Create output directories
        self._create_directories()

        # Load all schemas
        schemas = self._load_schemas()
        print(f"📋 Loaded {len(schemas)} schemas")

        # Generate model classes
        self._generate_models(schemas)

        # Update __init__.py files with imports
        self._update_init_files()

        print(f"✅ SDK generation complete! Generated {len(self.generated_models)} {self.model_group} models")
        print(f"📁 Output directory: {self.models_dir}")
        
    def _create_directories(self):
        """Create necessary directories."""
        self.models_dir.mkdir(parents=True, exist_ok=True)

        # Create __init__.py for the model group
        group_init_file = self.models_dir / "__init__.py"
        if not group_init_file.exists():
            with open(group_init_file, 'w', encoding='utf-8') as f:
                f.write(f'"""{self.model_group.title()} Models"""\n')

        # Create base.py if it doesn't exist
        base_file = self.models_dir / "base.py"
        if not base_file.exists():
            self._create_base_model_file()
        
    def _load_schemas(self) -> Dict[str, Dict[str, Any]]:
        """Load all JSON schemas."""
        schemas = {}
        
        # Try to load from combined file first
        combined_file = self.schemas_dir / "all_schemas.json"
        if combined_file.exists():
            print("📖 Loading from combined schema file...")
            with open(combined_file, 'r', encoding='utf-8') as f:
                schemas = json.load(f)
        else:
            # Load individual schema files
            print("📖 Loading individual schema files...")
            for schema_file in self.schemas_dir.glob("*.json"):
                if schema_file.name == "all_schemas.json":
                    continue
                    
                with open(schema_file, 'r', encoding='utf-8') as f:
                    schema_data = json.load(f)
                    schema_name = schema_data.get('title', schema_file.stem)
                    schemas[schema_name] = schema_data
        
        return schemas
    
    def _generate_models(self, schemas: Dict[str, Dict[str, Any]]):
        """Generate Python model classes from schemas."""
        for schema_name, schema_data in schemas.items():
            try:
                self._generate_single_model(schema_name, schema_data)
            except Exception as e:
                print(f"⚠️  Warning: Failed to generate model for {schema_name}: {e}")
    
    def _generate_single_model(self, schema_name: str, schema_data: Dict[str, Any]):
        """Generate a single Python model class."""
        class_name = self._convert_schema_name_to_class_name(schema_name)
        file_name = self._convert_class_name_to_file_name(class_name)
        
        # Generate the Python code
        code = self._generate_model_code(class_name, schema_name, schema_data)
        
        # Write to file
        output_file = self.models_dir / f"{file_name}.py"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(code)
        
        self.generated_models.append({
            'class_name': class_name,
            'file_name': file_name,
            'schema_name': schema_name
        })
        
        print(f"✨ Generated {class_name} -> {file_name}.py")
    
    def _generate_model_code(self, class_name: str, schema_name: str, schema_data: Dict[str, Any]) -> str:
        """Generate Python code for a model class."""
        imports = self._generate_imports(schema_data)
        class_code = self._generate_class_definition(class_name, schema_name, schema_data)
        
        return f'''"""
{class_name} Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: {schema_name}
Generated on: {datetime.now().isoformat()}
"""

{imports}

{class_code}
'''
    
    def _generate_imports(self, schema_data: Dict[str, Any]) -> str:
        """Generate import statements based on schema requirements."""
        imports = [
            "from typing import Optional, Dict, Any",
            "from datetime import datetime, date",
            "from decimal import Decimal",
            "from pydantic import Field",
            "from .base import BaseModel"
        ]
        
        # Check if we need additional imports based on field types
        properties = schema_data.get('properties', {})
        
        # Check for date/time fields
        has_date = any(
            prop.get('format') == 'date' 
            for prop in properties.values() 
            if isinstance(prop, dict)
        )
        has_datetime = any(
            prop.get('format') in ('time', 'date-time') 
            for prop in properties.values() 
            if isinstance(prop, dict)
        )
        
        # Check for binary fields
        has_binary = any(
            prop.get('format') == 'binary' 
            for prop in properties.values() 
            if isinstance(prop, dict)
        )
        
        return '\n'.join(imports)
    
    def _generate_class_definition(self, class_name: str, schema_name: str, schema_data: Dict[str, Any]) -> str:
        """Generate the class definition."""
        properties = schema_data.get('properties', {})
        schema_id = schema_data.get('$id', '')
        required_fields = schema_data.get('required', [])

        # Generate field definitions
        fields = []
        for field_name, field_schema in properties.items():
            is_required = field_name in required_fields
            field_def = self._generate_field_definition(field_name, field_schema, is_required)
            fields.append(field_def)

        fields_code = '\n    '.join(fields) if fields else '    pass'

        return f'''class {class_name}(BaseModel):
    """
    {schema_name} model.

    Represents data from the {schema_name} schema.
    """

    # Schema metadata
    _schema_title = "{schema_name}"
    _schema_id = "{schema_id}"
    _sql_table_name = "{schema_name.replace('.', '_')}"

    # Model fields
    {fields_code}'''
    
    def _generate_field_definition(self, field_name: str, field_schema: Dict[str, Any], is_required: bool = False) -> str:
        """Generate a field definition."""
        # Handle reserved Python keywords and built-in names
        safe_field_name = self._make_field_name_safe(field_name)

        python_type = self._map_json_schema_type(field_schema, is_required)
        field_config = self._generate_field_config(field_schema, is_required)

        # Add alias if field name was changed
        if safe_field_name != field_name:
            if field_config:
                field_config += f', alias="{field_name}"'
            else:
                field_config = f'alias="{field_name}"'

        if field_config:
            return f"{safe_field_name}: {python_type} = Field({field_config})"
        else:
            # For required fields without config, no default value
            if is_required:
                return f"{safe_field_name}: {python_type}"
            else:
                return f"{safe_field_name}: {python_type} = None"

    def _make_field_name_safe(self, field_name: str) -> str:
        """Make field name safe by avoiding Python reserved words and built-ins."""
        # List of Python reserved keywords and common built-ins that cause conflicts
        reserved_words = {
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
            'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
            'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with',
            'yield', 'None', 'True', 'False', 'type', 'object', 'str', 'int', 'float', 'bool',
            'list', 'dict', 'tuple', 'set', 'frozenset', 'bytes', 'bytearray', 'memoryview',
            'range', 'enumerate', 'zip', 'map', 'filter', 'sorted', 'reversed', 'sum', 'min',
            'max', 'abs', 'round', 'len', 'hash', 'id', 'repr', 'ascii', 'ord', 'chr', 'bin',
            'oct', 'hex', 'divmod', 'pow', 'callable', 'isinstance', 'issubclass', 'hasattr',
            'getattr', 'setattr', 'delattr', 'dir', 'vars', 'locals', 'globals', 'eval', 'exec',
            'compile', 'open', 'input', 'format', 'property', 'staticmethod', 'classmethod',
            'super', 'iter', 'next', 'slice', 'complex', 'Optional', 'Union', 'List', 'Dict',
            'Tuple', 'Set', 'FrozenSet', 'Any', 'Callable', 'Type', 'TypeVar', 'Generic',
            'Field', 'BaseModel'
        }

        if field_name in reserved_words:
            return f"{field_name}_field"

        return field_name
    
    def _map_json_schema_type(self, field_schema: Dict[str, Any], is_required: bool = False) -> str:
        """Map JSON schema type to Python type string."""
        json_type = field_schema.get('type', 'string')
        format_type = field_schema.get('format')

        # Determine the base type
        if json_type == "string":
            if format_type == "date":
                base_type = "date"
            elif format_type in ("time", "date-time"):
                base_type = "datetime"
            elif format_type == "binary":
                base_type = "bytes"
            else:
                base_type = "str"
        elif json_type == "number":
            if format_type == "float":
                base_type = "float"
            else:
                base_type = "Decimal"
        elif json_type == "integer":
            base_type = "int"
        elif json_type == "boolean":
            base_type = "bool"
        elif json_type == "array":
            base_type = "list"
        elif json_type == "object":
            base_type = "Dict[str, Any]"
        else:
            base_type = "Any"

        # Wrap in Optional if not required
        if is_required:
            return base_type
        else:
            return f"Optional[{base_type}]"
    
    def _generate_field_config(self, field_schema: Dict[str, Any], is_required: bool = False) -> str:
        """Generate Pydantic Field configuration."""
        config_parts = []

        # Add default value only for optional fields
        if not is_required:
            config_parts.append("default=None")

        # Add description
        sql_type = field_schema.get('sqlType', '')
        if sql_type:
            description = f"SQL Type: {sql_type}"
            config_parts.append(f'description="{description}"')

        # Add constraints based on field type
        json_type = field_schema.get('type', 'string')
        format_type = field_schema.get('format')

        # Only add max_length for string fields (not date/time fields)
        max_length = field_schema.get('maxLength')
        if max_length and json_type == 'string' and format_type not in ('date', 'time', 'date-time'):
            config_parts.append(f"max_length={max_length}")

        # Add numeric constraints
        multiple_of = field_schema.get('multipleOf')
        if multiple_of and json_type in ('number', 'integer'):
            config_parts.append(f"multiple_of={multiple_of}")

        return ', '.join(config_parts) if config_parts else ""
    
    def _convert_schema_name_to_class_name(self, schema_name: str) -> str:
        """Convert schema name to Python class name."""
        if "." in schema_name:
            entity_name = schema_name.split(".")[-1]
        else:
            # Handle different schema naming patterns
            if self.model_group == "common":
                entity_name = schema_name.replace("OpenWorksCommonModel_", "")
            elif self.model_group == "native":
                # Remove common prefixes for native models
                entity_name = schema_name.replace("NativeModel_", "").replace("Native_", "")
            else:
                entity_name = schema_name

        # Convert to PascalCase
        if "_" in entity_name:
            parts = entity_name.split("_")
            entity_name = "".join(word.capitalize() for word in parts)

        # Ensure class name starts with uppercase (PascalCase)
        if entity_name and entity_name[0].islower():
            entity_name = entity_name[0].upper() + entity_name[1:]

        return entity_name
    
    def _convert_class_name_to_file_name(self, class_name: str) -> str:
        """Convert class name to file name."""
        # Convert PascalCase to snake_case
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', class_name)
        result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

        # Fix specific patterns for 2D/3D naming
        result = re.sub(r'(\d)_?d_', r'_\1d_', result)  # Fix "3_d_" to "_3d_"
        result = re.sub(r'^(\d)_?d_', r'\1d_', result)   # Fix "3_d_" at start to "3d_"

        return result
    
    def _update_init_files(self):
        """Update __init__.py files with generated model imports."""
        # Generate imports for models/{group}/__init__.py
        model_imports = []
        model_names = []

        for model in self.generated_models:
            class_name = model['class_name']
            file_name = model['file_name']
            model_imports.append(f"from .{file_name} import {class_name}")
            model_names.append(f'"{class_name}"')

        # Update models/{group}/__init__.py
        init_content = f'''"""
DSIS SDK {self.model_group.title()} Models

Auto-generated model imports for all {self.model_group} entities.
Generated on: {datetime.now().isoformat()}
"""

from .base import BaseModel

# Generated model imports
{chr(10).join(model_imports)}

__all__ = [
    "BaseModel",
    {', '.join(model_names)}
]
'''

        with open(self.models_dir / "__init__.py", 'w', encoding='utf-8') as f:
            f.write(init_content)

        print(f"📝 Updated models/{self.model_group}/__init__.py with {len(self.generated_models)} model imports")

        # Update main models/__init__.py to include the group
        self._update_main_models_init()

    def _update_main_models_init(self):
        """Update the main models/__init__.py to include all model groups."""
        main_models_dir = self.output_dir / "models"
        main_init_file = main_models_dir / "__init__.py"

        # Check what model groups exist
        model_groups = []
        for item in main_models_dir.iterdir():
            if item.is_dir() and not item.name.startswith('__'):
                model_groups.append(item.name)

        # Generate imports for each group
        group_imports = []
        for group in sorted(model_groups):
            group_imports.append(f"from . import {group}")

        content = f'''"""
DSIS SDK Models

This package contains all model groups for the DSIS SDK.
Available model groups: {', '.join(sorted(model_groups))}
"""

{chr(10).join(group_imports)}

__all__ = {sorted(model_groups)}
'''

        with open(main_init_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"📝 Updated main models/__init__.py with {len(model_groups)} model groups")

    def _create_base_model_file(self):
        """Create the base model file."""
        base_content = '''"""
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
'''

        base_file = self.models_dir / "base.py"
        with open(base_file, 'w', encoding='utf-8') as f:
            f.write(base_content)

        print("📝 Created base.py model file")


def generate_common_models():
    """Generate Common Model SDK (OpenWorks)."""
    generator = DSISSDKGenerator(
        schemas_dir="common-model-json-schemas",
        output_dir="python_sdk",
        model_group="common"
    )
    generator.generate_sdk()

def generate_native_models():
    """Generate Native Model SDK."""
    generator = DSISSDKGenerator(
        schemas_dir="native-model-json-schemas",  # Adjust path as needed
        output_dir="python_sdk",
        model_group="native"
    )
    generator.generate_sdk()

def generate_all_models():
    """Generate all model groups."""
    print("🚀 Generating all Python SDK model groups...")
    generate_common_models()
    generate_native_models()
    print("✅ All model groups generated successfully!")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "common":
            generate_common_models()
        elif command == "native":
            generate_native_models()
        elif command == "all":
            generate_all_models()
        else:
            print("Usage: python generate_sdk.py [common|native|all]")
            print("  common - Generate Common Model (OpenWorks) only")
            print("  native - Generate Native Model only")
            print("  all    - Generate all model groups")
            sys.exit(1)
    else:
        # Default: generate Common models for backward compatibility
        generate_common_models()
