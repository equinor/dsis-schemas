"""
HorizonCatalog Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.HorizonCatalog
Generated on: 2025-10-09T21:15:04.735212
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
    max_value: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    min_value: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    max_amplitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    min_amplitude: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=1e-05)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
