# Protobuf Quick Reference

## Installation
```bash
pip install dsis-schemas[protobuf]
```

## Import Pattern
```python
# Models (metadata)
from dsis_model_sdk.models.common import HorizonData3D

# Protobuf decoders (bulk data)
from dsis_model_sdk.protobuf import decode_horizon_data

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
decoded = decode_seismic_float_data(seismic.data)

# To NumPy
array, meta = seismic_3d_to_numpy(decoded)
print(f"Volume: {array.shape}")
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

| Function | Input | Output |
|----------|-------|--------|
| `decode_horizon_data()` | bytes | HorizonData3D message |
| `decode_log_curves()` | bytes | LogCurves message |
| `decode_seismic_float_data()` | bytes | Array3FBuf message |
| `horizon_to_numpy()` | message | ndarray (2D) |
| `log_curve_to_dict()` | message | dict |
| `seismic_3d_to_numpy()` | message | ndarray (3D) |

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
