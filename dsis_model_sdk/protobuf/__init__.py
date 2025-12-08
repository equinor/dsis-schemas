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
    from dsis_model_sdk.protobuf import decode_horizon_data, H3DProtoBuf_pb2
    
    # Get data from OData API
    horizon = HorizonData3D.from_dict(odata_response)
    
    # Decode binary data field
    if horizon.data:
        decoded = decode_horizon_data(horizon.data)
        
        # Access structured data
        if decoded.mode == H3DProtoBuf_pb2.HorizonData3D.FULL:
            for line in decoded.lines:
                print(f"Line {line.lineIndex}: {len(line.values)} values")
        elif decoded.mode == H3DProtoBuf_pb2.HorizonData3D.SAMPLES:
            samples = decoded.samples
            for col, row, val in zip(samples.columnIndex, samples.rowIndex, samples.value):
                print(f"Sample at ({col}, {row}): {val}")

Note: 
    The protobuf package is optional. Install with:
    pip install dsis-schemas[protobuf]
"""

# Import generated protobuf modules
try:
    # Core data types
    from . import HorizonData3D_pb2
    from . import LogCurves_pb2
    from . import SeismicData_pb2
    from . import SeismicDataHeader_pb2
    from . import SeismicDataHeader2D_pb2
    from . import LGCStructure_pb2
    from . import PropertyTableSet_pb2
    
    # Array types
    from . import Array2FBuf_pb2
    from . import Array2FBufList_pb2
    from . import Array3BBuf_pb2
    from . import Array3FBuf_pb2
    from . import Array3FBufList_pb2
    from . import Array3IBuf_pb2
    from . import Array3SBuf_pb2
    
    # Geometry types
    from . import FaultPlane_pb2
    from . import PolyMesh_pb2
    from . import FractureNetwork_pb2
    
    # Common types
    from . import CRS_pb2
    
    PROTOBUF_AVAILABLE = True
except ImportError as e:
    PROTOBUF_AVAILABLE = False
    _import_error = str(e)


# Helper function for length-prefixed messages
def _skip_varint_length_prefix(binary_data: bytes) -> bytes:
    """
    Skip varint length prefix and return the actual message bytes.
    
    This is commonly used when protobuf messages are stored in files or
    transmitted over streams where message boundaries need to be defined.
    
    Args:
        binary_data: Binary data with varint length prefix
        
    Returns:
        Binary data without the length prefix
    """
    result = 0
    shift = 0
    offset = 0
    while offset < len(binary_data):
        byte = binary_data[offset]
        result |= (byte & 0x7f) << shift
        offset += 1
        if not (byte & 0x80):
            break
        shift += 7
    # Return only the message bytes (using length for boundary)
    return binary_data[offset:offset + result]


# Decoder functions
def decode_horizon_data(binary_data: bytes, skip_length_prefix: bool = False) -> 'HorizonData3D_pb2.HorizonData3D':
    """
    Decode binary horizon data into structured HorizonData3D protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of HorizonData3D model
        skip_length_prefix: If True, skips varint length prefix (for file storage)
        
    Returns:
        HorizonData3D protobuf message with decoded structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.models.common import HorizonData3D
        >>> from dsis_model_sdk.protobuf import decode_horizon_data, HorizonData3D_pb2
        >>> 
        >>> horizon = HorizonData3D.from_dict(api_response)
        >>> decoded = decode_horizon_data(horizon.data)
        >>> 
        >>> # Access data based on mode
        >>> if decoded.mode == HorizonData3D_pb2.HorizonData3D.FULL:
        ...     # All values including nulls (1.0E37f for non-interpreted)
        ...     for line in decoded.lines:
        ...         print(f"Line {line.lineIndex}, Direction: {line.direction}")
        ...         print(f"Values: {line.values[:10]}...")  # First 10 values
        >>> elif decoded.mode == HorizonData3D_pb2.HorizonData3D.SAMPLES:
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
    if skip_length_prefix:
        binary_data = _skip_varint_length_prefix(binary_data)
    message = HorizonData3D_pb2.HorizonData3D()
    message.ParseFromString(binary_data)
    return message


