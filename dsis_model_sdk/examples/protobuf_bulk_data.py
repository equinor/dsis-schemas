"""
Example: Working with Protobuf-Encoded Bulk Data in DSIS

This example demonstrates how to use the DSIS SDK to work with bulk data
that is encoded using Protocol Buffers. The DSIS API serves:
- Metadata via OData (JSON format)
- Bulk data as binary Protocol Buffer encoded fields

This example shows how to:
1. Query OData API for metadata
2. Decode binary bulk data fields
3. Convert to NumPy arrays for analysis
4. Work with different data types (horizon, log curves, seismic)
"""

# Example 1: Decoding HorizonData3D bulk data
def example_horizon_data():
    """
    Example of decoding 3D horizon interpretation data.
    
    HorizonData3D contains:
    - Metadata: horizon name, survey info, statistics (from OData JSON)
    - Bulk data: z-values for interpreted surface (from protobuf binary)
    """
    from dsis_model_sdk.models.common import HorizonData3D
    from dsis_model_sdk.protobuf import decode_horizon_data
    from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy, horizon_samples_to_dict
    
    # Simulate OData API response (in real use, this comes from API)
    odata_response = {
        'native_uid': 'horizon_001',
        'horizon_name': 'Top_Reservoir',
        'data_source': 'DSIS',
        'horizon_attribute_name': 'Depth',
        'interpretation_version_name': 'Final',
        'seismic3dsurvey_native_uid': 'survey_001',
        'horizon_mean': 2450.5,
        'horizon_min': 2200.0,
        'horizon_max': 2700.0,
        'data': b'\x08\x01\x10...',  # Binary protobuf data (example truncated)
    }
    
    # Step 1: Create model from OData response
    horizon = HorizonData3D.from_dict(odata_response)
    
    print(f"Horizon: {horizon.horizon_name}")
    print(f"Mean depth: {horizon.horizon_mean} {horizon.horizon_mean_unit}")
    print(f"Depth range: {horizon.horizon_min} - {horizon.horizon_max}")
    
    # Step 2: Decode binary bulk data
    if horizon.data:
        decoded = decode_horizon_data(horizon.data)
        
        print(f"\nBulk data mode: {'FULL' if decoded.mode == decoded.FULL else 'SAMPLES'}")
        print(f"Grid dimensions: {decoded.numberOfRows} x {decoded.numberOfColumns}")
        
        # Step 3a: Convert to NumPy array (for FULL mode)
        if decoded.mode == decoded.FULL:
            array, metadata = horizon_to_numpy(decoded)
            print(f"Array shape: {array.shape}")
            print(f"Valid samples: {(~np.isnan(array)).sum()}")
            print(f"Coverage: {(~np.isnan(array)).sum() / array.size * 100:.1f}%")
            
            # Analyze data
            import numpy as np
            valid_data = array[~np.isnan(array)]
            print(f"Data min: {np.min(valid_data):.2f}")
            print(f"Data max: {np.max(valid_data):.2f}")
            print(f"Data mean: {np.mean(valid_data):.2f}")
        
        # Step 3b: Get sparse samples (for SAMPLES mode)
        elif decoded.mode == decoded.SAMPLES:
            samples = horizon_samples_to_dict(decoded)
            print(f"Number of samples: {len(samples)}")
            
            # Show first few samples
            for i, sample in enumerate(samples[:5]):
                print(f"  Sample {i}: col={sample['column']}, row={sample['row']}, z={sample['value']:.2f}")


