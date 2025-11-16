"""
DSIS Protobuf Decoders

This module provides utilities for decoding binary bulk data fields from DSIS API responses.
The DSIS API serves metadata via OData (JSON) and bulk data as Protocol Buffer encoded binary.

Supported data types:
- HorizonData3D: 3D horizon interpretation data with z-values
- LogCurves: Well log curve data with depth/time indices
- SeismicData: 2D/3D seismic amplitude data
- Tabular: Generic tabular data structures

Usage:
    from dsis_model_sdk.models.common import HorizonData3D
    from dsis_model_sdk.protobuf import decode_horizon_data
    
    # Get data from OData API
    horizon = HorizonData3D.from_dict(odata_response)
    
    # Decode binary data field
    if horizon.data:
        decoded = decode_horizon_data(horizon.data)
        
        # Access structured data
        if decoded.mode == decoded.FULL:
            for line in decoded.lines:
                print(f"Line {line.lineIndex}: {len(line.values)} values")
        elif decoded.mode == decoded.SAMPLES:
            samples = decoded.samples
            for col, row, val in zip(samples.columnIndex, samples.rowIndex, samples.value):
                print(f"Sample at ({col}, {row}): {val}")

Note: 
    The protobuf package is optional. Install with:
    pip install dsis-schemas[protobuf]
"""

# Import generated protobuf modules
try:
    from . import H3DProtoBuf_pb2
    from . import LogCurveBuf_pb2
    from . import SeismicDataFloatBuf_pb2
    from . import SeismicDataHeaderBuf_pb2
    from . import LGCProtoBuf_pb2
    
    PROTOBUF_AVAILABLE = True
except ImportError as e:
    PROTOBUF_AVAILABLE = False
    _import_error = str(e)


# Decoder functions
def decode_horizon_data(binary_data: bytes) -> 'H3DProtoBuf_pb2.HorizonData3D':
    """
    Decode binary horizon data into structured HorizonData3D protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of HorizonData3D model
        
    Returns:
        HorizonData3D protobuf message with decoded structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.models.common import HorizonData3D
        >>> from dsis_model_sdk.protobuf import decode_horizon_data
        >>> 
        >>> horizon = HorizonData3D.from_dict(api_response)
        >>> decoded = decode_horizon_data(horizon.data)
        >>> 
        >>> # Access data based on mode
        >>> if decoded.mode == decoded.FULL:
        ...     # All values including nulls (1.0E37f for non-interpreted)
        ...     for line in decoded.lines:
        ...         print(f"Line {line.lineIndex}, Direction: {line.direction}")
        ...         print(f"Values: {line.values[:10]}...")  # First 10 values
        >>> elif decoded.mode == decoded.SAMPLES:
        ...     # Only interpreted samples (sparse)
        ...     samples = decoded.samples
        ...     print(f"Total samples: {len(samples.value)}")
        ...     for i in range(min(5, len(samples.value))):
        ...         col = samples.columnIndex[i]
        ...         row = samples.rowIndex[i]
        ...         val = samples.value[i]
        ...         print(f"Sample {i}: col={col}, row={row}, z={val}")
    """
    _check_protobuf_available()
    message = H3DProtoBuf_pb2.HorizonData3D()
    message.ParseFromString(binary_data)
    return message


def decode_log_curves(binary_data: bytes) -> 'LogCurveBuf_pb2.LogCurves':
    """
    Decode binary log curve data into structured LogCurves protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of log curve models
        
    Returns:
        LogCurves protobuf message with decoded structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_log_curves
        >>> 
        >>> decoded = decode_log_curves(log_data.data)
        >>> 
        >>> # Access curve type and index
        >>> print(f"Curve type: {'DEPTH' if decoded.curve_type == decoded.DEPTH else 'TIME'}")
        >>> print(f"Index start: {decoded.index.start_index}")
        >>> print(f"Index increment: {decoded.index.increment}")
        >>> 
        >>> # Access curve values
        >>> for curve in decoded.values:
        ...     print(f"Curve: {curve.name}")
        ...     print(f"Data type: {curve.data_type}")
        ...     print(f"Unit: {curve.unit}")
        ...     if curve.data_type == curve.DOUBLE:
        ...         print(f"Values: {curve.data_double[:10]}")  # First 10 values
    """
    _check_protobuf_available()
    message = LogCurveBuf_pb2.LogCurves()
    message.ParseFromString(binary_data)
    return message


def decode_seismic_float_data(binary_data: bytes) -> 'SeismicDataFloatBuf_pb2.Array3FBuf':
    """
    Decode binary 3D seismic float data into structured Array3FBuf protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of seismic models
        
    Returns:
        Array3FBuf protobuf message with decoded 3D array structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_seismic_float_data
        >>> 
        >>> decoded = decode_seismic_float_data(seismic_data.data)
        >>> 
        >>> # Access dimensions
        >>> print(f"Dimensions: i={decoded.length.i}, j={decoded.length.j}, k={decoded.length.k}")
        >>> 
        >>> # Access header if present
        >>> if decoded.HasField('header'):
        ...     print(f"World coordinates: X={decoded.header.x}, Y={decoded.header.y}")
        ...     print(f"Scalar: {decoded.header.scalarXY}")
        >>> 
        >>> # Access data array
        >>> print(f"Total data points: {len(decoded.data)}")
        >>> print(f"First 10 values: {decoded.data[:10]}")
    """
    _check_protobuf_available()
    message = SeismicDataFloatBuf_pb2.Array3FBuf()
    message.ParseFromString(binary_data)
    return message


def decode_seismic_2d_float_data(binary_data: bytes) -> 'SeismicDataFloatBuf_pb2.Array2FBuf':
    """
    Decode binary 2D seismic float data into structured Array2FBuf protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of 2D seismic models
        
    Returns:
        Array2FBuf protobuf message with decoded 2D array structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = SeismicDataFloatBuf_pb2.Array2FBuf()
    message.ParseFromString(binary_data)
    return message


def decode_tabular_data(binary_data: bytes) -> 'LGCProtoBuf_pb2.LGCStructure':
    """
    Decode binary tabular data into structured LGCStructure protobuf message.
    
    Args:
        binary_data: Binary bytes containing tabular data
        
    Returns:
        LGCStructure protobuf message with decoded tabular structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_tabular_data
        >>> 
        >>> decoded = decode_tabular_data(table_data.data)
        >>> 
        >>> # Access columns
        >>> for column in decoded.columns:
        ...     print(f"Column: {column.name}, Type: {column.dataType}")
        >>> 
        >>> # Access rows
        >>> for row in decoded.rows:
        ...     print(f"Row data: {row.values}")
    """
    _check_protobuf_available()
    message = LGCProtoBuf_pb2.LGCStructure()
    message.ParseFromString(binary_data)
    return message


def _check_protobuf_available():
    """Check if protobuf package is available."""
    if not PROTOBUF_AVAILABLE:
        raise ImportError(
            "Protocol Buffers support is not available. "
            "Install with: pip install dsis-schemas[protobuf]\n"
            f"Original error: {_import_error}"
        )


# Export public API
__all__ = [
    'decode_horizon_data',
    'decode_log_curves',
    'decode_seismic_float_data',
    'decode_seismic_2d_float_data',
    'decode_tabular_data',
    'PROTOBUF_AVAILABLE',
    # Generated modules (for advanced users)
    'H3DProtoBuf_pb2',
    'LogCurveBuf_pb2',
    'SeismicDataFloatBuf_pb2',
    'SeismicDataHeaderBuf_pb2',
    'LGCProtoBuf_pb2',
]
