"""
HorizonChangeLog Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.HorizonChangeLog
Generated on: 2025-10-09T21:15:04.735644
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class HorizonChangeLog(BaseModel):
    """
    OW5000.HorizonChangeLog model.

    Represents data from the OW5000.HorizonChangeLog schema.
    """

    # Schema metadata
    _schema_title = "OW5000.HorizonChangeLog"
    _schema_id = "#/definitions/OW5000_HorizonChangeLog"
    _sql_table_name = "OW5000_HorizonChangeLog"

    # Model fields
    horizon_change_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    horizon_data_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    horizon_update_user_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    horizon_update_timestamp: datetime = Field(description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    min_line: float = Field(description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    max_line: float = Field(description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    min_trace: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    max_trace: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    sync_node_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
