# Changelog

All notable changes to `dsis-schemas` will be documented in this file.

## [0.0.8] - 2026-04-09

### Added
- Support for converting LGC protobuf data to numpy arrays
- LGC protobuf tests with real-world test data

## [0.0.7] - 2026-03-17

### Fixed
- Read all messages correctly in `LgcStructure` decoding
- Extended the read-all-messages fix to remaining protobuf types

### Changed
- Dropped support for Python 3.8

## [0.0.6] - 2025-12-10

### Changed
- Updated protobuf dependency version to `>=6.33.1`

## [0.0.5] - 2025-12-08

### Fixed
- Pinned protobuf dependency to `>=5.28.3`

## [0.0.4] - 2025-12-08

### Added
- Comprehensive protobuf definitions and decoders

## [0.0.3] - 2025-11-19

### Fixed
- Protobuf enum access bugs

## [0.0.2] - 2025-10-18

### Added
- Protocol Buffers support for bulk data decoding
- Comprehensive PyPI package test suite

### Changed
- Updated all imports from `python_sdk` to `dsis_model_sdk`
- Updated documentation

## [0.0.1] - 2025-10-18

### Added
- Initial release
- Python SDK with dual model support (OpenWorks Common Model + OW5000 Native Model)
- Required field support
- PyPI publishing workflow
- Renamed package to `dsis-schemas` to match PyPI publisher
