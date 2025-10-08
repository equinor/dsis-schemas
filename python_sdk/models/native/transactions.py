"""
TRANSACTIONS Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYSADMIN.TRANSACTIONS
Generated on: 2025-10-08T21:10:50.531447
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class TRANSACTIONS(BaseModel):
    """
    SYSADMIN.TRANSACTIONS model.
    
    Represents data from the SYSADMIN.TRANSACTIONS schema.
    """
    
    # Schema metadata
    _schema_title = "SYSADMIN.TRANSACTIONS"
    _schema_id = "#/definitions/SYSADMIN_TRANSACTIONS"
    _sql_table_name = "SYSADMIN_TRANSACTIONS"
    
    # Model fields
    TransactionId: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    SessionId: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    StartTimestamp: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    Scope: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
