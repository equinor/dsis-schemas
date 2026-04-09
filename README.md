# DSIS Python SDK

A comprehensive Python SDK for both OpenWorks Common Model and Native Model schemas, providing type-safe data models and utilities for working with DSIS (Data Source Integration Service) data.

## Features

- 🎯 **Dual Model Support**: 1,160+ Pydantic-based models (201 Common + 959 Native)
- ✅ **Data Validation**: Automatic validation based on JSON Schema constraints
- 🔄 **Serialization**: Easy JSON/dict serialization and deserialization
- 📊 **Schema Introspection**: Utilities to explore model schemas and metadata
- 🔗 **Integration Ready**: Works seamlessly with existing OData query builders
- 🛡️ **Reserved Keyword Safe**: Handles Python reserved words with field aliases
- � **Protobuf Support**: Decode bulk data fields (horizon, log curves, seismic)
- �📝 **Well Documented**: Comprehensive documentation and examples

## Installation

### From PyPI (Recommended)

```bash
# Basic installation (metadata/OData support only)
pip install dsis-schemas

# With protobuf support for bulk data decoding
pip install dsis-schemas[protobuf]
```

### From Source

```bash
git clone https://github.com/equinor/dsis-schemas.git
cd dsis-schemas
pip install -e .
```

### Dependencies

- Python 3.9+
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

## Working with Bulk Data (Protobuf)

The DSIS API serves data in two formats:
- **Metadata**: Via OData (JSON) - entity properties, relationships, statistics
- **Bulk Data**: Via Protocol Buffers (binary) - large arrays like horizon z-values, log curves, seismic amplitudes

### Installation for Bulk Data Support

```bash
pip install dsis-schemas[protobuf]
```

### Decoding Horizon Data

```python
from dsis_model_sdk.models.common import HorizonData3D
from dsis_model_sdk.protobuf import decode_horizon_data
from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy

# Step 1: Get metadata from OData API
horizon = HorizonData3D.from_dict(odata_response)

print(f"Horizon: {horizon.horizon_name}")
print(f"Mean depth: {horizon.horizon_mean} {horizon.horizon_mean_unit}")

# Step 2: Decode binary bulk data field
if horizon.data:
    decoded = decode_horizon_data(horizon.data)
    
    # Step 3: Convert to NumPy array for analysis
    array, metadata = horizon_to_numpy(decoded)
    
    print(f"Grid shape: {array.shape}")
    print(f"Data coverage: {(~np.isnan(array)).sum() / array.size * 100:.1f}%")
    
    # Use the data
    valid_data = array[~np.isnan(array)]
    print(f"Depth range: {np.min(valid_data):.2f} - {np.max(valid_data):.2f}")
```

### Decoding Log Curve Data

```python
from dsis_model_sdk.protobuf import decode_log_curves
from dsis_model_sdk.utils.protobuf_decoders import log_curve_to_dict

# Decode log curve binary data
decoded = decode_log_curves(log_data.data)

print(f"Curve type: {'DEPTH' if decoded.curve_type == decoded.DEPTH else 'TIME'}")
print(f"Index range: {decoded.index.start_index} to {decoded.index.start_index + decoded.index.number_of_index * decoded.index.increment}")

# Convert to dict for easier access
data = log_curve_to_dict(decoded)

for curve_name, curve_data in data['curves'].items():
    print(f"Curve: {curve_name}")
    print(f"  Unit: {curve_data['unit']}")
    print(f"  Values: {len(curve_data['values'])} samples")
```

### Decoding Seismic Data

```python
from dsis_model_sdk.protobuf import decode_seismic_float_data
from dsis_model_sdk.utils.protobuf_decoders import seismic_3d_to_numpy

# Decode 3D seismic volume
decoded = decode_seismic_float_data(seismic.data)
array, metadata = seismic_3d_to_numpy(decoded)

print(f"Volume shape: {array.shape}")  # (traces_i, traces_j, samples_k)
print(f"Memory size: {array.nbytes / 1024 / 1024:.2f} MB")
print(f"Amplitude range: {np.min(array):.2f} to {np.max(array):.2f}")

# Extract a single trace
trace = array[100, 100, :]
print(f"Trace samples: {len(trace)}")
```

### Complete Workflow

```python
import requests
from dsis_model_sdk.models.common import HorizonData3D
from dsis_model_sdk.protobuf import decode_horizon_data

# 1. Query OData API for metadata
response = requests.get(
    "https://dsis-api.example.com/odata/HorizonData3D",
    params={'$filter': "horizon_name eq 'Top_Reservoir'"}
)
metadata = response.json()['value'][0]

# 2. Request bulk data (binary protobuf)
native_uid = metadata['native_uid']
bulk_response = requests.get(
    f"https://dsis-api.example.com/odata/HorizonData3D('{native_uid}')/data/$value",
    headers={'Accept': 'application/octet-stream'}
)

# 3. Create model with both metadata and bulk data
metadata['data'] = bulk_response.content
horizon = HorizonData3D.from_dict(metadata)

# 4. Decode and use bulk data
decoded = decode_horizon_data(horizon.data)
# ... process decoded data
```

### Decoding Surface Grid Data (LGCStructure)

Surface grids and tabular data are often stored as LGCStructure in DSIS. This format stores columnar data efficiently.

```python
import numpy as np
from dsis_model_sdk.protobuf import decode_lgc_structure
from dsis_model_sdk.utils.protobuf_decoders import lgc_structure_to_numpy2d

with open('surface.bin', 'rb') as f:
    binary_data = f.read()

decoded = decode_lgc_structure(binary_data) # LGCStructure_pb2.LGCStructure

# znon is the null-value marker and can be obtained form the SurfaceGrid / SurfaceGridProperties endpoints
grid_array: np.ndarray = lgc_structure_to_numpy2d(decoded, znon=-999.25, max_abs_value=1e15)

print(grid_array.shape) # (ncols, nrows)
print(grid_array.dtype) # e.g. dtype('float32')
```

### Supported Bulk Data Types

| Data Type | Protobuf Decoder | Content | Length Prefix |
|-----------|------------------|---------|---------------|
| **Horizon 3D** | `decode_horizon_data()` | Interpreted z-values on regular grid OR xyz points | Optional |
| **Log Curves** | `decode_log_curves()` | Well log measurements vs depth/time | Optional |
| **Seismic 3D** | `decode_seismic_data()` | 3D seismic amplitude volume | Optional |
| **Surface Grid** | `decode_lgc_structure()` | Interpreted z-values on regular grid | Yes |
| **Property Tables** | `decode_property_table_set()` | Property attribute tables | Optional |
| **3D Float Array** | `decode_array_3f()` | Generic 3D float arrays | Optional |
| **Fault Plane** | `decode_fault_plane()` | Fault surface geometry | No |
| **Poly Mesh** | `decode_poly_mesh()` | 3D polygon mesh data | No |
| **Fracture Network** | `decode_fracture_network()` | Fracture system geometry | No |

**Note**: Set `skip_length_prefix=True` when decoding files with varint length prefixes (common in file storage).

For more examples, see `dsis_model_sdk/examples/protobuf_bulk_data.py`.

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