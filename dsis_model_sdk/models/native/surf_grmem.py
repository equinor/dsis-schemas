"""
SurfGrmem Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.SurfGrmem
Generated on: 2025-10-09T21:15:04.967387
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SurfGrmem(BaseModel):
    """
    OW5000.SurfGrmem model.

    Represents data from the OW5000.SurfGrmem schema.
    """

    # Schema metadata
    _schema_title = "OW5000.SurfGrmem"
    _schema_id = "#/definitions/OW5000_SurfGrmem"
    _sql_table_name = "OW5000_SurfGrmem"

    # Model fields
    alias_group_surface: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    priority_seq: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    member_surface: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
