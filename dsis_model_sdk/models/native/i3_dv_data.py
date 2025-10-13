"""
I3DVData Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.I3DVData
Generated on: 2025-10-09T21:15:04.744416
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class I3DVData(BaseModel):
    """
    OW5000.I3DVData model.

    Represents data from the OW5000.I3DVData schema.
    """

    # Schema metadata
    _schema_title = "OW5000.I3DVData"
    _schema_id = "#/definitions/OW5000_I3DVData"
    _sql_table_name = "OW5000_I3DVData"

    # Model fields
    i3dv_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    i3dv_data_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    i3dv_data_type: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
