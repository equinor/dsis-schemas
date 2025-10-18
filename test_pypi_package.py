#!/usr/bin/env python3
"""
Test script for the published dsis-schemas package from PyPI.
Tests both common and native models with various operations.
"""

def test_common_models():
    """Test Common Models (OpenWorks Common Model)"""
    print("\n" + "="*60)
    print("Testing Common Models")
    print("="*60)
    
    from dsis_model_sdk.models.common import Well, Company, Wellbore, Basin
    
    # Test 1: Create a Basin (has required fields)
    print("\n1. Testing Basin with required fields...")
    try:
        basin = Basin(
            basin_name="North Sea Basin",
            basin_id="NSB"  # max_length is 3
        )
        print(f"   ✅ Basin created: {basin.basin_name} (ID: {basin.basin_id})")
    except Exception as e:
        print(f"   ❌ Failed to create Basin: {e}")
        return False
    
    # Test 2: Create a Company
    print("\n2. Testing Company creation...")
    try:
        company = Company(
            native_uid="company_001",
            company_name="Equinor ASA",
            company_type="Operator"
        )
        print(f"   ✅ Company created: {company.company_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Company: {e}")
        return False
    
    # Test 3: Create a Well
    print("\n3. Testing Well creation...")
    try:
        well = Well(
            native_uid="well_001",
            well_name="Troll A-1",
            well_uwi="NO-001",  # Required field
            operator_company_uid="company_001"
        )
        print(f"   ✅ Well created: {well.well_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Well: {e}")
        return False
    
    # Test 4: Create a Wellbore
    print("\n4. Testing Wellbore creation...")
    try:
        wellbore = Wellbore(
            native_uid="wb_001",
            well_native_uid="well_001",
            wellbore_name="Main Bore",
            wellbore_uwi="NO-001-WB"  # Required field
        )
        print(f"   ✅ Wellbore created: {wellbore.wellbore_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Wellbore: {e}")
        return False
    
    # Test 5: Serialization to dict
    print("\n5. Testing serialization to dict...")
    try:
        well_dict = well.model_dump()
        print(f"   ✅ Serialized to dict with {len(well_dict)} fields")
    except Exception as e:
        print(f"   ❌ Failed to serialize: {e}")
        return False
    
    # Test 6: Serialization to JSON
    print("\n6. Testing serialization to JSON...")
    try:
        well_json = well.model_dump_json()
        print(f"   ✅ Serialized to JSON ({len(well_json)} chars)")
    except Exception as e:
        print(f"   ❌ Failed to serialize to JSON: {e}")
        return False
    
    # Test 7: Deserialization from dict
    print("\n7. Testing deserialization from dict...")
    try:
        well_copy = Well.model_validate(well_dict)
        print(f"   ✅ Deserialized from dict: {well_copy.well_name}")
    except Exception as e:
        print(f"   ❌ Failed to deserialize: {e}")
        return False
    
    # Test 8: Schema metadata
    print("\n8. Testing schema metadata...")
    try:
        schema_title = well._schema_title
        schema_id = well._schema_id
        print(f"   ✅ Schema Title: {schema_title}")
        print(f"   ✅ Schema ID: {schema_id}")
    except Exception as e:
        print(f"   ❌ Failed to access schema metadata: {e}")
        return False
    
    print("\n✅ All Common Model tests passed!")
    return True


def test_native_models():
    """Test Native Models (OW5000 Native Model)"""
    print("\n" + "="*60)
    print("Testing Native Models")
    print("="*60)
    
    from dsis_model_sdk.models.native import Well, Activity, Project, WellTstFlwMeas
    
    # Test 1: Create a Project
    print("\n1. Testing Project creation...")
    try:
        project = Project(
            native_uid="proj_001",
            project_name="Troll Development",
            project_type="Development"  # Required field
        )
        print(f"   ✅ Project created: {project.project_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Project: {e}")
        return False
    
    # Test 2: Create a Native Well
    print("\n2. Testing Native Well creation...")
    try:
        well = Well(
            native_uid="native_well_001",
            well_name="Native Test Well",
            wellid="W001",  # Required field
            uwi="NO-W001",  # Required field
            well_location_id="LOC001"  # Required field
        )
        print(f"   ✅ Native Well created: {well.well_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Native Well: {e}")
        return False
    
    # Test 3: Create an Activity
    print("\n3. Testing Activity creation...")
    try:
        activity = Activity(
            native_uid="activity_001",
            activity_name="Drilling Activity",
            activity_id="ACT001",  # Required field
            entity_type_name="Activity"  # Required field
        )
        print(f"   ✅ Activity created: {activity.activity_name}")
    except Exception as e:
        print(f"   ❌ Failed to create Activity: {e}")
        return False
    
    # Test 4: Create WellTstFlwMeas (has required fields)
    print("\n4. Testing WellTstFlwMeas with required fields...")
    try:
        flow_meas = WellTstFlwMeas(
            native_uid="flow_001",
            well_tst_flw_meas_name="Flow Test 1",
            wellid="W001",  # Required field
            test_type="Production",  # Required field
            run_number="1",  # Required field (string)
            test_number="1",  # Required field (string)
            measurement_obs_no=1  # Required field
        )
        print(f"   ✅ WellTstFlwMeas created: {flow_meas.well_tst_flw_meas_name}")
    except Exception as e:
        print(f"   ❌ Failed to create WellTstFlwMeas: {e}")
        return False
    
    # Test 5: Serialization
    print("\n5. Testing native model serialization...")
    try:
        project_json = project.model_dump_json()
        print(f"   ✅ Serialized to JSON ({len(project_json)} chars)")
    except Exception as e:
        print(f"   ❌ Failed to serialize: {e}")
        return False
    
    # Test 6: Schema metadata
    print("\n6. Testing native model schema metadata...")
    try:
        schema_title = well._schema_title
        print(f"   ✅ Schema Title: {schema_title}")
    except Exception as e:
        print(f"   ❌ Failed to access schema metadata: {e}")
        return False
    
    print("\n✅ All Native Model tests passed!")
    return True


