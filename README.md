# DSIS Python SDK

A comprehensive Python SDK for the OpenWorks Common Model schemas, providing type-safe data models and utilities for working with DSIS (Data Source Integration Service) data.

## Features

- 🎯 **Type-Safe Models**: 201+ Pydantic-based models with full type hints
- ✅ **Data Validation**: Automatic validation based on JSON Schema constraints
- 🔄 **Serialization**: Easy JSON/dict serialization and deserialization
- 📊 **Schema Introspection**: Utilities to explore model schemas and metadata
- 🔗 **Integration Ready**: Works seamlessly with existing OData query builders
- 📝 **Well Documented**: Comprehensive documentation and examples

## Installation

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

```python
from dsis_sdk.models import Well, Company, Wellbore
from dsis_sdk.utils import serialize_to_json, validate_data
from datetime import date

# Create a well instance
well = Well(
    native_uid="well_12345",
    well_name="Test Well A-1",
    well_uwi="12345678901234567890123456",
    basin_name="North Sea",
    field_name="Troll Field",
    country_name="Norway",
    spud_date=date(2023, 6, 15),
    x_coordinate=123456.789,
    y_coordinate=987654.321
)

# Serialize to JSON
json_data = serialize_to_json(well, indent=2)
print(json_data)

# Validate data
data = {
    "native_uid": "company_equinor",
    "company_name": "Equinor ASA",
    "company_abbrev": "EQNR"
}
company = validate_data(data, Company)
print(f"Created: {company.company_name}")
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
from dsis_sdk.models import Well

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
from dsis_sdk.models import Company
from dsis_sdk.utils import serialize_to_json, deserialize_from_json

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
from dsis_sdk.models import Well, Wellbore
from dsis_sdk.utils import serialize_multiple_to_json

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
from dsis_sdk.utils import get_model_schema, get_field_info, list_all_models

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
from dsis_sdk.utils import get_models_by_domain, find_models_by_pattern

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
from dsis_sdk.models import Well
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
black dsis_sdk/

# Sort imports
isort dsis_sdk/

# Type checking
mypy dsis_sdk/

# Linting
flake8 dsis_sdk/
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