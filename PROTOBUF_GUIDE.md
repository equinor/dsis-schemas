# Protobuf Bulk Data Integration Guide

## Overview

The DSIS API uses **two complementary data formats**:

| Format | Use Case | Protocol | Field Types |
|--------|----------|----------|-------------|
| **Metadata** | Entity properties, relationships, statistics | OData (JSON) | Strings, numbers, dates |
| **Bulk Data** | Large arrays (horizon z-values, log curves, seismic) | Protocol Buffers (binary) | Binary field `data` |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      DSIS API (OData)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  GET /HorizonData3D('uid')                                 │
│  ├── Returns: JSON metadata                                │
│  │   ├── horizon_name: "Top_Reservoir"                     │
│  │   ├── horizon_mean: 2450.5                              │
│  │   └── data: <binary protobuf bytes>                     │
│  │                                                          │
│  └── data field contains:                                  │
│      └── Protobuf-encoded HorizonData3D message            │
│          ├── mode: FULL or SAMPLES                         │
│          ├── dimensions: rows × columns                    │
│          └── z-values: float arrays                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
         │                                   │
         ▼                                   ▼
┌──────────────────┐            ┌─────────────────────────┐
│  Pydantic Model  │            │  Protobuf Decoder       │
│  (Type Safety)   │            │  (Binary to Struct)     │
│                  │            │                         │
│  HorizonData3D   │────────────│  decode_horizon_data()  │
│  - metadata      │            │  - Parse binary         │
│  - data: bytes   │            │  - Return structured    │
└──────────────────┘            └─────────────────────────┘
         │                                   │
         └───────────────┬───────────────────┘
                         ▼
                ┌─────────────────┐
                │  Your Analysis  │
                │  - NumPy arrays │
                │  - Pandas dfs   │
                │  - Viz tools    │
                └─────────────────┘
```

## Installation

```bash
# Basic (metadata only)
pip install dsis-schemas

# With protobuf support (recommended)
pip install dsis-schemas[protobuf]

# Development
pip install dsis-schemas[protobuf,dev]
```

## Quick Start

### 1. Basic Decoding

```python
from dsis_model_sdk.models.common import HorizonData3D
from dsis_model_sdk.protobuf import decode_horizon_data

# Metadata from OData API
horizon = HorizonData3D.from_dict(api_response)

# Decode bulk data
decoded = decode_horizon_data(horizon.data)

# Access structure
print(f"Mode: {decoded.mode}")
print(f"Dimensions: {decoded.numberOfRows} × {decoded.numberOfColumns}")
```

### 2. Convert to NumPy

```python
from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy
import numpy as np

# Convert protobuf to NumPy array
array, metadata = horizon_to_numpy(decoded)

# Analyze
print(f"Shape: {array.shape}")
print(f"Valid samples: {(~np.isnan(array)).sum()}")
print(f"Depth range: {np.nanmin(array)} - {np.nanmax(array)}")
```

## Data Types & Decoders

### Horizon Data (3D Interpretation)

**Schema**: `OpenWorksCommonModel_HorizonData3D`  
**Binary field**: `data` (format: binary)  
**Protobuf**: `HorizonData3D`

```python
from dsis_model_sdk.protobuf import decode_horizon_data
from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy, horizon_samples_to_dict

# Decode
decoded = decode_horizon_data(binary_data)

# Two modes:
if decoded.mode == decoded.FULL:
    # All bins (including nulls as 1.0E37)
    array, meta = horizon_to_numpy(decoded)
    
elif decoded.mode == decoded.SAMPLES:
    # Sparse samples only
    samples = horizon_samples_to_dict(decoded)
    # [{'column': 100, 'row': 200, 'value': 2450.5}, ...]
```

**Grid Orientation**:
```python
# Check parent BinsetGrid3DGrid.grid_i_direction
if grid_i_direction == "TRACE":
    rows = grid_isize
    cols = grid_jsize
