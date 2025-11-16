# Protocol Buffer Definitions

This directory contains Protocol Buffer (.proto) definitions for DSIS bulk data formats.
These definitions are used to decode binary data fields from the DSIS API.

## Purpose

The DSIS API serves data in two formats:
- **Metadata**: OData (JSON) - entity properties, relationships, statistics
- **Bulk Data**: Protocol Buffers (binary) - large arrays encoded in binary `data` fields

These .proto files define the structure of the binary bulk data.

## Files

| File | Description | Used For |
|------|-------------|----------|
| `horizon/H3DProtoBuf.proto` | 3D horizon interpretation data | HorizonData3D z-values (FULL or SAMPLES mode) |
| `logcurve/LogCurveBuf.proto` | Well log curve data | Log measurements with depth/time index |
| `seismic/SeismicDataFloatBuf.proto` | Seismic amplitude data | 2D/3D seismic volumes |
| `seismic/SeismicDataHeaderBuf.proto` | Seismic header data | Trace headers and metadata |
| `tabular/LGCProtoBuf.proto` | Generic tabular data | Multi-purpose data structures |

## Usage

These .proto files are compiled to Python modules during SDK generation:

```bash
# Compile all protobuf definitions
./scripts/generate_protobuf.sh

# Or manually with protoc
protoc --python_out=dsis_model_sdk/protobuf \
    protobuf-definitions/horizon/H3DProtoBuf.proto
```

Generated files are placed in `dsis_model_sdk/protobuf/` as `*_pb2.py` modules.

## Python Usage

```python
from dsis_model_sdk.protobuf import decode_horizon_data

# Decode binary data
decoded = decode_horizon_data(binary_data)

# Access structured data
print(f"Mode: {decoded.mode}")
print(f"Dimensions: {decoded.numberOfRows} x {decoded.numberOfColumns}")
```

## Source

These definitions are copies from the DSIS project to make them available for all OEC users.

For more information, see the main [PROTOBUF_GUIDE.md](../PROTOBUF_GUIDE.md).