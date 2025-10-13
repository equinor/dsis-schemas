"""
Well Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.Well
Generated on: 2025-10-09T21:15:05.000841
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Well(BaseModel):
    """
    OW5000.Well model.

    Represents data from the OW5000.Well schema.
    """

    # Schema metadata
    _schema_title = "OW5000.Well"
    _schema_id = "#/definitions/OW5000_Well"
    _sql_table_name = "OW5000_Well"

    # Model fields
    wellid: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=31)
    uwi: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=26)
    well_location_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    symbol: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    well_operator: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    state: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    county: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    elevation: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.01)
    elevation_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    elev_type: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2)
    x_coordinate: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    x_coordinate_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    y_coordinate: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    y_coordinate_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    total_depth: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.01)
    total_depth_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    plugged_back_td: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.01)
    plugged_back_td_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    completion_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    latitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    latitude_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    longitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    longitude_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    latitude_bh: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    latitude_bh_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    longitude_bh: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    longitude_bh_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    x_coord_bh: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    x_coord_bh_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    y_coord_bh: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    y_coord_bh_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    orig_x_lon: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    orig_x_lon_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    orig_y_lat: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    orig_y_lat_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    orig_bh_x_lon: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    orig_bh_x_lon_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    orig_bh_y_lat: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-09)
    orig_bh_y_lat_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    orig_crs_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    orig_bh_crs_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    well_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    well_number: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=10)
    common_well_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=80)
    platform_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    current_status: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    country: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    field: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=60)
    data_source: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
