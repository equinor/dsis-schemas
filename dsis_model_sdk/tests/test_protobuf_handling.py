import numpy as np
from dsis_model_sdk.protobuf import decode_lgc_structure
from dsis_model_sdk.utils.protobuf_decoders import lgc_structure_to_numpy2d
from pathlib import Path


class TestLGCProtobufDecodeAndConvert:
    """
    Test handling of LGC protobuf data, including decoding and conversion to numpy arrays.
    Use binary protobufs previously downloaded for surface grids in Volve public project
    """

    test_data_path = Path(__file__).parent / 'test_data'

    def test_decode_and_convert_cartesian_order(self) -> None:

        with open(self.test_data_path / 'VOLVE_PUBLIC_2636.bin', 'rb') as f:
            binary_data = f.read()

        # Test that decoding works and produces expected structure

        decoded = decode_lgc_structure(binary_data) # LGCStructure_pb2.LGCStructure

        assert len(decoded.elements) == 879
        assert len(decoded.elements[0].data_float) == 629
        assert decoded.elements[0].dataType == 2 # FLOAT

        grid_array: np.ndarray = lgc_structure_to_numpy2d(decoded)

        assert(grid_array.shape == (879, 629))
        assert(grid_array.dtype == np.float32)
        assert (int(np.sum(np.isnan(grid_array))) == 0) # no null values in this grid

        # Withthe default cartesian_origin=True, the bottom row is the first (0) and the top row the last (628)
        assert np.isclose(grid_array[0][0], -3177.0334)
        assert np.isclose(grid_array[0][628], -3438.7725)
        assert np.isclose(grid_array[878][0], -2770.6748)
        assert np.isclose(grid_array[878][628], -2649.9097)


    def test_decode_and_convert_keep_protobuf_order(self) -> None:

        with open(self.test_data_path / 'VOLVE_PUBLIC_2636.bin', 'rb') as f:
            binary_data = f.read()

        decoded = decode_lgc_structure(binary_data) # LGCStructure_pb2.LGCStructure

        assert len(decoded.elements) == 879
        assert len(decoded.elements[0].data_float) == 629
        assert decoded.elements[0].dataType == 2 # FLOAT

        grid_array: np.ndarray = lgc_structure_to_numpy2d(decoded, cartesian_origin=False)

        assert(grid_array.shape == (879, 629))
        assert(grid_array.dtype == np.float32)
        assert (int(np.sum(np.isnan(grid_array))) == 0) # no null values in this grid

        # With cartesian_origin=False, row order is as in the original protobuf (first row at top, last row at bottom)
        assert np.isclose(grid_array[0][628], -3177.0334)
        assert np.isclose(grid_array[0][0], -3438.7725)
        assert np.isclose(grid_array[878][628], -2770.6748)
        assert np.isclose(grid_array[878][0], -2649.9097)

    def test_decode_and_convert_replace_with_nan(self) -> None:

        with open(self.test_data_path / 'VOLVE_PUBLIC_2622.bin', 'rb') as f:
            binary_data = f.read()

        decoded = decode_lgc_structure(binary_data) # LGCStructure_pb2.LGCStructure

        assert len(decoded.elements) == 282
        assert len(decoded.elements[0].data_float) == 202
        assert decoded.elements[0].dataType == 2 # FLOAT

        grid_array: np.ndarray = lgc_structure_to_numpy2d(decoded, znon=-999.25, max_abs_value=1e15)

        assert(grid_array.shape == (282, 202))
        assert(grid_array.dtype == np.float32)

        # With znon and max_abs_value set, dummy values are converted to NaN as expected (36101 NaNs in this grid)
        assert (int(np.sum(np.isnan(grid_array))) == 36101)
        assert np.isnan(grid_array[0][0])
        assert np.isnan(grid_array[-1][-1])

    def test_decode_and_convert_without_nan_replacement(self) -> None:

        with open(self.test_data_path / 'VOLVE_PUBLIC_2622.bin', 'rb') as f:
            binary_data = f.read()

        decoded = decode_lgc_structure(binary_data) # LGCStructure_pb2.LGCStructure

        assert len(decoded.elements) == 282
        assert len(decoded.elements[0].data_float) == 202
        assert decoded.elements[0].dataType == 2 # FLOAT

        grid_array: np.ndarray = lgc_structure_to_numpy2d(decoded, znon=None, max_abs_value=None)

        assert(grid_array.shape == (282, 202))
        assert(grid_array.dtype == np.float32)

        # With znon=None and max_abs_value=None, dummy values are left as-is (no NaNs produced)
        assert (int(np.sum(np.isnan(grid_array))) == 0)
        assert not np.isnan(grid_array[0][0])
        assert not np.isnan(grid_array[-1][-1])



if __name__ == "__main__":
    print("Running TestProtobufHandling...")
    test = TestLGCProtobufDecodeAndConvert()
    test.test_decode_and_convert_cartesian_order()
    test.test_decode_and_convert_keep_protobuf_order()
    test.test_decode_and_convert_replace_with_nan()
    test.test_decode_and_convert_without_nan_replacement()