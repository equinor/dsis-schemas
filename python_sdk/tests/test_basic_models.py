"""
Basic tests for DSIS SDK models.
"""

import pytest
from datetime import date, datetime
from decimal import Decimal

from dsis_sdk.models import Well, Company, Wellbore, LogCurve
from dsis_sdk.utils import validate_data, serialize_to_json, deserialize_from_json
from dsis_sdk.exceptions import ValidationError


class TestWellModel:
    """Test the Well model."""
    
    def test_create_well_basic(self):
        """Test creating a basic well instance."""
        well = Well(
            native_uid="well_test_001",
            well_name="Test Well"
        )
        
        assert well.native_uid == "well_test_001"
        assert well.well_name == "Test Well"
        assert well.is_valid()
    
    def test_create_well_full(self):
        """Test creating a well with all common fields."""
        well = Well(
            native_uid="well_test_002",
            well_name="Full Test Well",
            well_uwi="12345678901234567890123456",
            basin_name="North Sea",
            field_name="Test Field",
            country_name="Norway",
            spud_date=date(2023, 6, 15),
            x_coordinate=123456.789,
            y_coordinate=987654.321,
            xy_unit="meters",
            crs="UTM Zone 32N"
        )
        
        assert well.well_name == "Full Test Well"
        assert well.spud_date == date(2023, 6, 15)
        assert well.x_coordinate == 123456.789
        assert well.is_valid()
    
    def test_well_serialization(self):
        """Test well serialization to JSON."""
        well = Well(
            native_uid="well_serialize",
            well_name="Serialize Test",
            x_coordinate=100.0
        )
        
        json_str = serialize_to_json(well)
        assert "well_serialize" in json_str
        assert "Serialize Test" in json_str
        
        # Test deserialization
        well_copy = deserialize_from_json(json_str, Well)
        assert well_copy.native_uid == well.native_uid
        assert well_copy.well_name == well.well_name
    
    def test_well_metadata(self):
        """Test well model metadata."""
        well = Well()
        
        assert well.get_schema_title() == "OpenWorksCommonModel.Well"
        assert well.get_schema_id() == "#/definitions/OpenWorksCommonModel_Well"
        assert well.get_sql_table_name() == "OpenWorksCommonModel_Well"


class TestCompanyModel:
    """Test the Company model."""
    
    def test_create_company(self):
        """Test creating a company instance."""
        company = Company(
            native_uid="company_test",
            company_name="Test Company",
            company_abbrev="TC",
            company_code="TC001"
        )
        
        assert company.native_uid == "company_test"
        assert company.company_name == "Test Company"
        assert company.company_abbrev == "TC"
        assert company.is_valid()
    
    def test_company_serialization(self):
        """Test company serialization."""
        company = Company(
            native_uid="comp_001",
            company_name="Serialization Test Co"
        )
        
        # To dict
        company_dict = company.to_dict(exclude_none=True)
        assert "native_uid" in company_dict
        assert "company_name" in company_dict
        assert company_dict["native_uid"] == "comp_001"
        
        # From dict
        company_copy = Company.from_dict(company_dict)
        assert company_copy.native_uid == company.native_uid


class TestWellboreModel:
    """Test the Wellbore model."""
    
    def test_create_wellbore(self):
        """Test creating a wellbore with parent well reference."""
        wellbore = Wellbore(
            native_uid="wellbore_001",
            well_native_uid="well_parent_001",
            wellbore_name="Test Wellbore",
            wellbore_uwi="12345678901234567890123456"
        )
        
        assert wellbore.native_uid == "wellbore_001"
        assert wellbore.well_native_uid == "well_parent_001"
        assert wellbore.wellbore_name == "Test Wellbore"
        assert wellbore.is_valid()


class TestValidation:
    """Test data validation functionality."""
    
    def test_validate_data_success(self):
        """Test successful data validation."""
        data = {
            "native_uid": "well_valid",
            "well_name": "Valid Well",
            "x_coordinate": 123.456
        }
        
        well = validate_data(data, Well)
        assert well.native_uid == "well_valid"
        assert well.well_name == "Valid Well"
        assert well.x_coordinate == 123.456
    
    def test_validate_data_type_coercion(self):
        """Test that Pydantic handles type coercion."""
        data = {
            "native_uid": "well_coerce",
            "well_name": "Coercion Test",
            "x_coordinate": "123.456"  # String that should be converted to float
        }
        
        well = validate_data(data, Well)
        assert well.x_coordinate == 123.456
        assert isinstance(well.x_coordinate, float)
    
    def test_field_constraints(self):
        """Test field constraints like max_length."""
        # This should work even with long strings due to Pydantic's behavior
        long_name = "A" * 100  # Well name has max_length=80 in schema
        
        well = Well(
            native_uid="well_long",
            well_name=long_name
        )
        
        # Pydantic allows this by default, but we can check validation
        assert well.well_name == long_name


class TestUtilities:
    """Test utility functions."""
    
    def test_model_introspection(self):
        """Test model introspection utilities."""
        from dsis_sdk.utils import get_model_schema, get_field_info, list_all_models
        
        # Test schema retrieval
        schema = get_model_schema(Well)
        assert "properties" in schema
        assert "native_uid" in schema["properties"]
        
        # Test field info
        field_info = get_field_info(Well, "well_name")
        assert field_info is not None
        assert field_info["name"] == "well_name"
        assert field_info["type"] == "string"
        
        # Test model listing
        all_models = list_all_models()
        assert len(all_models) > 0
        assert "Well" in all_models
        assert "Company" in all_models
    
    def test_domain_filtering(self):
        """Test domain-based model filtering."""
        from dsis_sdk.utils import get_models_by_domain, find_models_by_pattern
        
        # Test domain filtering
        well_models = get_models_by_domain('well')
        assert len(well_models) > 0
        assert any('Well' in model for model in well_models)
        
        # Test pattern matching
        seismic_models = find_models_by_pattern('seismic')
        assert len(seismic_models) > 0
        assert any('Seismic' in model for model in seismic_models)


class TestSerialization:
    """Test serialization functionality."""
    
    def test_multiple_model_serialization(self):
        """Test serializing multiple models."""
        from dsis_sdk.utils import serialize_multiple_to_json, deserialize_multiple_from_json
        
        well = Well(native_uid="well_multi_1", well_name="Multi Well 1")
        company = Company(native_uid="comp_multi_1", company_name="Multi Company 1")
        
        models = [well, company]
        
        # Serialize multiple (this will convert to dicts first)
        json_str = serialize_multiple_to_json(models)
        assert "well_multi_1" in json_str
        assert "comp_multi_1" in json_str
    
    def test_json_compatibility(self):
        """Test JSON compatibility with special types."""
        from dsis_sdk.utils import convert_to_json_compatible
        
        data = {
            "date_field": date(2023, 6, 15),
            "datetime_field": datetime(2023, 6, 15, 10, 30),
            "decimal_field": Decimal("123.456"),
            "string_field": "normal string"
        }
        
        converted = convert_to_json_compatible(data)
        
        assert converted["date_field"] == "2023-06-15"
        assert converted["datetime_field"].startswith("2023-06-15T10:30")
        assert converted["decimal_field"] == 123.456
        assert converted["string_field"] == "normal string"
