# Protobuf Quick Reference

## Installation
```bash
pip install dsis-schemas[protobuf]
```

## Import Pattern
```python
# Models (metadata)
from dsis_model_sdk.models.common import HorizonData3D

# Core protobuf decoders (bulk data)
from dsis_model_sdk.protobuf import (
    decode_horizon_data,
    decode_log_curves,
    decode_seismic_data,
    decode_lgc_structure,
    decode_property_table_set,
)

# Array decoders
from dsis_model_sdk.protobuf import decode_array_2f, decode_array_3f

# Geometry decoders
from dsis_model_sdk.protobuf import (
    decode_fault_plane,
    decode_poly_mesh,
    decode_fracture_network,
)

# NumPy utilities (optional)
from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy
```

## Quick Examples

### Horizon Data
```python
# Decode
decoded = decode_horizon_data(horizon.data)

# To NumPy
array, meta = horizon_to_numpy(decoded)
print(f"Shape: {array.shape}")
```

### Log Curves
```python
# Decode
decoded = decode_log_curves(log_data.data)

# Access
for curve in decoded.values:
    print(f"{curve.name}: {len(curve.data_double)} samples")
```

### Seismic Data
```python
# Decode
decoded = decode_seismic_data(seismic.data)

# Access data
if decoded.data.data_float:
    print(f"Float data: {len(decoded.data.data_float)} values")
print(f"Dimensions: {decoded.length.i}x{decoded.length.j}x{decoded.length.k}")
```

### Array Data
```python
# Decode 3D float array
array_3d = decode_array_3f(binary_data)
print(f"Shape: {array_3d.length.i}x{array_3d.length.j}x{array_3d.length.k}")
print(f"Data: {len(array_3d.data)} points")
```

### Geometry Data
```python
# Decode fault plane
fault = decode_fault_plane(fault_data)
for segment in fault.faultSegment:
    print(f"Points: {len(segment.x)}")

# Decode mesh
mesh = decode_poly_mesh(mesh_data)
print(f"Mesh type: {mesh.meshset.geomType}")
```

## Data Flow
```
OData JSON → Pydantic Model → model.data (bytes)
                                    ↓
                           decode_xxx(bytes)
                                    ↓
                           Protobuf Message
                                    ↓
                           xxx_to_numpy()
                                    ↓
                              NumPy Array
```

## Decoder Functions

### Core Data Types
| Function | Input | Output |
|----------|-------|--------|
| `decode_horizon_data()` | bytes | HorizonData3D message |
| `decode_log_curves()` | bytes | LogCurves message |
| `decode_seismic_data()` | bytes | SeismicData message |
| `decode_seismic_header()` | bytes | SeismicDataHeader message |
| `decode_lgc_structure()` | bytes | LGCStructure message |
| `decode_property_table_set()` | bytes | PropertyTableSet message |

### Array Types
| Function | Input | Output |
|----------|-------|--------|
| `decode_array_2f()` | bytes | Array2FBuf message |
| `decode_array_3f()` | bytes | Array3FBuf message |

### Geometry Types
| Function | Input | Output |
|----------|-------|--------|
| `decode_fault_plane()` | bytes | FaultPlane message |
| `decode_poly_mesh()` | bytes | PolyMesh message |
| `decode_fracture_network()` | bytes | FractureNetwork message |

### Utilities (if available)
| Function | Input | Output |
|----------|-------|--------|
| `horizon_to_numpy()` | message | ndarray (2D) |
| `log_curve_to_dict()` | message | dict |

## Error Handling
```python
from dsis_model_sdk.protobuf import PROTOBUF_AVAILABLE

if not PROTOBUF_AVAILABLE:
    print("Install: pip install dsis-schemas[protobuf]")

if not horizon.data:
    print("No bulk data available")

try:
    decoded = decode_horizon_data(horizon.data)
except Exception as e:
    print(f"Decode error: {e}")
```

## Common Patterns

### Pattern 1: Full Pipeline
```python
# 1. Query API
response = requests.get(api_url)
horizon = HorizonData3D.from_dict(response.json()['value'][0])

# 2. Decode
decoded = decode_horizon_data(horizon.data)

# 3. Convert
array, _ = horizon_to_numpy(decoded)

# 4. Analyze
print(f"Mean: {np.nanmean(array)}")
```

### Pattern 2: Sparse Samples
```python
decoded = decode_horizon_data(horizon.data)

if decoded.mode == decoded.SAMPLES:
    samples = horizon_samples_to_dict(decoded)
    df = pd.DataFrame(samples)
    # Use DataFrame for analysis
```

### Pattern 3: Multiple Curves
```python
decoded = decode_log_curves(log_data.data)
data = log_curve_to_dict(decoded)

for name, curve in data['curves'].items():
    plt.plot(curve['values'], label=name)
plt.legend()
```

## File Locations

| What | Where |
|------|-------|
| Proto definitions | `protobuf-definitions/` |
| Generated modules | `dsis_model_sdk/protobuf/*_pb2.py` |
| Decoders | `dsis_model_sdk/protobuf/__init__.py` |
| Utilities | `dsis_model_sdk/utils/protobuf_decoders.py` |
| Examples | `dsis_model_sdk/examples/protobuf_bulk_data.py` |
| Full guide | `PROTOBUF_GUIDE.md` |

## Regenerate Protobuf Files
```bash
./scripts/generate_protobuf.sh
```

## See Also
- Full documentation: `PROTOBUF_GUIDE.md`
- Examples: `dsis_model_sdk/examples/protobuf_bulk_data.py`
- README section: "Working with Bulk Data (Protobuf)"
