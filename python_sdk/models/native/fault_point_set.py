"""
FaultPointSet Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.FaultPointSet
Generated on: 2025-10-09T21:15:04.683479
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class FaultPointSet(BaseModel):
    """
    OW5000.FaultPointSet model.

    Represents data from the OW5000.FaultPointSet schema.
    """

    # Schema metadata
    _schema_title = "OW5000.FaultPointSet"
    _schema_id = "#/definitions/OW5000_FaultPointSet"
    _sql_table_name = "OW5000_FaultPointSet"

    # Model fields
    fault_surf_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    fault_cut_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    fault_point_set_seq: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
