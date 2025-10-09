"""
VDBResources Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYSADMIN.VDBResources
Generated on: 2025-10-09T21:15:05.071487
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class VDBResources(BaseModel):
    """
    SYSADMIN.VDBResources model.

    Represents data from the SYSADMIN.VDBResources schema.
    """

    # Schema metadata
    _schema_title = "SYSADMIN.VDBResources"
    _schema_id = "#/definitions/SYSADMIN_VDBResources"
    _sql_table_name = "SYSADMIN_VDBResources"

    # Model fields
    resourcePath: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    contents: Optional[bytes] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BINARY', 'BLOB', 'LONGVARBINARY', 'VARBINARY')", max_length=2147483647)
