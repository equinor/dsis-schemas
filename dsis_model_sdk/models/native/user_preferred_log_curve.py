"""
UserPreferredLogCurve Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.UserPreferredLogCurve
Generated on: 2025-10-09T21:15:04.987365
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class UserPreferredLogCurve(BaseModel):
    """
    OW5000.UserPreferredLogCurve model.

    Represents data from the OW5000.UserPreferredLogCurve schema.
    """

    # Schema metadata
    _schema_title = "OW5000.UserPreferredLogCurve"
    _schema_id = "#/definitions/OW5000_UserPreferredLogCurve"
    _sql_table_name = "OW5000_UserPreferredLogCurve"

    # Model fields
    log_crv_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    log_crv_version: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
