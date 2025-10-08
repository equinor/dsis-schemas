"""
MeasSystemMember Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.MeasSystemMember
Generated on: 2025-10-08T21:10:50.333649
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class MeasSystemMember(BaseModel):
    """
    OW5000.MeasSystemMember model.
    
    Represents data from the OW5000.MeasSystemMember schema.
    """
    
    # Schema metadata
    _schema_title = "OW5000.MeasSystemMember"
    _schema_id = "#/definitions/OW5000_MeasSystemMember"
    _sql_table_name = "OW5000_MeasSystemMember"
    
    # Model fields
    id_field: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3, alias="id")
    unit_type_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    unit_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
