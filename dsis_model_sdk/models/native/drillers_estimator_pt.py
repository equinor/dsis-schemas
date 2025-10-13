"""
DrillersEstimatorPt Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.DrillersEstimatorPt
Generated on: 2025-10-09T21:15:04.630515
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class DrillersEstimatorPt(BaseModel):
    """
    OW5000.DrillersEstimatorPt model.

    Represents data from the OW5000.DrillersEstimatorPt schema.
    """

    # Schema metadata
    _schema_title = "OW5000.DrillersEstimatorPt"
    _schema_id = "#/definitions/OW5000_DrillersEstimatorPt"
    _sql_table_name = "OW5000_DrillersEstimatorPt"

    # Model fields
    target_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_pt_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_corner_u: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    target_corner_u_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    target_corner_v: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    target_corner_v_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
