"""
HorizonCatalog Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.HorizonCatalog
Generated on: 2026-04-17T09:03:28.655533
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class HorizonCatalog(BaseModel):
    """
    OW5000.HorizonCatalog model.

    Represents data from the OW5000.HorizonCatalog schema.
    """

    # Schema metadata
    _schema_title = "OW5000.HorizonCatalog"
    _schema_id = "#/definitions/OW5000_HorizonCatalog"
    _sql_table_name = "OW5000_HorizonCatalog"

    # Model fields
    horizon_attr_hdr_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    max_value: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')")
    min_value: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')")
    max_amplitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')")
    min_amplitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
