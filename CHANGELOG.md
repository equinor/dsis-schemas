# Changelog

All notable changes to `dsis-schemas` will be documented in this file.

## [0.0.10] - 2026-10-04

### Fixed
- Complex-type BLOB fields (`isComplexType=true` in the DDL) were mis-typed as `bytes`/binary instead of the decoded JSON objects DSIS actually serves, causing `ValidationError` on `Model(**row)`. Affected fields now type as `Optional[Dict[str, Any]]`: `FaultSegment.data`, `FaultPlaneTrimesh.vertices`/`.triangles`, `FaultTrimesh.vertices`/`.triangles`, `MappingPolygon.data`/`.spatial`, `Project.spatial`, `Well.surface_location_point`, `Wellbore.bh_location_point`, `DirectionalSurvey.data`, `PositionLog.data`, `TimeDepthTable.data`, `WellCoreAnalysis.data`, `WellCoreDescription.data`, `BinsetGrid3DGrid.spatial`, `Seis2DLine.shotpoints`/`.orig_shotpoints`/`.mappings`/`.spatial`, `wellplanlocation.spatial`. Also dropped `data` from `required` on entities where it isn't returned without an explicit `$select`.
- Truly-binary BLOBs (e.g. `HorizonData3D`, `LogCurve`, `SeismicData`, served as protobuf) are unaffected and remain `bytes`.

### Added
- `test_complex_blob_fields.py`: regression test asserting the affected JSON schemas stay typed as `object` and that each generated model accepts a dict payload for the fixed fields.

### Removed
- Obsolete `test_sdk_structure.py`, which referenced a stale `python_sdk/` package layout and was fully superseded by `test_required_fields.py` / `test_pypi_package.py`.

### Known gaps
- Root cause is still open: `generate_sdk.py`/`type_mapping.py` are untouched, so a fresh re-export of the JSON schemas from the DDL (outside this repo) will drop `isComplexType`/`elementStruct` again and regress these fields back to `bytes`. `test_complex_blob_fields.py` is a tripwire for this, not a permanent fix.
- Native model (OW5000) checked and left unchanged: `models/native/fault_segment.py` and `models/native/mapping_polygon.py` still type `spatial` as `Optional[bytes]`. The native DDL (`OW_NativeExtension_10_3.ddl`) carries no `isComplexType` OPTIONS for these fields at all (unlike the common model), so there's no DDL evidence either way — needs live verification against DEV before touching.

## [0.0.9] - 2026-04-17

### Changed
- Version bump only (no changelog entry recorded at the time).

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
