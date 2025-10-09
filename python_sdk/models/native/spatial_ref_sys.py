"""
SpatialRefSys Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.spatial_ref_sys
Generated on: 2025-10-09T21:15:05.068742
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SpatialRefSys(BaseModel):
    """
    SYS.spatial_ref_sys model.

    Represents data from the SYS.spatial_ref_sys schema.
    """

    # Schema metadata
    _schema_title = "SYS.spatial_ref_sys"
    _schema_id = "#/definitions/SYS_spatial_ref_sys"
    _sql_table_name = "SYS_spatial_ref_sys"

    # Model fields
    srid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    auth_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    auth_srid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    srtext: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2048)
    proj4text: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2048)