elif grid_i_direction == "LINE":
    rows = grid_jsize
    cols = grid_isize
```

### Log Curve Data

**Schema**: `OpenWorksCommonModel_LogCurve`  
**Binary field**: `data`  
**Protobuf**: `LogCurves`

```python
from dsis_model_sdk.protobuf import decode_log_curves
from dsis_model_sdk.utils.protobuf_decoders import log_curve_to_dict

# Decode
decoded = decode_log_curves(binary_data)

# Access index (depth/time)
print(f"Type: {decoded.curve_type}")  # DEPTH or TIME
print(f"Start: {decoded.index.start_index}")
print(f"Increment: {decoded.index.increment}")

# Access curves
data = log_curve_to_dict(decoded)
for curve_name, curve_data in data['curves'].items():
    print(f"{curve_name}: {curve_data['unit']}")
    values = curve_data['values']  # List of measurements
```

**Data Types**: `DOUBLE`, `FLOAT`, `INT`, `LONG`, `STRING`  
**Sample Types**: `VALUE`, `FIXEDLIST1D`, `FIXEDLIST2D`, `VARIABLELIST`

### Seismic Data

**Schema**: `OpenWorksCommonModel_SeismicDataSet3D`  
**Binary field**: `data`  
**Protobuf**: `Array3FBuf` (3D) or `Array2FBuf` (2D)

```python
from dsis_model_sdk.protobuf import decode_seismic_float_data
from dsis_model_sdk.utils.protobuf_decoders import seismic_3d_to_numpy

# Decode 3D
decoded = decode_seismic_float_data(binary_data)
array, meta = seismic_3d_to_numpy(decoded)

print(f"Shape: {array.shape}")  # (i, j, k) = (traces_i, traces_j, samples_k)
print(f"Size: {array.nbytes / 1e6:.2f} MB")

# World coordinates (if available)
if meta['header']:
    print(f"Origin: ({meta['header']['x']}, {meta['header']['y']})")
```

## API Request Patterns

### Pattern 1: Metadata Only

```python
import requests

response = requests.get(
    "https://dsis-api/odata/HorizonData3D",
    params={
        '$select': 'native_uid,horizon_name,horizon_mean',
        '$filter': "horizon_name eq 'Top_Reservoir'"
    }
)

metadata = response.json()['value'][0]
# No bulk data requested
```

### Pattern 2: Metadata + Bulk Data

```python
# Request metadata with bulk data
response = requests.get(
    "https://dsis-api/odata/HorizonData3D",
    params={
        '$filter': "horizon_name eq 'Top_Reservoir'"
    }
)

data = response.json()['value'][0]
# data['data'] contains base64-encoded protobuf (depending on API)
```

### Pattern 3: Separate Bulk Data Request

```python
# 1. Get metadata
response = requests.get(f"https://dsis-api/odata/HorizonData3D('{uid}')")
metadata = response.json()

# 2. Request bulk data separately
bulk_response = requests.get(
    f"https://dsis-api/odata/HorizonData3D('{uid}')/data/$value",
    headers={'Accept': 'application/octet-stream'}
)

binary_data = bulk_response.content
```

## Performance Tips

### 1. Request Only What You Need

```python
# Good: Select only required fields
params = {
    '$select': 'native_uid,horizon_name,horizon_mean',
    '$top': 100
}

# Avoid: Requesting all fields including bulk data
params = {}  # Returns everything including large binary fields
```

### 2. Stream Large Data

```python
import requests

# Stream large bulk data
with requests.get(url, stream=True) as response:
    chunks = []
    for chunk in response.iter_content(chunk_size=8192):
        chunks.append(chunk)
    binary_data = b''.join(chunks)
```

### 3. Cache Decoded Data

```python
from functools import lru_cache

@lru_cache(maxsize=10)
def get_decoded_horizon(native_uid: str):
    horizon = fetch_from_api(native_uid)
    return decode_horizon_data(horizon.data)
