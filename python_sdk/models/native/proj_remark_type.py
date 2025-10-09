"""
ProjRemarkType Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.ProjRemarkType
Generated on: 2025-10-09T21:15:04.861527
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class ProjRemarkType(BaseModel):
    """
    OW5000.ProjRemarkType model.

    Represents data from the OW5000.ProjRemarkType schema.
    """

    # Schema metadata
    _schema_title = "OW5000.ProjRemarkType"
    _schema_id = "#/definitions/OW5000_ProjRemarkType"
    _sql_table_name = "OW5000_ProjRemarkType"

    # Model fields
    remark_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    remark_type_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2000)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
