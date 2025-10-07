#!/usr/bin/env python3
"""
DSIS SDK Basic Usage Examples

This script demonstrates basic usage of the DSIS Python SDK for working with
OpenWorks Common Model data.
"""

import sys
import os
from datetime import date, datetime
from decimal import Decimal

# Add the parent directory to the path so we can import dsis_sdk
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dsis_sdk.models import Well, Company, Wellbore, LogCurve
from dsis_sdk.utils import validate_data, serialize_to_json, deserialize_from_json
from dsis_sdk.exceptions import ValidationError


def example_create_well():
    """Example: Creating a Well model instance."""
    print("🔧 Creating a Well instance...")
    
    well = Well(
        native_uid="well_12345",
        well_name="Test Well A-1",
        well_uwi="12345678901234567890123456",
        basin_name="North Sea",
        field_name="Troll Field",
        country_name="Norway",
        spud_date=date(2023, 6, 15),
        x_coordinate=123456.789,
        y_coordinate=987654.321,
        xy_unit="meters",
        crs="UTM Zone 32N"
    )
    
    print(f"✅ Created well: {well}")
    print(f"   Schema: {well.get_schema_title()}")
    print(f"   SQL Table: {well.get_sql_table_name()}")
    
    return well


def example_create_company():
    """Example: Creating a Company model instance."""
    print("\n🏢 Creating a Company instance...")
    
    company = Company(
        native_uid="company_equinor",
        company_name="Equinor ASA",
        company_abbrev="EQNR",
        company_code="EQN001"
    )
    
    print(f"✅ Created company: {company}")
    return company


def example_serialization(well: Well):
    """Example: Serializing models to JSON and dict."""
    print("\n📄 Serialization examples...")
    
    # Serialize to JSON
    json_str = serialize_to_json(well, indent=2)
    print("JSON representation:")
    print(json_str[:200] + "..." if len(json_str) > 200 else json_str)
    
    # Serialize to dictionary
    well_dict = well.to_dict(exclude_none=True)
    print(f"\nDictionary keys: {list(well_dict.keys())[:5]}...")
    
    return json_str, well_dict


def example_deserialization(json_str: str):
    """Example: Deserializing from JSON."""
    print("\n🔄 Deserialization example...")
    
    try:
        # Deserialize from JSON
        well_from_json = deserialize_from_json(json_str, Well)
        print(f"✅ Deserialized well: {well_from_json.well_name}")
        
        return well_from_json
    except ValidationError as e:
        print(f"❌ Validation error: {e}")
        return None


def example_validation():
    """Example: Data validation."""
    print("\n✅ Validation examples...")
    
    # Valid data
    valid_data = {
        "native_uid": "well_valid",
        "well_name": "Valid Well",
        "x_coordinate": 123.456
    }
    
    try:
        valid_well = validate_data(valid_data, Well)
        print(f"✅ Valid data created well: {valid_well.well_name}")
    except ValidationError as e:
        print(f"❌ Validation failed: {e}")
    
    # Invalid data (string for numeric field)
    invalid_data = {
        "native_uid": "well_invalid",
        "well_name": "Invalid Well",
        "x_coordinate": "not_a_number"  # This should cause validation error
    }
    
    try:
        invalid_well = validate_data(invalid_data, Well)
        print(f"✅ Invalid data somehow created well: {invalid_well.well_name}")
    except ValidationError as e:
        print(f"❌ Expected validation error: {e.errors[0] if e.errors else str(e)}")


def example_field_constraints():
    """Example: Field constraints and validation."""
    print("\n📏 Field constraints example...")
    
    # Test max length constraint
    long_name = "A" * 100  # Well name has max_length=80
    
    well_with_long_name = Well(
        native_uid="well_long_name",
        well_name=long_name
    )
    
    # Check if validation catches the constraint
    if well_with_long_name.is_valid():
        print("✅ Well with long name is valid (Pydantic allows it)")
    else:
        print(f"❌ Well with long name failed validation: {well_with_long_name.get_validation_errors()}")


def example_model_metadata():
    """Example: Accessing model metadata."""
    print("\n📋 Model metadata example...")
    
    from dsis_sdk.utils import get_model_schema, get_field_info, list_all_models
    
    # Get schema information
    well_schema = get_model_schema(Well)
    print(f"Well schema has {len(well_schema.get('properties', {}))} properties")
    
    # Get field information
    field_info = get_field_info(Well, 'well_name')
    if field_info:
        print(f"Field 'well_name': type={field_info['type']}, max_length={field_info['max_length']}")
    
    # List some models
    all_models = list_all_models()
    print(f"Total models available: {len(all_models)}")
    print(f"First 10 models: {all_models[:10]}")


def example_working_with_relationships():
    """Example: Working with related models."""
    print("\n🔗 Relationship example...")
    
    # Create a well and related wellbore
    well = Well(
        native_uid="well_parent",
        well_name="Parent Well",
        field_name="Test Field"
    )
    
    wellbore = Wellbore(
        native_uid="wellbore_child",
        well_native_uid="well_parent",  # Reference to parent well
        wellbore_name="Child Wellbore A",
        wellbore_uwi="12345678901234567890123456"
    )
    
    print(f"✅ Created well: {well.well_name}")
    print(f"✅ Created wellbore: {wellbore.wellbore_name} (parent: {wellbore.well_native_uid})")


def main():
    """Run all examples."""
    print("🚀 DSIS SDK Basic Usage Examples")
    print("=" * 50)
    
    try:
        # Basic model creation
        well = example_create_well()
        company = example_create_company()
        
        # Serialization/deserialization
        json_str, well_dict = example_serialization(well)
        deserialized_well = example_deserialization(json_str)
        
        # Validation
        example_validation()
        
        # Field constraints
        example_field_constraints()
        
        # Model metadata
        example_model_metadata()
        
        # Relationships
        example_working_with_relationships()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
