"""
GgxWellMetadata Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.GgxWellMetadata
Generated on: 2025-10-09T21:15:04.720449
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class GgxWellMetadata(BaseModel):
    """
    OW5000.GgxWellMetadata model.

    Represents data from the OW5000.GgxWellMetadata schema.
    """

    # Schema metadata
    _schema_title = "OW5000.GgxWellMetadata"
    _schema_id = "#/definitions/OW5000_GgxWellMetadata"
    _sql_table_name = "OW5000_GgxWellMetadata"

    # Model fields
    data_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=60)
    count: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    flag: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    delete_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
