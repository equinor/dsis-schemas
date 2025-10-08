"""
GgxWellMetadata Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.GgxWellMetadata
Generated on: 2025-10-08T21:10:50.267647
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
    data_type: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=60)
    count: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    flag: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    delete_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
