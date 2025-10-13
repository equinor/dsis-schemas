"""
GeologicalEstimatorPtAll Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.GeologicalEstimatorPtAll
Generated on: 2025-10-09T21:15:04.716118
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class GeologicalEstimatorPtAll(BaseModel):
    """
    OW5000.GeologicalEstimatorPtAll model.

    Represents data from the OW5000.GeologicalEstimatorPtAll schema.
    """

    # Schema metadata
    _schema_title = "OW5000.GeologicalEstimatorPtAll"
    _schema_id = "#/definitions/OW5000_GeologicalEstimatorPtAll"
    _sql_table_name = "OW5000_GeologicalEstimatorPtAll"

    # Model fields
    target_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_pt_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    border_pick_unc: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    border_pick_unc_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    border_tolerance_risk: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    border_tolerance_risk_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    border_hardline: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