# Example 2: Decoding LogCurve bulk data
def example_log_curve_data():
    """
    Example of decoding well log curve data.
    
    LogCurve contains:
    - Metadata: curve name, well info, units (from OData JSON)
    - Bulk data: depth/time index and curve values (from protobuf binary)
    """
    from dsis_model_sdk.protobuf import decode_log_curves
    from dsis_model_sdk.utils.protobuf_decoders import log_curve_to_dict
    
    # Assume we have binary log curve data from API
    binary_data = b'...'  # Binary protobuf data from API
    
    # Step 1: Decode binary data
    decoded = decode_log_curves(binary_data)
    
    print(f"Curve type: {'DEPTH' if decoded.curve_type == decoded.DEPTH else 'TIME'}")
    print(f"Index start: {decoded.index.start_index} {decoded.index.unit}")
    print(f"Index increment: {decoded.index.increment}")
    print(f"Number of samples: {decoded.index.number_of_index}")
    
    # Step 2: Convert to dict for easier access
    data = log_curve_to_dict(decoded)
    
    print(f"\nCurves in dataset: {len(data['curves'])}")
    
    for curve_name, curve_data in data['curves'].items():
        print(f"\nCurve: {curve_name}")
        print(f"  Data type: {curve_data['data_type']}")
        print(f"  Unit: {curve_data['unit']}")
        print(f"  Number of values: {len(curve_data['values'])}")
        print(f"  Value range: {min(curve_data['values']):.2f} - {max(curve_data['values']):.2f}")
        
        # Step 3: Create depth vs value pairs
        if data['index']['values']:
            # Non-periodic curve with explicit depth values
            depth_values = list(zip(data['index']['values'], curve_data['values']))
            print(f"  First 3 samples: {depth_values[:3]}")
        else:
            # Periodic curve - calculate depths
            start = data['index']['start_index']
            increment = data['index']['increment']
            depths = [start + i * increment for i in range(len(curve_data['values']))]
            depth_values = list(zip(depths, curve_data['values']))
            print(f"  First 3 samples: {depth_values[:3]}")


# Example 3: Decoding Seismic bulk data
def example_seismic_3d_data():
    """
    Example of decoding 3D seismic amplitude data.
    
    Seismic data contains:
    - Metadata: survey info, trace/sample info (from OData JSON)
    - Bulk data: 3D volume of amplitude values (from protobuf binary)
    """
    from dsis_model_sdk.protobuf import decode_seismic_float_data
    from dsis_model_sdk.utils.protobuf_decoders import seismic_3d_to_numpy
    
    # Assume we have binary seismic data from API
    binary_data = b'...'  # Binary protobuf data from API
    
    # Step 1: Decode binary data
    decoded = decode_seismic_float_data(binary_data)
    
    print(f"Dimensions: i={decoded.length.i}, j={decoded.length.j}, k={decoded.length.k}")
    
    if decoded.HasField('header'):
        print(f"Origin: X={decoded.header.x}, Y={decoded.header.y}")
        print(f"Coordinate scalar: {decoded.header.scalarXY}")
    
    # Step 2: Convert to NumPy array
    array, metadata = seismic_3d_to_numpy(decoded)
    
    print(f"\nArray shape: {array.shape}")
    print(f"Data type: {array.dtype}")
    print(f"Memory size: {array.nbytes / 1024 / 1024:.2f} MB")
    
    # Step 3: Analyze seismic data
    import numpy as np
    print(f"Amplitude range: {np.min(array):.2f} to {np.max(array):.2f}")
    print(f"Mean amplitude: {np.mean(array):.2f}")
    print(f"Std deviation: {np.std(array):.2f}")
    
    # Extract a single trace
    trace_i, trace_j = 100, 100
    trace = array[trace_i, trace_j, :]
    print(f"\nTrace at ({trace_i}, {trace_j}):")
    print(f"  Samples: {len(trace)}")
    print(f"  Min: {np.min(trace):.2f}, Max: {np.max(trace):.2f}")


