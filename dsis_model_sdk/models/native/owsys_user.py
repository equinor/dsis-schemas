"""
OwsysUser Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.OwsysUser
Generated on: 2025-10-09T21:15:04.821141
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class OwsysUser(BaseModel):
    """
    OW5000.OwsysUser model.

    Represents data from the OW5000.OwsysUser schema.
    """

    # Schema metadata
    _schema_title = "OW5000.OwsysUser"
    _schema_id = "#/definitions/OW5000_OwsysUser"
    _sql_table_name = "OW5000_OwsysUser"

    # Model fields
    user_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
