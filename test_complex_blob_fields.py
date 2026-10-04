#!/usr/bin/env python3
"""
Regression test for the complex-type BLOB fields fix.

Guards against two ways this can regress:
1. The JSON schema for a fixed field reverting to {"type":"string","format":"binary"}
   (e.g. from a fresh, unmodified re-export of the DDL into JSON Schema).
2. The generated Pydantic model rejecting a decoded-JSON dict payload for that field.

See CHANGELOG.md [0.0.10] for background.
"""

import json
import sys
from pathlib import Path

from pydantic import ValidationError

from dsis_model_sdk.models.common import (
    BinsetGrid3DGrid,
    DirectionalSurvey,
    FaultPlaneTrimesh,
    FaultSegment,
    FaultTrimesh,
    MappingPolygon,
    PositionLog,
    Project,
    Seis2DLine,
    TimeDepthTable,
    Well,
    Wellbore,
    WellCoreAnalysis,
    WellCoreDescription,
    Wellplanlocation,
)

SCHEMAS_DIR = Path(__file__).parent / "common-model-json-schemas"

# schema title -> complex-type fields that must be JSON objects, not binary
COMPLEX_BLOB_FIELDS = {
    "OpenWorksCommonModel.Project": ["spatial"],
    "OpenWorksCommonModel.Well": ["surface_location_point"],
    "OpenWorksCommonModel.Wellbore": ["bh_location_point"],
    "OpenWorksCommonModel.DirectionalSurvey": ["data"],
    "OpenWorksCommonModel.PositionLog": ["data"],
    "OpenWorksCommonModel.TimeDepthTable": ["data"],
    "OpenWorksCommonModel.WellCoreAnalysis": ["data"],
    "OpenWorksCommonModel.WellCoreDescription": ["data"],
    "OpenWorksCommonModel.BinsetGrid3DGrid": ["spatial"],
    "OpenWorksCommonModel.Seis2DLine": ["shotpoints", "orig_shotpoints", "mappings", "spatial"],
    "OpenWorksCommonModel.FaultPlaneTrimesh": ["vertices", "triangles"],
    "OpenWorksCommonModel.FaultTrimesh": ["vertices", "triangles"],
    "OpenWorksCommonModel.FaultSegment": ["data"],
    "OpenWorksCommonModel.MappingPolygon": ["data", "spatial"],
    "OpenWorksCommonModel.wellplanlocation": ["spatial"],
}

