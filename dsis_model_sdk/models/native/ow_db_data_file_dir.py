"""
OwDbDataFileDir Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.OwDbDataFileDir
Generated on: 2025-10-09T21:15:04.815649
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class OwDbDataFileDir(BaseModel):
    """
    OW5000.OwDbDataFileDir model.

    Represents data from the OW5000.OwDbDataFileDir schema.
    """

    # Schema metadata
    _schema_title = "OW5000.OwDbDataFileDir"
    _schema_id = "#/definitions/OW5000_OwDbDataFileDir"
    _sql_table_name = "OW5000_OwDbDataFileDir"

    # Model fields
    dir_path: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    file_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=8)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