def test_required_fields_validation():
    """Test that required fields are properly enforced"""
    print("\n" + "="*60)
    print("Testing Required Fields Validation")
    print("="*60)
    
    from dsis_model_sdk.models.common import Basin, DataSource
    from pydantic import ValidationError
    
    # Test 1: Basin without required fields should fail
    print("\n1. Testing Basin without required fields (should fail)...")
    try:
        basin = Basin()
        print(f"   ❌ Basin created without required fields (should have failed!)")
        return False
    except ValidationError as e:
        print(f"   ✅ Correctly rejected: Missing required fields")
        print(f"      Errors: {len(e.errors())} validation errors")
    
    # Test 2: Basin with required fields should succeed
    print("\n2. Testing Basin with required fields (should succeed)...")
    try:
        basin = Basin(
            basin_name="Test Basin",
            basin_id="TB1"  # max_length is 3
        )
        print(f"   ✅ Basin created successfully with required fields")
    except ValidationError as e:
        print(f"   ❌ Failed to create Basin with required fields: {e}")
        return False
    
    # Test 3: DataSource with required fields
    print("\n3. Testing DataSource with required fields...")
    try:
        data_source = DataSource(
            data_source_name="Test Source",
            data_source_id="DS1",
            name="Test Source",  # Required field
            type="Database",  # Required field
            public_ind="Y"  # Required field (string, not bool)
        )
        print(f"   ✅ DataSource created: {data_source.data_source_name}")
    except Exception as e:
        print(f"   ❌ Failed to create DataSource: {e}")
        return False
    
    print("\n✅ All Required Fields Validation tests passed!")
    return True


def test_package_info():
    """Test package information and imports"""
    print("\n" + "="*60)
    print("Testing Package Information")
    print("="*60)
    
    # Test 1: Check package can be imported
    print("\n1. Testing package import...")
    try:
        import dsis_model_sdk
        print(f"   ✅ Package imported successfully")
    except Exception as e:
        print(f"   ❌ Failed to import package: {e}")
        return False
    
    # Test 2: Check models subpackages
    print("\n2. Testing models subpackages...")
    try:
        from dsis_model_sdk import models
        from dsis_model_sdk.models import common, native
        print(f"   ✅ Models subpackages imported successfully")
    except Exception as e:
        print(f"   ❌ Failed to import models subpackages: {e}")
        return False
    
    # Test 3: Check utils
    print("\n3. Testing utils package...")
    try:
        from dsis_model_sdk import utils
        print(f"   ✅ Utils package imported successfully")
    except Exception as e:
        print(f"   ❌ Failed to import utils: {e}")
        return False
    
    # Test 4: Count available models
    print("\n4. Counting available models...")
    try:
        from dsis_model_sdk.models import common, native
        common_models = [name for name in dir(common) if not name.startswith('_')]
        native_models = [name for name in dir(native) if not name.startswith('_')]
        print(f"   ✅ Common models: {len(common_models)}")
        print(f"   ✅ Native models: {len(native_models)}")
        print(f"   ✅ Total models: {len(common_models) + len(native_models)}")
    except Exception as e:
        print(f"   ❌ Failed to count models: {e}")
        return False
    
    print("\n✅ All Package Information tests passed!")
    return True


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("DSIS-SCHEMAS PyPI Package Test Suite")
    print("="*60)
    
    results = []
    
    # Run all test suites
    results.append(("Package Info", test_package_info()))
    results.append(("Common Models", test_common_models()))
    results.append(("Native Models", test_native_models()))
    results.append(("Required Fields", test_required_fields_validation()))
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    for test_name, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:20s}: {status}")
    
    all_passed = all(result[1] for result in results)
    
    print("\n" + "="*60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Package is working correctly.")
    else:
        print("❌ SOME TESTS FAILED! Please review the errors above.")
    print("="*60 + "\n")
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())

