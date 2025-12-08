# Protocol Buffer Definitions

This directory contains Protocol Buffer (.proto) definitions for DSIS bulk data formats.
These definitions are used to decode binary data fields from the DSIS API.

## Purpose

The DSIS API serves data in two formats:
- **Metadata**: OData (JSON) - entity properties, relationships, statistics
- **Bulk Data**: Protocol Buffers (binary) - large arrays encoded in binary `data` fields

These .proto files define the structure of the binary bulk data.

## Directory Structure

### Core Data Types

| File | Description | Used For |
|------|-------------|----------|
| `horizon/HorizonData3D.proto` | 3D horizon interpretation data | HorizonData3D z-values (FULL or SAMPLES mode) |
| `logcurve/LogCurves.proto` | Well log curve data | Log measurements with depth/time index |
| `seismic/SeismicData.proto` | Seismic amplitude data | 2D/3D seismic volumes |
| `seismic/SeismicDataHeader.proto` | Seismic header data (3D) | Trace headers and metadata |
| `seismic/SeismicDataHeader2D.proto` | Seismic header data (2D) | 2D seismic trace headers |
| `tabular/LGCStructure.proto` | Generic tabular data | Multi-purpose data structures |
| `tabular/PropertyTableSet.proto` | Property tables | Property metadata and values |

### Array Types

| File | Description | Data Type |
|------|-------------|-----------|
| `arrays/Array2FBuf.proto` | 2D float arrays | Float |
| `arrays/Array2FBufList.proto` | Lists of 2D float arrays | Float |
| `arrays/Array3FBuf.proto` | 3D float arrays | Float |
| `arrays/Array3FBufList.proto` | Lists of 3D float arrays | Float |
| `arrays/Array3BBuf.proto` | 3D byte arrays | Byte |
| `arrays/Array3IBuf.proto` | 3D integer arrays | Integer |
| `arrays/Array3SBuf.proto` | 3D short arrays | Short |

### Geometry Types

| File | Description | Used For |
|------|-------------|----------|
| `geometry/FaultPlane.proto` | Fault plane geometry | Fault interpretation data |
| `geometry/PolyMesh.proto` | Polygon mesh data | 2D/3D mesh geometries (polylines, trimesh, quadmesh) |
| `geometry/FractureNetwork.proto` | Fracture network data | Complex fracture systems with properties |

### Common Types

| File | Description | Used For |
|------|-------------|----------|
| `common/CRS.proto` | Coordinate Reference System | Spatial reference information |

## Usage

These .proto files are compiled to Python modules during SDK generation:

```bash
# Compile all protobuf definitions
./scripts/generate_protobuf.sh
```

Generated files are placed in `dsis_model_sdk/protobuf/` as `*_pb2.py` modules.

## Python Usage

### Core Data Types

```python
from dsis_model_sdk.protobuf import (
    decode_horizon_data,
    decode_log_curves,
    decode_seismic_data,
    decode_lgc_structure,
    decode_property_table_set
)

# Decode horizon data
horizon_decoded = decode_horizon_data(binary_data)
print(f"Mode: {horizon_decoded.mode}")
print(f"Dimensions: {horizon_decoded.numberOfRows} x {horizon_decoded.numberOfColumns}")

# Decode log curves
log_decoded = decode_log_curves(log_binary_data)
for curve in log_decoded.values:
    print(f"Curve: {curve.name}, Unit: {curve.unit}")

# Decode seismic data
seismic_decoded = decode_seismic_data(seismic_binary_data)
print(f"Volume: {seismic_decoded.length.i} x {seismic_decoded.length.j} x {seismic_decoded.length.k}")

# Decode surface grid / tabular data (LGCStructure)
# Common for property grids, surface data, and columnar datasets
with open('surface.bin', 'rb') as f:
    binary_data = f.read()

# Use skip_length_prefix=True for files with varint length prefix
lgc_decoded = decode_lgc_structure(binary_data, skip_length_prefix=True)

print(f"Structure name: {lgc_decoded.structName}")
print(f"Number of columns: {len(lgc_decoded.elements)}")

# Access column data
for element in lgc_decoded.elements[:5]:
    print(f"Column: {element.elementName} (DataType: {element.dataType})")
    
    if element.data_float:
        # Filter out null values (commonly -99999.0)
        valid_values = [v for v in element.data_float if v != -99999.0]
        print(f"  Float data: {len(element.data_float)} values, {len(valid_values)} non-null")
        if valid_values:
            print(f"  Range: {min(valid_values):.2f} to {max(valid_values):.2f}")
    elif element.data_double:
        print(f"  Double data: {len(element.data_double)} values")
    elif element.data_int:
        print(f"  Integer data: {len(element.data_int)} values")
    elif element.data_string:
        print(f"  String data: {len(element.data_string)} values")

# Convert to pandas DataFrame
import pandas as pd
data_dict = {
    element.elementName or f"col_{i}": list(
        element.data_float or element.data_double or 
        element.data_int or element.data_string
    )
    for i, element in enumerate(lgc_decoded.elements)
}
df = pd.DataFrame(data_dict)
print(f"DataFrame shape: {df.shape}")
```

**Note on Length Prefixes**: When decoding binary files (not API responses), you may encounter a varint length prefix before the actual protobuf message. Set `skip_length_prefix=True` for decoders that support it (`decode_horizon_data`, `decode_seismic_data`, `decode_lgc_structure`, `decode_array_3f`, `decode_property_table_set`).

### Array Types

```python
from dsis_model_sdk.protobuf import decode_array_2f, decode_array_3f

# Decode 3D float array
array_3d = decode_array_3f(binary_data)
print(f"Shape: {array_3d.length.i} x {array_3d.length.j} x {array_3d.length.k}")
print(f"Data points: {len(array_3d.data)}")

# Decode 2D float array
array_2d = decode_array_2f(binary_data)
```

### Geometry Types

```python
from dsis_model_sdk.protobuf import (
    decode_fault_plane,
    decode_poly_mesh,
    decode_fracture_network
)

# Decode fault plane
fault = decode_fault_plane(fault_binary_data)
for segment in fault.faultSegment:
    print(f"Segment points: {len(segment.x)}")

# Decode polygon mesh
mesh = decode_poly_mesh(mesh_binary_data)
print(f"Mesh type: {mesh.meshset.geomType}")
print(f"Dimensions: {mesh.coordset.ndim}")

# Decode fracture network
fracnet = decode_fracture_network(fracnet_binary_data)
if fracnet.fractures:
    print(f"Number of fractures: {fracnet.fractures.num_fracture}")
```

## Source

These definitions are copies from the DSIS project to make them available for all OEC users.

For more information, see the main [PROTOBUF_GUIDE.md](../PROTOBUF_GUIDE.md).