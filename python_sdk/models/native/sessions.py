"""
SESSIONS Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYSADMIN.SESSIONS
Generated on: 2025-10-09T21:15:05.069668
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SESSIONS(BaseModel):
    """
    SYSADMIN.SESSIONS model.

    Represents data from the SYSADMIN.SESSIONS schema.
    """

    # Schema metadata
    _schema_title = "SYSADMIN.SESSIONS"
    _schema_id = "#/definitions/SYSADMIN_SESSIONS"
    _sql_table_name = "SYSADMIN_SESSIONS"

    # Model fields
    VDBName: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    SessionId: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    UserName: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    CreatedTime: datetime = Field(description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    ApplicationName: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    IPAddress: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
