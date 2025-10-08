#!/usr/bin/env python3
"""
Test script to verify the Python SDK structure and functionality.
"""

import sys
from pathlib import Path

# Add python_sdk to path
sys.path.insert(0, str(Path(__file__).parent / "python_sdk"))

def test_common_models():
    """Test common models functionality."""
    print("🧪 Testing Common Models...")
    
    try:
        from models.common import Well, Company, Wellbore
        from datetime import date
        
        # Test Well creation
        well = Well(
            native_uid="test_well_001",
            well_name="Test Well",
            spud_date=date(2023, 6, 15),
            x_coordinate=123456.789,
            y_coordinate=987654.321
        )
        
        print(f"✅ Well created: {well.well_name}")
        print(f"   Native UID: {well.native_uid}")
        print(f"   Coordinates: ({well.x_coordinate}, {well.y_coordinate})")
        print(f"   Schema: {well.get_schema_title()}")
        
        # Test Company creation
        company = Company(
            native_uid="test_company_001",
            company_name="Test Company Ltd",
            company_abbrev="TCL"
        )
        
        print(f"✅ Company created: {company.company_name}")
        print(f"   Abbreviation: {company.company_abbrev}")
        
        # Test Wellbore creation
        wellbore = Wellbore(
            native_uid="test_wellbore_001",
            well_native_uid="test_well_001",
            wellbore_name="Test Wellbore"
        )
        
        print(f"✅ Wellbore created: {wellbore.wellbore_name}")
        print(f"   Parent well: {wellbore.well_native_uid}")
        
        # Test serialization
        well_json = well.to_json(exclude_none=True, indent=2)
        print(f"✅ Serialization works (JSON length: {len(well_json)} chars)")
        
        # Test validation
        if well.is_valid():
            print("✅ Validation works")
        
        return True
        
    except Exception as e:
        print(f"❌ Common models test failed: {e}")
        return False

def test_sdk_structure():
    """Test SDK directory structure."""
    print("🧪 Testing SDK Structure...")
    
    try:
        from models import common
        print("✅ Common models module imported")
        
        # Check if we can list models
        from models.common import BaseModel
        print("✅ BaseModel imported")
        
        # Test model count
        import models.common as common_module
        model_count = len([attr for attr in dir(common_module) 
                          if not attr.startswith('_') and attr != 'BaseModel'])
        print(f"✅ Found {model_count} common models")
        
        return True
        
    except Exception as e:
        print(f"❌ SDK structure test failed: {e}")
        return False

def test_utilities():
    """Test utility functions."""
    print("🧪 Testing Utilities...")
    
    try:
        from utils import validation, serialization
        print("✅ Utility modules imported")
        
        # Test validation
        from models.common import Well
        test_data = {
            "native_uid": "util_test_well",
            "well_name": "Utility Test Well"
        }
        
        validated_well = validation.validate_data(test_data, Well)
        print(f"✅ Validation utility works: {validated_well.well_name}")
        
        # Test serialization
        json_str = serialization.serialize_to_json(validated_well)
        print(f"✅ Serialization utility works (JSON length: {len(json_str)} chars)")
        
        return True
        
    except Exception as e:
        print(f"❌ Utilities test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing Python SDK Structure and Functionality\n")
    
    tests = [
        ("SDK Structure", test_sdk_structure),
        ("Common Models", test_common_models),
        ("Utilities", test_utilities)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running {test_name} Test")
        print('='*50)
        
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print('='*50)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("🎉 All tests passed! SDK is ready for use.")
        print("\nNext steps:")
        print("1. Add your native model schemas to 'native-model-json-schemas/'")
        print("2. Run: python3 generate_sdk.py native")
        print("3. Test native models with similar approach")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
