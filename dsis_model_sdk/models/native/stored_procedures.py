"""
StoredProcedures Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYSADMIN.StoredProcedures
Generated on: 2025-10-09T21:15:05.070048
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class StoredProcedures(BaseModel):
    """
    SYSADMIN.StoredProcedures model.

    Represents data from the SYSADMIN.StoredProcedures schema.
    """

    # Schema metadata
    _schema_title = "SYSADMIN.StoredProcedures"
    _schema_id = "#/definitions/SYSADMIN_StoredProcedures"
    _sql_table_name = "SYSADMIN_StoredProcedures"

    # Model fields
    VDBName: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    SchemaName: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    Name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    Body: str = Field(description="SQL Type: DBAPITYPEOBJECT('CLOB', 'LONGVARCHAR', 'LONGNVARCHAR', 'NCLOB', 'SQLXML')", max_length=2097152)
    UID: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50)
