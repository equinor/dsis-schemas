"""
REQUESTS Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYSADMIN.REQUESTS
Generated on: 2025-10-09T21:15:05.069392
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class REQUESTS(BaseModel):
    """
    SYSADMIN.REQUESTS model.

    Represents data from the SYSADMIN.REQUESTS schema.
    """

    # Schema metadata
    _schema_title = "SYSADMIN.REQUESTS"
    _schema_id = "#/definitions/SYSADMIN_REQUESTS"
    _sql_table_name = "SYSADMIN_REQUESTS"

    # Model fields
    VDBName: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    SessionId: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    ExecutionId: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    Command: str = Field(description="SQL Type: DBAPITYPEOBJECT('CLOB', 'LONGVARCHAR', 'LONGNVARCHAR', 'NCLOB', 'SQLXML')", max_length=2147483647)
    StartTimestamp: datetime = Field(description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    TransactionId: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    ProcessingState: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    ThreadState: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    IsSource: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
