"""
DrillersEstimatorPtAll Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.DrillersEstimatorPtAll
Generated on: 2025-10-09T21:15:04.632003
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class DrillersEstimatorPtAll(BaseModel):
    """
    OW5000.DrillersEstimatorPtAll model.

    Represents data from the OW5000.DrillersEstimatorPtAll schema.
    """

    # Schema metadata
    _schema_title = "OW5000.DrillersEstimatorPtAll"
    _schema_id = "#/definitions/OW5000_DrillersEstimatorPtAll"
    _sql_table_name = "OW5000_DrillersEstimatorPtAll"

    # Model fields
    target_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_pt_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_corner_u: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    target_corner_u_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    target_corner_v: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    target_corner_v_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
