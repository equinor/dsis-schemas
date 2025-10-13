"""
Seis2DStorageArea Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.Seis2DStorageArea
Generated on: 2025-10-09T21:15:04.935593
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Seis2DStorageArea(BaseModel):
    """
    OW5000.Seis2DStorageArea model.

    Represents data from the OW5000.Seis2DStorageArea schema.
    """

    # Schema metadata
    _schema_title = "OW5000.Seis2DStorageArea"
    _schema_id = "#/definitions/OW5000_Seis2DStorageArea"
    _sql_table_name = "OW5000_Seis2DStorageArea"

    # Model fields
    directory_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    seis_2d_storage_area_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    is_default: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
