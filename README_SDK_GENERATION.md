# Python SDK Generation for DSIS Schemas

This document explains how to use the updated `generate_sdk.py` script to generate Python SDK for both Common Models (OpenWorks) and Native Models.

## Setup

1. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Directory Structure

The SDK is now organized as follows:
```
dsis_model_sdk/
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── common/          # OpenWorks Common Model entities
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── well.py
│   │   ├── company.py
│   │   └── ... (201 models)
│   └── native/          # Native Model entities (to be generated)
│       ├── __init__.py
│       ├── base.py
│       └── ... (native models)
├── utils/
│   ├── __init__.py
│   ├── validation.py
│   ├── serialization.py
│   └── ...
└── examples/
    └── basic_usage.py
```

## Usage

### Generate Common Models (OpenWorks)
```bash
# Generate only common models
python3 generate_sdk.py common
```

### Generate Native Models
```bash
# First, ensure you have native model schemas in native-model-json-schemas/
# Then generate native models
python3 generate_sdk.py native
```

### Generate All Models
```bash
# Generate both common and native models
python3 generate_sdk.py all
```

### Command Line Options
```bash
python3 generate_sdk.py [common|native|all]
  common - Generate Common Model (OpenWorks) only
  native - Generate Native Model only  
  all    - Generate all model groups
```

## Using the Generated SDK

### Import Common Models
```python
from dsis_model_sdk.models.common import Well, Company, Wellbore

# Create a well
well = Well(
    native_uid="well_001",
    well_name="Test Well",
    x_coordinate=123.456,
    y_coordinate=789.012
)

print(f"Created well: {well.well_name}")
print(f"Schema: {well.get_schema_title()}")
```

### Import Native Models (after generation)
```python
from dsis_model_sdk.models.native import SomeNativeModel

# Use native models
native_obj = SomeNativeModel(
    # native model fields
)
```

### Import Both Model Groups
```python
from dsis_model_sdk.models import common, native

# Use common models
well = common.Well(native_uid="well_001", well_name="Test Well")

# Use native models (after generation)
# native_obj = native.SomeModel(...)
```

## Schema Requirements

### For Common Models
- Schemas should be in `common-model-json-schemas/all_schemas.json`
- Schema names typically follow pattern: `OpenWorksCommonModel.EntityName`

### For Native Models
- Schemas should be in `native-model-json-schemas/` directory
- Can be individual JSON files or combined in `all_schemas.json`
- Schema names can follow patterns like `NativeModel.EntityName` or `Native.EntityName`

## Generated Features

Each generated model includes:

1. **Pydantic v2 BaseModel** with full validation
2. **Type hints** for all fields
3. **Field constraints** (max_length, format validation, etc.)
4. **Schema metadata** access methods
5. **Serialization/deserialization** methods
6. **SQL type information** preservation

### Example Model Usage
```python
from dsis_model_sdk.models.common import Well
from datetime import date

# Create with validation
well = Well(
    native_uid="well_123",
    well_name="North Sea Well",
    spud_date=date(2023, 6, 15),
    x_coordinate=456789.12,
    y_coordinate=6789012.34
)

# Serialize to JSON
json_str = well.to_json(exclude_none=True, indent=2)

# Serialize to dict
data_dict = well.to_dict(exclude_none=True)

# Validate
if well.is_valid():
    print("Well data is valid")

# Get schema info
print(f"Schema Title: {well.get_schema_title()}")
print(f"SQL Table: {well.get_sql_table_name()}")
```

## Testing

Test the generated models:
```bash
source venv/bin/activate
python3 -c "
from dsis_model_sdk.models.common import Well, Company
well = Well(native_uid='test', well_name='Test Well')
print(f'✅ {well.well_name} created successfully')
"
```

## Next Steps

1. **Provide Native Model Schemas**: Place your native model JSON schemas in `native-model-json-schemas/`
2. **Generate Native Models**: Run `python3 generate_sdk.py native`
3. **Test Integration**: Verify both model groups work together
4. **Update Examples**: Add examples using both common and native models