def decode_log_curves(binary_data: bytes) -> 'LogCurves_pb2.LogCurves':
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
        >>> from dsis_model_sdk.protobuf import decode_log_curves, LogCurves_pb2
        >>> 
        >>> decoded = decode_log_curves(log_data.data)
        >>> 
        >>> # Access curve type and index
        >>> print(f"Curve type: {'DEPTH' if decoded.curve_type == LogCurves_pb2.LogCurves.DEPTH else 'TIME'}")
        >>> print(f"Index start: {decoded.index.start_index}")
        >>> print(f"Index increment: {decoded.index.increment}")
        >>> 
        >>> # Access curve values
        >>> for curve in decoded.values:
        ...     print(f"Curve: {curve.name}")
        ...     print(f"Data type: {curve.data_type}")
        ...     print(f"Unit: {curve.unit}")
        ...     if curve.data_type == LogCurves_pb2.LogCurves.CurveValue.DOUBLE:
        ...         print(f"Values: {curve.data_double[:10]}")  # First 10 values
    """
    _check_protobuf_available()
    message = LogCurves_pb2.LogCurves()
    message.ParseFromString(binary_data)
    return message


def decode_seismic_data(binary_data: bytes, skip_length_prefix: bool = False) -> 'SeismicData_pb2.SeismicData':
    """
    Decode binary seismic data into structured SeismicData protobuf message.
    
    Args:
        binary_data: Binary bytes from the 'data' field of seismic models
        skip_length_prefix: If True, skips varint length prefix (for file storage)
        
    Returns:
        SeismicData protobuf message with decoded structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_seismic_data
        >>> 
        >>> decoded = decode_seismic_data(seismic_data.data)
        >>> 
        >>> # Access dimensions
        >>> print(f"Dimensions: i={decoded.length.i}, j={decoded.length.j}, k={decoded.length.k}")
        >>> 
        >>> # Access data based on type
        >>> if decoded.data.data_float:
        ...     print(f"Float data: {len(decoded.data.data_float)} values")
        >>> elif decoded.data.data_short:
        ...     print(f"Short data: {len(decoded.data.data_short)} values")
    """
    _check_protobuf_available()
    if skip_length_prefix:
        binary_data = _skip_varint_length_prefix(binary_data)
    message = SeismicData_pb2.SeismicData()
    message.ParseFromString(binary_data)
    return message


def decode_array_3f(binary_data: bytes, skip_length_prefix: bool = False) -> 'Array3FBuf_pb2.Array3FBuf':
    """
    Decode binary 3D float array data into structured Array3FBuf protobuf message.
    
    Args:
        binary_data: Binary bytes containing 3D float array data
        skip_length_prefix: If True, skips varint length prefix (for file storage)
        
    Returns:
        Array3FBuf protobuf message with decoded 3D array structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> decoded = decode_array_3f(binary_data)
        >>> print(f"Dimensions: {decoded.length.i} x {decoded.length.j} x {decoded.length.k}")
        >>> print(f"Data points: {len(decoded.data)}")
    """
    _check_protobuf_available()
    if skip_length_prefix:
        binary_data = _skip_varint_length_prefix(binary_data)
    message = Array3FBuf_pb2.Array3FBuf()
    message.ParseFromString(binary_data)
    return message


def decode_array_2f(binary_data: bytes) -> 'Array2FBuf_pb2.Array2FBuf':
    """
    Decode binary 2D float array data into structured Array2FBuf protobuf message.
    
    Args:
        binary_data: Binary bytes containing 2D float array data
        
    Returns:
        Array2FBuf protobuf message with decoded 2D array structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = Array2FBuf_pb2.Array2FBuf()
    message.ParseFromString(binary_data)
    return message


def decode_lgc_structure(binary_data: bytes, skip_length_prefix: bool = False) -> 'LGCStructure_pb2.LGCStructure':
    """
    Decode binary tabular data into structured LGCStructure protobuf message.
    
    Args:
        binary_data: Binary bytes containing tabular data
        skip_length_prefix: If True, skips varint length prefix (for file storage)
        
    Returns:
        LGCStructure protobuf message with decoded tabular structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_lgc_structure
        >>> 
        >>> # Decode with length prefix (common in file storage)
        >>> decoded = decode_lgc_structure(file_data, skip_length_prefix=True)
        >>> 
        >>> # Access structure
        >>> print(f"Structure: {decoded.structName}")
        >>> for element in decoded.elements:
        ...     print(f"Element: {element.elementName}, Type: {element.dataType}")
    """
    _check_protobuf_available()
    if skip_length_prefix:
        binary_data = _skip_varint_length_prefix(binary_data)
    message = LGCStructure_pb2.LGCStructure()
    message.ParseFromString(binary_data)
    return message


