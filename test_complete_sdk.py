#!/usr/bin/env python3
"""
Complete SDK Test Script

Tests both Common and Native model groups to ensure they work correctly together.
"""

import sys
import json
from datetime import datetime
from typing import Dict, Any

# Add paths for imports
sys.path.insert(0, '.')
sys.path.insert(0, 'dsis_model_sdk')

def test_common_models():
    """Test Common Models (OpenWorks Common Model)"""
    print("🧪 Testing Common Models...")
    
    from models.common import Well, Company, Wellbore, Basin
    
    # Create instances
    company = Company(
        native_uid="company_001",
        company_name="Test Oil Company",
        company_type="Operator"
    )
    
    well = Well(
        native_uid="well_001", 
        well_name="Test Well #1",
        operator_company_uid="company_001"
    )
    
    wellbore = Wellbore(
        native_uid="wellbore_001",
        wellbore_name="Test Wellbore #1",
        well_uid="well_001"
    )
    
    basin = Basin(
        native_uid="basin_001",
        basin_name="Test Basin"
    )
    
    # Test serialization
    models = {
        "Company": company,
        "Well": well, 
        "Wellbore": wellbore,
        "Basin": basin
    }
    
    for name, model in models.items():
        json_data = model.to_json()
        dict_data = model.to_dict()
        
        print(f"  ✅ {name}: {model.native_uid} - JSON: {len(json_data)} chars, Dict: {len(dict_data)} fields")
        print(f"     Schema: {model.get_schema_title()}")
    
    return models

def test_native_models():
    """Test Native Models (OW5000 Native Model)"""
    print("\n🧪 Testing Native Models...")
    
    from models.native import Well, Activity, Basin, RCompany, ProcedureParams

    # Create instances
    company = RCompany(
        native_uid="native_company_001",
        company_name="Native Oil Company"
    )
    
    well = Well(
        native_uid="native_well_001",
        well_name="Native Test Well #1"
    )
    
    activity = Activity(
        native_uid="activity_001",
        activity_name="Drilling Activity"
    )
    
    basin = Basin(
        native_uid="native_basin_001", 
        basin_name="Native Test Basin"
    )
    
    # Test reserved keyword handling
    proc_params = ProcedureParams(
        ProcedureName="test_procedure",
        Optional_field=1  # This field was renamed from 'Optional' to avoid conflict
    )
    
    # Test serialization
    models = {
        "RCompany": company,
        "Well": well,
        "Activity": activity,
        "Basin": basin,
        "ProcedureParams": proc_params
    }
    
    for name, model in models.items():
        json_data = model.to_json()
        dict_data = model.to_dict()

        # Handle models that may not have native_uid
        uid = getattr(model, 'native_uid', getattr(model, 'ProcedureName', 'N/A'))

        print(f"  ✅ {name}: {uid} - JSON: {len(json_data)} chars, Dict: {len(dict_data)} fields")
        print(f"     Schema: {model.get_schema_title()}")
    
    return models

def test_model_interoperability():
    """Test that both model groups can work together"""
    print("\n🧪 Testing Model Interoperability...")
    
    from models.common import Well as CommonWell
    from models.native import Well as NativeWell
    
    # Create wells from both groups
    common_well = CommonWell(
        native_uid="common_well_001",
        well_name="Common Well"
    )
    
    native_well = NativeWell(
        native_uid="native_well_001", 
        well_name="Native Well"
    )
    
    # Test that they can coexist
    wells = [common_well, native_well]
    
    print(f"  ✅ Created {len(wells)} wells from different model groups:")
    for i, well in enumerate(wells, 1):
        schema_title = str(well.get_schema_title())
        model_type = "Common" if "OpenWorks" in schema_title else "Native"
        print(f"    {i}. {model_type} Well: {well.well_name} ({schema_title})")
    
    # Test JSON serialization of mixed models
    combined_data = {
        "common_well": common_well.to_dict(),
        "native_well": native_well.to_dict()
    }
    
    json_str = json.dumps(combined_data, indent=2, default=str)
    print(f"  ✅ Combined JSON serialization: {len(json_str)} chars")
    
    return combined_data

def test_model_statistics():
    """Display model statistics"""
    print("\n📊 Model Statistics:")
    
    # Import model groups
    import models.common
    import models.native
    
    # Count models in each group
    common_models = [name for name in dir(models.common) if not name.startswith('_')]
    native_models = [name for name in dir(models.native) if not name.startswith('_')]
    
    print(f"  📁 Common Models: {len(common_models)} models")
    print(f"  📁 Native Models: {len(native_models)} models") 
    print(f"  📁 Total Models: {len(common_models) + len(native_models)} models")
    
    # Show some example model names
    print(f"\n  🔍 Sample Common Models: {', '.join(common_models[:5])}...")
    print(f"  🔍 Sample Native Models: {', '.join(native_models[:5])}...")

def main():
    """Main test function"""
    print("🚀 DSIS Python SDK Complete Test")
    print("=" * 50)
    
    try:
        # Test individual model groups
        common_models = test_common_models()
        native_models = test_native_models()
        
        # Test interoperability
        combined_data = test_model_interoperability()
        
        # Show statistics
        test_model_statistics()
        
        print("\n" + "=" * 50)
        print("🎉 ALL TESTS PASSED!")
        print("✅ Common Models: Working")
        print("✅ Native Models: Working") 
        print("✅ Reserved Keywords: Fixed")
        print("✅ Interoperability: Working")
        print("✅ Serialization: Working")
        print("\n🏆 Python SDK is ready for use!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