```

### 4. Use NumPy for Analysis

```python
import numpy as np

# NumPy operations are vectorized and fast
array, _ = horizon_to_numpy(decoded)

# Good: Vectorized
valid_mask = ~np.isnan(array)
mean_depth = np.mean(array[valid_mask])

# Avoid: Python loops
# mean_depth = sum(val for val in array.flat if not np.isnan(val)) / count
```

## Error Handling

```python
from dsis_model_sdk.protobuf import decode_horizon_data, PROTOBUF_AVAILABLE

# Check availability
if not PROTOBUF_AVAILABLE:
    raise ImportError("Install with: pip install dsis-schemas[protobuf]")

# Validate data exists
if not horizon.data:
    print("No bulk data available")
    return

# Handle decode errors
try:
    decoded = decode_horizon_data(horizon.data)
except Exception as e:
    print(f"Failed to decode: {e}")
    return

# Validate decoded structure
if decoded.mode == decoded.FULL and not decoded.lines:
    print("Warning: FULL mode but no line data")
```

## Advanced Usage

### Custom Processing Pipeline

```python
def process_horizon_data(horizon: HorizonData3D) -> dict:
    """Complete processing pipeline for horizon data."""
    
    # 1. Decode
    decoded = decode_horizon_data(horizon.data)
    
    # 2. Convert to NumPy
    array, metadata = horizon_to_numpy(decoded)
    
    # 3. Clean data
    valid_mask = ~np.isnan(array)
    valid_data = array[valid_mask]
    
    # 4. Statistics
    stats = {
        'count': len(valid_data),
        'coverage': len(valid_data) / array.size * 100,
        'mean': float(np.mean(valid_data)),
        'std': float(np.std(valid_data)),
        'min': float(np.min(valid_data)),
        'max': float(np.max(valid_data)),
        'p10': float(np.percentile(valid_data, 10)),
        'p50': float(np.percentile(valid_data, 50)),
        'p90': float(np.percentile(valid_data, 90)),
    }
    
    # 5. Return results
    return {
        'metadata': metadata,
        'statistics': stats,
        'array': array
    }
```

### Integration with Pandas

```python
import pandas as pd
from dsis_model_sdk.utils.protobuf_decoders import horizon_samples_to_dict

# Convert sparse samples to DataFrame
samples = horizon_samples_to_dict(decoded)
df = pd.DataFrame(samples)

print(df.head())
#    column  row    value
# 0     100  200  2450.5
# 1     101  200  2451.2
# 2     102  200  2452.1
# ...

# Statistics by region
df['region'] = pd.cut(df['column'], bins=4, labels=['W', 'WC', 'EC', 'E'])
regional_stats = df.groupby('region')['value'].describe()
```

## Troubleshooting

### Issue: Import Error

```
ImportError: protobuf module not found
```

**Solution**: Install protobuf extras
```bash
pip install dsis-schemas[protobuf]
```

### Issue: Decode Error

```
Exception: Error parsing message
```

**Solution**: Verify binary data is valid protobuf format
```python
# Check data field exists and has content
if not horizon.data or len(horizon.data) == 0:
    print("No binary data available")
```

### Issue: Wrong Array Shape

```python
# Check grid orientation in parent BinsetGrid3DGrid
grid = get_binset_grid(horizon.seismic3dsurvey_native_uid)
if grid.grid_i_direction == "TRACE":
    expected_shape = (grid.grid_isize, grid.grid_jsize)
else:
    expected_shape = (grid.grid_jsize, grid.grid_isize)
```

## References

- [Protocol Buffers Documentation](https://developers.google.com/protocol-buffers)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [OData V4 Protocol](https://www.odata.org/documentation/)
- DSIS API Documentation (internal)

## Support

For issues or questions:
- GitHub: https://github.com/equinor/dsis-schemas/issues
- Examples: `dsis_model_sdk/examples/protobuf_bulk_data.py`