# entity schema file name -> list of (class, required kwargs, {field: sample dict value})
MODEL_CASES = [
    (Project, {"project_name": "P1"}, {"spatial": {"linestring": [{"x": 1.0, "y": 2.0}]}}),
    (Well, {"well_uwi": "W1"}, {"surface_location_point": {"x": 1.0, "y": 2.0}}),
    (Wellbore, {"well_native_uid": "w1", "wellbore_uwi": "WB1"}, {"bh_location_point": {"x": 1.0, "y": 2.0}}),
    (
        DirectionalSurvey,
        {
            "wellbore_native_uid": "w1", "survey_name": "s", "survey_calc_method": "m",
            "north_reference": "true", "npts": 1, "md_unit": "ft",
            "inclination_unit": "deg", "azimuth_unit": "deg",
        },
        {"data": {"md": [1.0], "tvd": [1.0]}},
    ),
    (
        PositionLog,
        {"wellbore_native_uid": "w1", "npts": 1, "md_unit": "ft", "tvd_unit": "ft", "xy_offset_unit": "ft"},
        {"data": {"md": [1.0], "tvd": [1.0]}},
    ),
    (
        TimeDepthTable,
        {"wellbore_native_uid": "w1", "td_name": "t", "datum": 0.0, "npts": 1, "depth_unit": "ft", "time_unit": "ms"},
        {"data": {"md": [1.0], "time": [1.0]}},
    ),
    (
        WellCoreAnalysis,
        {
            "wellbore_native_uid": "w1", "wellbore_uwi": "WB1", "wellcore_native_uid": "c1",
            "core_id": "c1", "data_source": "SRC", "analysis_obs_no": 1, "sample_analysis_obs_no": 1,
        },
        {"data": {"top_depth": [1.0], "sample_number": ["1"]}},
    ),
    (
        WellCoreDescription,
        {"wellbore_native_uid": "w1", "wellcore_native_uid": "c1", "core_id": "c1", "data_source": "SRC"},
        {"data": {"top_depth": [1.0], "well_status": ["ok"]}},
    ),
    (
        BinsetGrid3DGrid,
        {"seismic3dsurvey_native_uid": "s1"},
        {"spatial": {"linestringzm": [{"x": 1.0, "y": 2.0, "z": 3.0, "m": 0.0}]}},
    ),
    (
        Seis2DLine,
        {"seismic_line_name": "L1", "seismic2dsurvey_native_uid": "s1"},
        {
            "shotpoints": {"shotpoint": [1.0], "x": [1.0], "y": [1.0]},
            "orig_shotpoints": {"shotpoint": [1.0], "x": [1.0], "y": [1.0]},
            "mappings": {"shotpoint": [1.0], "trace": [1.0]},
            "spatial": {"x": 1.0, "y": 2.0, "z": 3.0, "m": 0.0},
        },
    ),
    (
        FaultPlaneTrimesh,
        {
            "fault_name": "F1", "interpretation_version_name": "v1", "data_source": "SRC",
            "domain": "TIME", "min_x": 0.0, "max_x": 1.0, "min_y": 0.0, "max_y": 1.0,
            "min_z": 0.0, "max_z": 1.0, "z_unit": "ft",
        },
        {
            "vertices": {"x": [1.0], "y": [2.0], "z": [3.0]},
            "triangles": {"vertex_1": [0], "vertex_2": [1], "vertex_3": [2]},
        },
    ),
    (
        FaultTrimesh,
        {
            "fault_plane_id": "fp1", "min_wrk_prj_x": 0.0, "max_wrk_prj_x": 1.0,
            "min_wrk_prj_y": 0.0, "max_wrk_prj_y": 1.0, "min_z": 0.0, "max_z": 1.0,
            "z_unit": "ft", "z_domain": "TIME",
        },
        {
            "vertices": {"x": [1.0], "y": [2.0], "z": [3.0]},
            "triangles": {"vertex_1": [0], "vertex_2": [1], "vertex_3": [2]},
        },
    ),
    (
        FaultSegment,
        {
            "min_x": 0.0, "max_x": 1.0, "min_y": 0.0, "max_y": 1.0, "min_z": 0.0, "max_z": 1.0,
            "crs": "WGS84", "z_domain": "TIME", "z_unit": "ms",
        },
        {"data": {"x": [1.0], "y": [2.0], "z": [3.0]}},
    ),
    (
        MappingPolygon,
        {"mappingpolygonset_native_uid": "s1", "polygon_seq_no": 1, "num_points": 4, "crs": "WGS84"},
        {
            "data": {"x_coord": [1.0], "y_coord": [2.0], "z_value": [3.0], "throw_direction": ["N"]},
            "spatial": {"x": [1.0], "y": [2.0], "z": [3.0], "geo_type": "LINESTRING"},
        },
    ),
    (Wellplanlocation, {}, {"spatial": {"x": 1.0, "y": 2.0}}),
]


def test_schemas_declare_object_type() -> bool:
    """The JSON Schema for each affected field must be an object, not binary."""
    all_schemas = json.loads((SCHEMAS_DIR / "all_schemas.json").read_text())
    ok = True
    for title, fields in COMPLEX_BLOB_FIELDS.items():
        schema = all_schemas.get(title)
        if schema is None:
            print(f"❌ schema missing from all_schemas.json: {title}")
            ok = False
            continue
        for field_name in fields:
            prop = schema["properties"].get(field_name, {})
            if prop.get("type") != "object" or prop.get("format") == "binary":
                print(f"❌ {title}.{field_name} is not typed as object: {prop}")
                ok = False
    if ok:
        print(f"✅ All {sum(len(v) for v in COMPLEX_BLOB_FIELDS.values())} complex-type fields declared as object in all_schemas.json")
    return ok


def test_models_accept_dict_payloads() -> bool:
    """Each fixed model must instantiate successfully with dict payloads (not bytes)."""
    ok = True
    for model_cls, required_kwargs, dict_fields in MODEL_CASES:
        try:
            instance = model_cls(**required_kwargs, **dict_fields)
            for field_name, expected in dict_fields.items():
                assert getattr(instance, field_name) == expected
            print(f"✅ {model_cls.__name__} accepts dict payload for {list(dict_fields)}")
        except (ValidationError, AssertionError) as e:
            print(f"❌ {model_cls.__name__} failed: {e}")
            ok = False
    return ok


def main() -> bool:
    print("🧪 Testing complex-type BLOB field fix (dict, not bytes)\n")
    results = [
        ("Schema declarations", test_schemas_declare_object_type()),
        ("Model instantiation", test_models_accept_dict_payloads()),
    ]
    passed = sum(1 for _, r in results if r)
    print(f"\nOverall: {passed}/{len(results)} test groups passed")
    return passed == len(results)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