def decode_fault_plane(binary_data: bytes) -> 'FaultPlane_pb2.FaultPlane':
    """
    Decode binary fault plane data into structured FaultPlane protobuf message.
    
    Args:
        binary_data: Binary bytes containing fault plane geometry data
        
    Returns:
        FaultPlane protobuf message with decoded fault segments
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = FaultPlane_pb2.FaultPlane()
    message.ParseFromString(binary_data)
    return message


def decode_poly_mesh(binary_data: bytes) -> 'PolyMesh_pb2.PolyMesh':
    """
    Decode binary mesh data into structured PolyMesh protobuf message.
    
    Args:
        binary_data: Binary bytes containing 2D/3D mesh geometry
        
    Returns:
        PolyMesh protobuf message with decoded mesh structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = PolyMesh_pb2.PolyMesh()
    message.ParseFromString(binary_data)
    return message


def decode_fracture_network(binary_data: bytes) -> 'FractureNetwork_pb2.FractureNetwork':
    """
    Decode binary fracture network data into structured FractureNetwork protobuf message.
    
    Args:
        binary_data: Binary bytes containing fracture network data
        
    Returns:
        FractureNetwork protobuf message with decoded fracture data
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = FractureNetwork_pb2.FractureNetwork()
    message.ParseFromString(binary_data)
    return message


def decode_property_table_set(binary_data: bytes, skip_length_prefix: bool = False) -> 'PropertyTableSet_pb2.PropertyTableSet':
    """
    Decode binary property table set data into structured PropertyTableSet protobuf message.
    
    Args:
        binary_data: Binary bytes containing property table data
        skip_length_prefix: If True, skips varint length prefix (for file storage)
        
    Returns:
        PropertyTableSet protobuf message with decoded property tables
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    if skip_length_prefix:
        binary_data = _skip_varint_length_prefix(binary_data)
    message = PropertyTableSet_pb2.PropertyTableSet()
    message.ParseFromString(binary_data)
    return message


def decode_seismic_header(binary_data: bytes) -> 'SeismicDataHeader_pb2.SeismicDataHeader':
    """
    Decode binary seismic header data into structured SeismicDataHeader protobuf message.
    
    Args:
        binary_data: Binary bytes containing seismic header metadata
        
    Returns:
        SeismicDataHeader protobuf message with decoded header info
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = SeismicDataHeader_pb2.SeismicDataHeader()
    message.ParseFromString(binary_data)
    return message


def decode_seismic_header_2d(binary_data: bytes) -> 'SeismicDataHeader2D_pb2.SeismicDataHeader2D':
    """
    Decode binary 2D seismic header data into structured SeismicDataHeader2D protobuf message.
    
    Args:
        binary_data: Binary bytes containing 2D seismic header metadata
        
    Returns:
        SeismicDataHeader2D protobuf message with decoded header info
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
    """
    _check_protobuf_available()
    message = SeismicDataHeader2D_pb2.SeismicDataHeader2D()
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
    # Core decoder functions
    'decode_horizon_data',
    'decode_log_curves',
    'decode_seismic_data',
    'decode_seismic_header',
    'decode_seismic_header_2d',
    'decode_lgc_structure',
    'decode_property_table_set',
    
    # Array decoder functions
    'decode_array_2f',
    'decode_array_3f',
    
    # Geometry decoder functions
    'decode_fault_plane',
    'decode_poly_mesh',
    'decode_fracture_network',
    
    # Status flag
    'PROTOBUF_AVAILABLE',
    
    # Generated modules (for advanced users)
    'HorizonData3D_pb2',
    'LogCurves_pb2',
    'SeismicData_pb2',
    'SeismicDataHeader_pb2',
    'SeismicDataHeader2D_pb2',
    'LGCStructure_pb2',
    'PropertyTableSet_pb2',
    'Array2FBuf_pb2',
    'Array2FBufList_pb2',
    'Array3BBuf_pb2',
    'Array3FBuf_pb2',
    'Array3FBufList_pb2',
    'Array3IBuf_pb2',
    'Array3SBuf_pb2',
    'FaultPlane_pb2',
    'PolyMesh_pb2',
    'FractureNetwork_pb2',
    'CRS_pb2',
]
