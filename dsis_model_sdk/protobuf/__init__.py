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
from typing import Tuple, TypeVar

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



def _decode_varint(data: bytes, offset: int) -> Tuple[int, int]:
    """Decode a varint to find the size of the subsequent message and the offset where it starts.

    A varint is a variable-length encoding for integers used in protobuf to record the size of the subsequent message.

    Each byte of the varint  has the most significant bit (MSB) as a continuation flag.
    The remaining 7 bits of each byte contribute to the integer value.
    The varint ends when a byte with MSB=0 is encountered (meaning no continuation).

    Returns:
    (message_size, message_start): the message size (decoded int value) and the byte offset where it starts (after the decoded int)

    Raises:
    ValueError: If the varint is malformed or exceeds expected length
    """
    result = 0
    shift = 0
    while True:
        if offset >= len(data):
            raise ValueError("Unexpected end of data while decoding varint.")
        byte = data[offset]
        result |= (byte & 0x7F) << shift
        offset += 1
        if not (byte & 0x80):
            return result, offset
        shift += 7
        if shift > 64:
            raise ValueError("Varint is too long, possible overflow or malformed data.")

# All protobuf messages (such as LGCStructure, HorizonData3D, etc.) inherit from google.protobuf.message.Message
# With this, we bind that to a generic type _M so when a specific subbclass of Message is used, the type hinting
# will know which one it is and provide better autocompletion and type checking.
try:
    from google.protobuf.message import Message as _PbMessage
    _M = TypeVar('_M', bound=_PbMessage)
except ImportError:
    _M = TypeVar('_M')  # type: ignore[misc]


def _decode_length_delimited_protobuf(input_binary: bytes, target_protobuf: _M) -> _M:  # type: ignore[return]
    """
    Decode one or more length-delimited protobuf messages

    DSIS returns bulk protobuf payloads as lenght-delimited streams: a series of one or more messages,
    where each message is prefixed by a varint indicating its size, followed by the message bytes.
    This function reads all the messages in a payload, merging them into a single message.

    Args:
        input_binary: The raw bytes as received from the API.
        target_protobuf: A pre-instantiated (empty) object of any protobuf type (e.g. LGCStructure, HorizonData3D, etc.)
        Important: the object is modified in place and returned for convenience, but the caller can also
        just use the modified object without relying on the return value.

    Returns:
        The same target_protobuf object, now populated with the decoded data. 

    Raises:
        ValueError: If a varint is malformed or data is truncated.

    Example:
        >>> lgc_structure = LGCStructure_pb2.LGCStructure()
        >>> lgc_structure = _decode_length_delimited_protobuf(binary_data, lgc_structure)
    """
    offset = 0
    msg_count = 0
    while offset < len(input_binary):
        msg_size, msg_start = _decode_varint(input_binary, offset) # Read and decode the size of the next message
        msg_binary = input_binary[msg_start:msg_start + msg_size]  # Extract the actual message bytes
        if msg_count == 0:
            target_protobuf.ParseFromString(msg_binary)            # First message goes into empty buffer
        else:
            target_protobuf.MergeFromString(msg_binary)            # Subsequent messages are appended
        offset = msg_start + msg_size
        msg_count += 1
    return target_protobuf


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
    message = HorizonData3D_pb2.HorizonData3D() # type: ignore[attr-defined]
    if skip_length_prefix:
        _decode_length_delimited_protobuf(binary_data, message)
    else:
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
    message = SeismicData_pb2.SeismicData() # type: ignore[attr-defined]
    if skip_length_prefix:
        _decode_length_delimited_protobuf(binary_data, message)
    else:
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
    message = Array3FBuf_pb2.Array3FBuf() # type: ignore[attr-defined]
    if skip_length_prefix:
        _decode_length_delimited_protobuf(binary_data, message)
    else:
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


def decode_lgc_structure(binary_data: bytes) -> 'LGCStructure_pb2.LGCStructure': # type: ignore[name-defined]
    """
    Decode binary tabular data into structured LGCStructure protobuf message.

    The payload is a length-delimited protobuf stream: one or more
    concatenated messages, each prefixed by a varint indicating its size.
    The first message initialises the structure; subsequent messages are
    merged to build the complete table.
    
    Args:
        binary_data: Binary bytes containing tabular data (length-delimited)
        
    Returns:
        LGCStructure protobuf message with decoded tabular structure
        
    Raises:
        ImportError: If protobuf is not installed
        Exception: If binary data is invalid or corrupted
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_lgc_structure
        >>> 
        >>> decoded = decode_lgc_structure(raw_bytes)
        >>> print(f"Structure: {decoded.structName}")
        >>> for element in decoded.elements:
        ...     print(f"Element: {element.elementName}, Type: {element.dataType}")
    """
    _check_protobuf_available()
    message = LGCStructure_pb2.LGCStructure() # type: ignore[attr-defined]
    _decode_length_delimited_protobuf(binary_data, message)
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
    message = PropertyTableSet_pb2.PropertyTableSet() # type: ignore[attr-defined]
    if skip_length_prefix:
        _decode_length_delimited_protobuf(binary_data, message)
    else:
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
