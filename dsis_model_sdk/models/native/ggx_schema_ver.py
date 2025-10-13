"""
GgxSchemaVer Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.GgxSchemaVer
Generated on: 2025-10-09T21:15:04.719821
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class GgxSchemaVer(BaseModel):
    """
    OW5000.GgxSchemaVer model.

    Represents data from the OW5000.GgxSchemaVer schema.
    """

    # Schema metadata
    _schema_title = "OW5000.GgxSchemaVer"
    _schema_id = "#/definitions/OW5000_GgxSchemaVer"
    _sql_table_name = "OW5000_GgxSchemaVer"

    # Model fields
    sqlfile: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=80)
    comments: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=240)
    row_changed_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
