"""
RelativeUncertaintyAll Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.RelativeUncertaintyAll
Generated on: 2025-10-09T21:15:04.929417
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class RelativeUncertaintyAll(BaseModel):
    """
    OW5000.RelativeUncertaintyAll model.

    Represents data from the OW5000.RelativeUncertaintyAll schema.
    """

    # Schema metadata
    _schema_title = "OW5000.RelativeUncertaintyAll"
    _schema_id = "#/definitions/OW5000_RelativeUncertaintyAll"
    _sql_table_name = "OW5000_RelativeUncertaintyAll"

    # Model fields
    target_a_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    target_b_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
