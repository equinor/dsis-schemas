# DSIS Python SDK

A comprehensive Python SDK for both OpenWorks Common Model and Native Model schemas, providing type-safe data models and utilities for working with DSIS (Data Source Integration Service) data.

## Features

- 🎯 **Dual Model Support**: 1,160+ Pydantic-based models (201 Common + 959 Native)
- ✅ **Data Validation**: Automatic validation based on JSON Schema constraints
- 🔄 **Serialization**: Easy JSON/dict serialization and deserialization
- 📊 **Schema Introspection**: Utilities to explore model schemas and metadata
- 🔗 **Integration Ready**: Works seamlessly with existing OData query builders
- 🛡️ **Reserved Keyword Safe**: Handles Python reserved words with field aliases
- 📝 **Well Documented**: Comprehensive documentation and examples

## Installation

### From PyPI (Recommended)

```bash
pip install dsis-schemas
```

### From Source

```bash
git clone https://github.com/equinor/dsis-schemas.git
cd dsis-schemas
pip install -e .
```

### Dependencies

- Python 3.8+
- Pydantic 2.0+
- typing-extensions 4.0+

## Quick Start

### Common Models (OpenWorks Common Model)

```python
from dsis_model_sdk.models.common import Well, Company, Wellbore

# Create a company
company = Company(
    native_uid="company_001",
    company_name="Equinor ASA",
    company_type="Operator"
)

# Create a well
well = Well(
    native_uid="well_001",
    well_name="Troll A-1",
    operator_company_uid="company_001"
)

# Serialize to JSON
well_json = well.to_json()
print(well_json)
```

### Native Models (OW5000 Native Model)

```python
from dsis_model_sdk.models.native import Well, Activity, Basin, RCompany

# Create native models
company = RCompany(
    native_uid="native_company_001",
    company_name="Native Oil Company"
)

well = Well(
    native_uid="native_well_001",
    well_name="Native Test Well"
)

activity = Activity(
    native_uid="activity_001",
    activity_name="Drilling Activity"
)

# Both model groups work together
print(f"Native Well Schema: {well.get_schema_title()}")
print(f"Activity Schema: {activity.get_schema_title()}")
```

## Available Models

The SDK includes 201 models covering all OpenWorks Common Model entities:

### Well & Drilling
- `Well`, `Wellbore`, `WellLog`, `LogCurve`
- `Casing`, `Liner`, `Packer`, `WellPlan`
- `DirectionalSurvey`, `WellTest`, `WellPerforation`

### Seismic & Geophysics
- `Seismic2DSurvey`, `Seismic3DSurvey`
- `SeismicDataSet2D`, `SeismicDataSet3D`
- `Wavelet`, `SyntheticSeismic`

### Geology & Interpretation
- `Fault`, `Horizon`, `StratigraphicUnit`
- `Pick`, `GeologicalEstimatorPoint`
- `SurfaceGrid`, `Gridded3DVolume`

### Reference Data
- `RefCountry`, `RefCurrency`, `RefWellClass`
- `MeasurementUnit`, `DataDictionary`

### Projects & Planning
- `Project`, `WellPlanProject`, `ConceptPlans`
- `Target`, `Platform`, `Field`

## Usage Examples

### Basic Model Operations

```python
from dsis_model_sdk.models.common import Well

# Create with validation
well = Well(
    native_uid="well_001",
    well_name="Discovery Well",
    x_coordinate=123456.78,
    y_coordinate=987654.32
)

# Check if valid
if well.is_valid():
    print("Well data is valid!")

# Get validation errors
errors = well.get_validation_errors()
if errors:
    print(f"Validation errors: {errors}")
```

### Serialization & Deserialization

```python
from dsis_model_sdk.models.common import Company
from dsis_model_sdk.utils import serialize_to_json, deserialize_from_json

# Create and serialize
company = Company(
    native_uid="comp_001",
    company_name="Test Company"
)

# To JSON
json_str = serialize_to_json(company, indent=2)

# From JSON
company_copy = deserialize_from_json(json_str, Company)
```

### Working with Multiple Models

```python
from dsis_model_sdk.models.common import Well, Wellbore
from dsis_model_sdk.utils import serialize_multiple_to_json

# Create related models
well = Well(native_uid="well_001", well_name="Parent Well")
wellbore = Wellbore(
    native_uid="wb_001",
    well_native_uid="well_001",
    wellbore_name="Main Bore"
)

# Serialize multiple
models = [well, wellbore]
json_data = serialize_multiple_to_json(models, indent=2)
```

### Schema Introspection

```python
from dsis_model_sdk.utils import get_model_schema, get_field_info, list_all_models

# List all available models
all_models = list_all_models()
print(f"Available models: {len(all_models)}")

# Get schema information
schema = get_model_schema(Well)
print(f"Well has {len(schema['properties'])} fields")

# Get field details
field_info = get_field_info(Well, 'well_name')
print(f"Field type: {field_info['type']}")
print(f"Max length: {field_info['max_length']}")
```

### Finding Models by Domain

```python
from dsis_model_sdk.utils import get_models_by_domain, find_models_by_pattern

# Get all well-related models
well_models = get_models_by_domain('well')
print(f"Well models: {well_models}")

# Find models by pattern
seismic_models = find_models_by_pattern('seismic')
print(f"Seismic models: {seismic_models}")
```

## Integration with Existing Tools

The SDK works seamlessly with the existing OData query builder:

```python
from dsis_model_sdk.models.common import Well
from tmp.odata_query_builder import Query  # Existing query builder

# Use SDK models for type safety
well_data = Query('Well').select('native_uid', 'well_name').execute()

# Convert to SDK models
wells = [Well.from_dict(row) for row in well_data]

# Now you have type-safe, validated models
for well in wells:
    print(f"Well: {well.well_name} ({well.native_uid})")
```

## Development

### Regenerating the SDK

If the JSON schemas are updated, regenerate the SDK:

```bash
python3 generate_sdk.py
```

### Running Tests

```bash
pip install -e ".[dev]"
pytest tests/
```

### Code Quality

```bash
# Format code
black dsis_model_sdk/

# Sort imports
isort dsis_model_sdk/

# Type checking
mypy dsis_model_sdk/

# Linting
flake8 dsis_model_sdk/
```

## Schema Information

- **Total Models**: 201
- **Schema Version**: JSON Schema Draft 2020-12
- **Source**: OpenWorks Common Model
- **Field Types**: String, Number, Integer, Date, DateTime, Binary
- **Validation**: Max length, numeric constraints, format validation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run quality checks
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
- GitHub Issues: https://github.com/equinor/dsis-schemas/issues
- Documentation: See examples/ directory
- Schema Reference: See common-model-json-schemas/ directory