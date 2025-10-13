"""
VirtualDatabases Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.VirtualDatabases
Generated on: 2025-10-09T21:15:05.068330
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class VirtualDatabases(BaseModel):
    """
    SYS.VirtualDatabases model.

    Represents data from the SYS.VirtualDatabases schema.
    """

    # Schema metadata
    _schema_title = "SYS.VirtualDatabases"
    _schema_id = "#/definitions/SYS_VirtualDatabases"
    _sql_table_name = "SYS_VirtualDatabases"

    # Model fields
    Name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    Version: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50)
    Description: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    LoadingTimestamp: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    ActiveTimestamp: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
