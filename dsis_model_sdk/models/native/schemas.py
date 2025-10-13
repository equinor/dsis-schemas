"""
Schemas Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.Schemas
Generated on: 2025-10-09T21:15:05.067449
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Schemas(BaseModel):
    """
    SYS.Schemas model.

    Represents data from the SYS.Schemas schema.
    """

    # Schema metadata
    _schema_title = "SYS.Schemas"
    _schema_id = "#/definitions/SYS_Schemas"
    _sql_table_name = "SYS_Schemas"

    # Model fields
    VDBName: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    Name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    IsPhysical: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    UID: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50)
    Description: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    PrimaryMetamodelURI: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
