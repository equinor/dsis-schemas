#!/usr/bin/env bash
#
# Generate Python protobuf files from .proto definitions
#
# This script compiles Protocol Buffer definition files (.proto) into Python modules
# that can be used to decode binary bulk data from the DSIS API.
#
# Usage:
#   ./scripts/generate_protobuf.sh
#
# Requirements:
#   - protoc (Protocol Buffer compiler) must be installed
#   - Install with: brew install protobuf (macOS) or apt-get install protobuf-compiler (Linux)

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}Generating Python protobuf files...${NC}\n"

# Check if protoc is installed
if ! command -v protoc &> /dev/null; then
    echo -e "${RED}Error: protoc not found${NC}"
    echo "Please install Protocol Buffer compiler:"
    echo "  macOS:   brew install protobuf"
    echo "  Ubuntu:  sudo apt-get install protobuf-compiler"
    echo "  Windows: Download from https://github.com/protocolbuffers/protobuf/releases"
    exit 1
fi

echo -e "protoc version: $(protoc --version)"
echo ""

# Set directories
PROTO_DIR="protobuf-definitions"
OUTPUT_DIR="dsis_model_sdk/protobuf"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Generate from each proto file
echo -e "${YELLOW}Generating from horizon definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/horizon/HorizonData3D.proto"

echo -e "${YELLOW}Generating from logcurve definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/logcurve/LogCurves.proto"

echo -e "${YELLOW}Generating from seismic definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/seismic/SeismicData.proto" \
    "$PROTO_DIR/seismic/SeismicDataHeader.proto" \
    "$PROTO_DIR/seismic/SeismicDataHeader2D.proto"

echo -e "${YELLOW}Generating from tabular definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/tabular/LGCStructure.proto" \
    "$PROTO_DIR/tabular/PropertyTableSet.proto"

echo -e "${YELLOW}Generating from array definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/arrays/Array2FBuf.proto" \
    "$PROTO_DIR/arrays/Array2FBufList.proto" \
    "$PROTO_DIR/arrays/Array3BBuf.proto" \
    "$PROTO_DIR/arrays/Array3FBuf.proto" \
    "$PROTO_DIR/arrays/Array3FBufList.proto" \
    "$PROTO_DIR/arrays/Array3IBuf.proto" \
    "$PROTO_DIR/arrays/Array3SBuf.proto"

echo -e "${YELLOW}Generating from geometry definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/geometry/FaultPlane.proto" \
    "$PROTO_DIR/geometry/PolyMesh.proto" \
    "$PROTO_DIR/geometry/FractureNetwork.proto"

echo -e "${YELLOW}Generating from common definitions...${NC}"
protoc --python_out="$OUTPUT_DIR" \
    "$PROTO_DIR/common/CRS.proto"

# Flatten directory structure (protoc creates nested dirs)
if [ -d "$OUTPUT_DIR/protobuf_definitions" ]; then
    echo -e "${YELLOW}Flattening directory structure...${NC}"
    
    # Move all _pb2.py files to output root
    find "$OUTPUT_DIR/protobuf_definitions" -name "*_pb2.py" -exec mv {} "$OUTPUT_DIR/" \;
    
    # Remove nested directory
    rm -rf "$OUTPUT_DIR/protobuf_definitions"
fi

# List generated files
echo ""
echo -e "${GREEN}Generated files:${NC}"
ls -lh "$OUTPUT_DIR"/*_pb2.py | awk '{print "  " $9 " (" $5 ")"}'

# Verify __init__.py exists
if [ ! -f "$OUTPUT_DIR/__init__.py" ]; then
    echo ""
    echo -e "${RED}Warning: $OUTPUT_DIR/__init__.py not found${NC}"
    echo "The __init__.py file should exist and provide decoder functions."
else
    echo ""
    echo -e "${GREEN}✓ Protobuf package ready${NC}"
fi

echo ""
echo -e "${GREEN}✓ Protobuf generation complete!${NC}"
echo ""
echo "Usage:"
echo "  from dsis_model_sdk.protobuf import decode_horizon_data"
echo "  decoded = decode_horizon_data(binary_data)"
