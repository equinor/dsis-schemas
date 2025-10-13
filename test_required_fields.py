#!/usr/bin/env python3
"""
Test script to verify required fields are properly enforced in generated models.
"""

import sys
sys.path.insert(0, '.')

from dsis_model_sdk.models.common import Basin, DataSource
from dsis_model_sdk.models.native import WellTstFlwMeas, Project
from pydantic import ValidationError


def test_common_models_required_fields():
    """Test that common models enforce required fields."""
    print("🧪 Testing Common Models - Required Fields")
    print("=" * 60)
    
    # Test Basin - should fail without required fields
    print("\n1. Testing Basin without required fields (should fail)...")
    try:
        basin = Basin()
        print("   ❌ FAILED: Basin created without required fields!")
        return False
    except ValidationError as e:
        print(f"   ✅ PASSED: Validation error as expected")
        print(f"   Missing fields: {[err['loc'][0] for err in e.errors()]}")
    
    # Test Basin - should succeed with required fields
    print("\n2. Testing Basin with required fields (should succeed)...")
    try:
        basin = Basin(
            basin_name="North Sea Basin",
            basin_id="NSB"
        )
        print(f"   ✅ PASSED: Basin created successfully")
        print(f"   Basin: {basin.basin_name} ({basin.basin_id})")
    except ValidationError as e:
        print(f"   ❌ FAILED: {e}")
        return False
    
    # Test DataSource - should fail without required fields
    print("\n3. Testing DataSource without required fields (should fail)...")
    try:
        ds = DataSource()
        print("   ❌ FAILED: DataSource created without required fields!")
        return False
    except ValidationError as e:
        print(f"   ✅ PASSED: Validation error as expected")
        print(f"   Missing fields: {[err['loc'][0] for err in e.errors()]}")
    
    # Test DataSource - should succeed with required fields
    print("\n4. Testing DataSource with required fields (should succeed)...")
    try:
        ds = DataSource(
            name="Test Data Source",
            type="Database",  # Using alias
            public_ind="Y"
        )
        print(f"   ✅ PASSED: DataSource created successfully")
        print(f"   DataSource: {ds.name} ({ds.type_field})")  # Access via field name
    except ValidationError as e:
        print(f"   ❌ FAILED: {e}")
        return False
    
    return True


def test_native_models_required_fields():
    """Test that native models enforce required fields."""
    print("\n\n🧪 Testing Native Models - Required Fields")
    print("=" * 60)
    
    # Test WellTstFlwMeas - should fail without required fields
    print("\n1. Testing WellTstFlwMeas without required fields (should fail)...")
    try:
        well_test = WellTstFlwMeas()
        print("   ❌ FAILED: WellTstFlwMeas created without required fields!")
        return False
    except ValidationError as e:
        print(f"   ✅ PASSED: Validation error as expected")
        print(f"   Missing fields: {[err['loc'][0] for err in e.errors()]}")
    
    # Test WellTstFlwMeas - should succeed with required fields
    print("\n2. Testing WellTstFlwMeas with required fields (should succeed)...")
    try:
        well_test = WellTstFlwMeas(
            wellid="WELL-001",
            test_type="DST",
            run_number="1",
            test_number="1",
            measurement_obs_no=1
        )
        print(f"   ✅ PASSED: WellTstFlwMeas created successfully")
        print(f"   Well: {well_test.wellid}, Test: {well_test.test_type}")
    except ValidationError as e:
        print(f"   ❌ FAILED: {e}")
        return False
    
    # Test Project - should fail without required fields
    print("\n3. Testing Project without required fields (should fail)...")
    try:
        project = Project()
        print("   ❌ FAILED: Project created without required fields!")
        return False
    except ValidationError as e:
        print(f"   ✅ PASSED: Validation error as expected")
        print(f"   Missing fields: {[err['loc'][0] for err in e.errors()]}")
    
    # Test Project - should succeed with required fields
    print("\n4. Testing Project with required fields (should succeed)...")
    try:
        project = Project(
            project_name="Test Project",
            project_type="Exploration"
        )
        print(f"   ✅ PASSED: Project created successfully")
        print(f"   Project: {project.project_name} ({project.project_type})")
    except ValidationError as e:
        print(f"   ❌ FAILED: {e}")
        return False
    
    return True


def test_optional_fields():
    """Test that optional fields work correctly."""
    print("\n\n🧪 Testing Optional Fields")
    print("=" * 60)
    
    print("\n1. Creating Basin with only required fields...")
    basin = Basin(
        basin_name="Test Basin",
        basin_id="TB"
    )
    print(f"   ✅ Basin created: {basin.basin_name}")
    print(f"   Optional field (basin_type): {basin.basin_type}")
    
    print("\n2. Creating Basin with optional fields...")
    basin_full = Basin(
        basin_name="Full Basin",
        basin_id="FB",
        basin_type="Sedimentary",
        basin_abbreviation="FB",
        basin_area=1000.5,
        remark="Test basin with all fields"
    )
    print(f"   ✅ Basin created: {basin_full.basin_name}")
    print(f"   Optional field (basin_type): {basin_full.basin_type}")
    print(f"   Optional field (basin_area): {basin_full.basin_area}")
    
    return True


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("TESTING REQUIRED FIELDS IN GENERATED MODELS")
    print("=" * 60)
    
    results = []
    
    # Test common models
    results.append(("Common Models", test_common_models_required_fields()))
    
    # Test native models
    results.append(("Native Models", test_native_models_required_fields()))
    
    # Test optional fields
    results.append(("Optional Fields", test_optional_fields()))
    
    # Print summary
    print("\n\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 All tests passed! Required fields are working correctly.")
        return 0
    else:
        print("\n❌ Some tests failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

