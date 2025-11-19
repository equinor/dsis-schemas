"""
Protobuf Decoder Utilities

Helper functions for working with protobuf-encoded bulk data in DSIS models.
These utilities provide convenient wrappers and conversion functions for common use cases.
"""

from typing import List, Tuple, Optional, Dict, Any
import numpy as np


def horizon_to_numpy(decoded_horizon) -> Tuple[Optional[np.ndarray], Dict[str, Any]]:
    """
    Convert decoded HorizonData3D protobuf to NumPy array.
    
    Args:
        decoded_horizon: Decoded HorizonData3D protobuf message
        
    Returns:
        Tuple of (data_array, metadata) where:
        - data_array: 2D NumPy array with shape (rows, columns) or None if in SAMPLES mode
        - metadata: Dictionary with metadata (mode, dimensions, etc.)
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_horizon_data
        >>> from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy
        >>> 
        >>> decoded = decode_horizon_data(horizon.data)
        >>> array, meta = horizon_to_numpy(decoded)
        >>> 
        >>> print(f"Shape: {array.shape}")
        >>> print(f"Mode: {meta['mode']}")
        >>> print(f"Min z-value: {np.nanmin(array)}")
        >>> print(f"Max z-value: {np.nanmax(array)}")
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError("NumPy is required for this function. Install with: pip install numpy")
    
    # Import protobuf to access enum values
    try:
        from dsis_model_sdk.protobuf import H3DProtoBuf_pb2
    except ImportError:
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'protobuf'))
        import H3DProtoBuf_pb2
    
    metadata = {
        'mode': 'FULL' if decoded_horizon.mode == H3DProtoBuf_pb2.HorizonData3D.FULL else 'SAMPLES',
        'first_row_index': decoded_horizon.firstRowIndex,
        'number_of_rows': decoded_horizon.numberOfRows,
        'first_column_index': decoded_horizon.firstColumnIndex,
        'number_of_columns': decoded_horizon.numberOfColumns,
    }
    
    if decoded_horizon.mode == H3DProtoBuf_pb2.HorizonData3D.FULL:
        # Convert lines to 2D array
        rows = decoded_horizon.numberOfRows
        cols = decoded_horizon.numberOfColumns
        array = np.full((rows, cols), np.nan, dtype=np.float32)
        
        for line in decoded_horizon.lines:
            if line.direction == H3DProtoBuf_pb2.HorizonData3D.COLUMN:
                # Column direction: fill column
                col_idx = line.lineIndex - decoded_horizon.firstColumnIndex
                if 0 <= col_idx < cols:
                    values = np.array(line.values, dtype=np.float32)
                    # Replace null value (1.0E37) with NaN
                    values[values >= 1.0e37] = np.nan
                    array[:len(values), col_idx] = values
            else:
                # Row direction: fill row
                row_idx = line.lineIndex - decoded_horizon.firstRowIndex
                if 0 <= row_idx < rows:
                    values = np.array(line.values, dtype=np.float32)
                    values[values >= 1.0e37] = np.nan
                    array[row_idx, :len(values)] = values
        
        return array, metadata
    
    else:  # SAMPLES mode
        metadata['sample_count'] = len(decoded_horizon.samples.value) if decoded_horizon.HasField('samples') else 0
        return None, metadata


def horizon_samples_to_dict(decoded_horizon) -> List[Dict[str, Any]]:
    """
    Convert horizon samples to list of dictionaries.
    
    Args:
        decoded_horizon: Decoded HorizonData3D protobuf message
        
    Returns:
        List of dictionaries with keys: 'column', 'row', 'value'
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_horizon_data
        >>> from dsis_model_sdk.utils.protobuf_decoders import horizon_samples_to_dict
        >>> 
        >>> decoded = decode_horizon_data(horizon.data)
        >>> samples = horizon_samples_to_dict(decoded)
        >>> 
        >>> for sample in samples[:5]:
        ...     print(f"Col {sample['column']}, Row {sample['row']}: {sample['value']}")
    """
    if not decoded_horizon.HasField('samples'):
        return []
    
    samples = decoded_horizon.samples
    return [
        {
            'column': col,
            'row': row,
            'value': val
        }
        for col, row, val in zip(samples.columnIndex, samples.rowIndex, samples.value)
    ]


def log_curve_to_dict(decoded_log_curves) -> Dict[str, Any]:
    """
    Convert decoded LogCurves protobuf to dictionary format.
    
    Args:
        decoded_log_curves: Decoded LogCurves protobuf message
        
    Returns:
        Dictionary with structured log curve data
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_log_curves
        >>> from dsis_model_sdk.utils.protobuf_decoders import log_curve_to_dict
        >>> 
        >>> decoded = decode_log_curves(log_data.data)
        >>> data = log_curve_to_dict(decoded)
        >>> 
        >>> print(f"Curve type: {data['curve_type']}")
        >>> print(f"Index unit: {data['index']['unit']}")
        >>> 
        >>> for curve_name, curve_data in data['curves'].items():
        ...     print(f"{curve_name}: {len(curve_data['values'])} values")
    """
    result = {
        'curve_type': 'DEPTH' if decoded_log_curves.curve_type == decoded_log_curves.DEPTH else 'TIME',
        'index': {
            'increment': decoded_log_curves.index.increment,
            'start_index': decoded_log_curves.index.start_index,
            'number_of_index': decoded_log_curves.index.number_of_index,
            'unit_type': decoded_log_curves.index.unit_type,
            'unit': decoded_log_curves.index.unit,
            'values': list(decoded_log_curves.index.index) if decoded_log_curves.index.index else None
        },
        'curves': {}
    }
    
    # Import the protobuf module to access enum values
    try:
        from dsis_model_sdk.protobuf import LogCurveBuf_pb2
    except ImportError:
        import sys
        import os
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'protobuf'))
        import LogCurveBuf_pb2
    
    for curve in decoded_log_curves.values:
        # Access enums from the LogCurves message class
        data_type_map = {
            LogCurveBuf_pb2.LogCurves.DOUBLE: 'DOUBLE',
            LogCurveBuf_pb2.LogCurves.FLOAT: 'FLOAT',
            LogCurveBuf_pb2.LogCurves.INT: 'INT',
            LogCurveBuf_pb2.LogCurves.LONG: 'LONG',
            LogCurveBuf_pb2.LogCurves.STRING: 'STRING'
        }
        
        sample_type_map = {
            LogCurveBuf_pb2.LogCurves.VALUE: 'VALUE',
            LogCurveBuf_pb2.LogCurves.FIXEDLIST1D: 'FIXEDLIST1D',
            LogCurveBuf_pb2.LogCurves.FIXEDLIST2D: 'FIXEDLIST2D',
            LogCurveBuf_pb2.LogCurves.VARIABLELIST: 'VARIABLELIST',
            LogCurveBuf_pb2.LogCurves.FIXEDROWSVARCOLSLIST2D: 'FIXEDROWSVARCOLSLIST2D'
        }
        
        # Get actual data based on data type
        values = None
        if curve.data_type == LogCurveBuf_pb2.LogCurves.DOUBLE:
            values = list(curve.data_double)
        elif curve.data_type == LogCurveBuf_pb2.LogCurves.FLOAT:
            values = list(curve.data_float)
        elif curve.data_type == LogCurveBuf_pb2.LogCurves.INT:
            values = list(curve.data_int)
        elif curve.data_type == LogCurveBuf_pb2.LogCurves.LONG:
            values = list(curve.data_long)
        elif curve.data_type == LogCurveBuf_pb2.LogCurves.STRING:
            values = list(curve.data_string)
        
        curve_data = {
            'name': curve.name,
            'native_uid': curve.native_uid,
            'sample_type': sample_type_map.get(curve.sample_type, 'UNKNOWN'),
            'data_type': data_type_map.get(curve.data_type, 'UNKNOWN'),
            'unit_type': curve.unit_type,
            'unit': curve.unit,
            'null_value': curve.null_value,
            'fixed_columns': curve.fixed_columns,
            'fixed_rows': curve.fixed_rows,
            'values': values
        }
        
        result['curves'][curve.name] = curve_data
    
    return result


def seismic_3d_to_numpy(decoded_seismic):
    """
    Convert decoded 3D seismic data to NumPy array.
    
    Args:
        decoded_seismic: Decoded Array3FBuf protobuf message
        
    Returns:
        Tuple of (data_array, metadata) where:
        - data_array: 3D NumPy array with shape (i, j, k)
        - metadata: Dictionary with dimensions and header info
        
    Example:
        >>> from dsis_model_sdk.protobuf import decode_seismic_float_data
        >>> from dsis_model_sdk.utils.protobuf_decoders import seismic_3d_to_numpy
        >>> 
        >>> decoded = decode_seismic_float_data(seismic.data)
        >>> array, meta = seismic_3d_to_numpy(decoded)
        >>> 
        >>> print(f"Shape: {array.shape}")
        >>> print(f"World X: {meta['header']['x']}")
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError("NumPy is required for this function. Install with: pip install numpy")
    
    i, j, k = decoded_seismic.length.i, decoded_seismic.length.j, decoded_seismic.length.k
    array = np.array(decoded_seismic.data, dtype=np.float32).reshape((i, j, k))
    
    metadata = {
        'dimensions': {'i': i, 'j': j, 'k': k},
        'header': None
    }
    
    if decoded_seismic.HasField('header'):
        metadata['header'] = {
            'x': decoded_seismic.header.x,
            'y': decoded_seismic.header.y,
            'scalarXY': decoded_seismic.header.scalarXY
        }
    
    return array, metadata


def seismic_2d_to_numpy(decoded_seismic):
    """
    Convert decoded 2D seismic data to NumPy array.
    
    Args:
        decoded_seismic: Decoded Array2FBuf protobuf message
        
    Returns:
        Tuple of (data_array, metadata) where:
        - data_array: 2D NumPy array with shape (i, k)
        - metadata: Dictionary with dimensions and header info
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError("NumPy is required for this function. Install with: pip install numpy")
    
    i, k = decoded_seismic.length.i, decoded_seismic.length.k
    array = np.array(decoded_seismic.data, dtype=np.float32).reshape((i, k))
    
    metadata = {
        'dimensions': {'i': i, 'k': k},
        'header': None
    }
    
    if decoded_seismic.HasField('header'):
        metadata['header'] = {
            'x': decoded_seismic.header.x,
            'y': decoded_seismic.header.y,
            'shotpoint': decoded_seismic.header.shotpoint,
            'scalarXY': decoded_seismic.header.scalarXY
        }
    
    return array, metadata


__all__ = [
    'horizon_to_numpy',
    'horizon_samples_to_dict',
    'log_curve_to_dict',
    'seismic_3d_to_numpy',
    'seismic_2d_to_numpy',
]
