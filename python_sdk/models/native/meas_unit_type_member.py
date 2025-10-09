"""
MeasUnitTypeMember Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.MeasUnitTypeMember
Generated on: 2025-10-09T21:15:04.799348
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class MeasUnitTypeMember(BaseModel):
    """
    OW5000.MeasUnitTypeMember model.

    Represents data from the OW5000.MeasUnitTypeMember schema.
    """

    # Schema metadata
    _schema_title = "OW5000.MeasUnitTypeMember"
    _schema_id = "#/definitions/OW5000_MeasUnitTypeMember"
    _sql_table_name = "OW5000_MeasUnitTypeMember"

    # Model fields
    unit_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    unit_type_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