# Example 4: Complete workflow with OData query
def example_complete_workflow():
    """
    Complete example showing the typical workflow:
    1. Query DSIS OData API for metadata
    2. Request bulk data endpoint
    3. Decode and process data
    """
    import requests
    from dsis_model_sdk.models.common import HorizonData3D
    from dsis_model_sdk.protobuf import decode_horizon_data
    from dsis_model_sdk.utils.protobuf_decoders import horizon_to_numpy
    
    # Configuration
    DSIS_API_BASE = "https://dsis-api.example.com/odata"
    
    # Step 1: Query OData API for horizon metadata
    print("Step 1: Querying OData API for horizon metadata...")
    response = requests.get(
        f"{DSIS_API_BASE}/HorizonData3D",
        params={
            '$filter': "horizon_name eq 'Top_Reservoir'",
            '$select': 'native_uid,horizon_name,seismic3dsurvey_native_uid,horizon_mean,horizon_min,horizon_max'
        }
    )
    
    metadata = response.json()['value'][0]
    print(f"Found horizon: {metadata['horizon_name']}")
    
    # Step 2: Request bulk data (binary protobuf)
    print("\nStep 2: Requesting bulk data...")
    native_uid = metadata['native_uid']
    bulk_response = requests.get(
        f"{DSIS_API_BASE}/HorizonData3D('{native_uid}')/data/$value",
        headers={'Accept': 'application/octet-stream'}
    )
    
    binary_data = bulk_response.content
    print(f"Received {len(binary_data)} bytes of bulk data")
    
    # Step 3: Create model with metadata
    print("\nStep 3: Creating model with metadata...")
    metadata['data'] = binary_data
    horizon = HorizonData3D.from_dict(metadata)
    
    # Step 4: Decode and process bulk data
    print("\nStep 4: Decoding bulk data...")
    decoded = decode_horizon_data(horizon.data)
    array, meta = horizon_to_numpy(decoded)
    
    print(f"Decoded horizon data:")
    print(f"  Mode: {meta['mode']}")
    print(f"  Shape: {array.shape}")
    print(f"  Coverage: {(~np.isnan(array)).sum() / array.size * 100:.1f}%")
    
    # Step 5: Use the data
    print("\nStep 5: Using the data...")
    import numpy as np
    
    # Calculate statistics
    valid_data = array[~np.isnan(array)]
    stats = {
        'mean': np.mean(valid_data),
        'std': np.std(valid_data),
        'min': np.min(valid_data),
        'max': np.max(valid_data),
        'p10': np.percentile(valid_data, 10),
        'p50': np.percentile(valid_data, 50),
        'p90': np.percentile(valid_data, 90),
    }
    
    print(f"Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}")
    
    # Export for visualization
    # np.save('horizon_data.npy', array)
    # print("\nData exported to horizon_data.npy")


# Example 5: Error handling and validation
def example_error_handling():
    """
    Example showing proper error handling when working with bulk data.
    """
    from dsis_model_sdk.models.common import HorizonData3D
    from dsis_model_sdk.protobuf import decode_horizon_data, PROTOBUF_AVAILABLE
    
    # Check if protobuf support is available
    if not PROTOBUF_AVAILABLE:
        print("Protobuf support not available!")
        print("Install with: pip install dsis-schemas[protobuf]")
        return
    
    # Try to decode data with error handling
    try:
        horizon = HorizonData3D.from_dict(api_response)
        
        # Check if data field exists
        if not horizon.data:
            print("No bulk data available for this horizon")
            return
        
        # Decode with error handling
        decoded = decode_horizon_data(horizon.data)
        
        # Validate decoded data
        if decoded.mode == decoded.FULL:
            if not decoded.lines:
                print("Warning: FULL mode but no lines data")
        elif decoded.mode == decoded.SAMPLES:
            if not decoded.HasField('samples'):
                print("Warning: SAMPLES mode but no samples data")
        
        print("Data decoded successfully!")
        
    except ValueError as e:
        print(f"Validation error: {e}")
    except Exception as e:
        print(f"Error decoding bulk data: {e}")


if __name__ == '__main__':
    print("=" * 80)
    print("DSIS Protobuf Bulk Data Examples")
    print("=" * 80)
    
    print("\n\n" + "=" * 80)
    print("Example 1: Horizon Data")
    print("=" * 80)
    # example_horizon_data()  # Uncomment to run
    
    print("\n\n" + "=" * 80)
    print("Example 2: Log Curve Data")
    print("=" * 80)
    # example_log_curve_data()  # Uncomment to run
    
    print("\n\n" + "=" * 80)
    print("Example 3: 3D Seismic Data")
    print("=" * 80)
    # example_seismic_3d_data()  # Uncomment to run
    
    print("\n\n" + "=" * 80)
    print("Example 4: Complete Workflow")
    print("=" * 80)
    # example_complete_workflow()  # Uncomment to run
    
    print("\n\n" + "=" * 80)
    print("Example 5: Error Handling")
    print("=" * 80)
    # example_error_handling()  # Uncomment to run
