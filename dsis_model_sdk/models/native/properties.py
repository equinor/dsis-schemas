"""
Properties Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.Properties
Generated on: 2025-10-09T21:15:05.066066
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Properties(BaseModel):
    """
    SYS.Properties model.

    Represents data from the SYS.Properties schema.
    """

    # Schema metadata
    _schema_title = "SYS.Properties"
    _schema_id = "#/definitions/SYS_Properties"
    _sql_table_name = "SYS_Properties"

    # Model fields
    Name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    Value: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    UID: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50)
    ClobValue: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CLOB', 'LONGVARCHAR', 'LONGNVARCHAR', 'NCLOB', 'SQLXML')", max_length=2097152)
