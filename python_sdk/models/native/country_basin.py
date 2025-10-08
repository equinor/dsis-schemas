"""
CountryBasin Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.CountryBasin
Generated on: 2025-10-08T21:10:50.126293
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class CountryBasin(BaseModel):
    """
    OW5000.CountryBasin model.
    
    Represents data from the OW5000.CountryBasin schema.
    """
    
    # Schema metadata
    _schema_title = "OW5000.CountryBasin"
    _schema_id = "#/definitions/OW5000_CountryBasin"
    _sql_table_name = "OW5000_CountryBasin"
    
    # Model fields
    country: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    basin: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=60)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
