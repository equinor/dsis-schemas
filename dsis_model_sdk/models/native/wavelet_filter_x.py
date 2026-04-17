"""
WaveletFilterX Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.WaveletFilterX
Generated on: 2026-04-17T09:03:29.063523
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class WaveletFilterX(BaseModel):
    """
    OW5000.WaveletFilterX model.

    Represents data from the OW5000.WaveletFilterX schema.
    """

    # Schema metadata
    _schema_title = "OW5000.WaveletFilterX"
    _schema_id = "#/definitions/OW5000_WaveletFilterX"
    _sql_table_name = "OW5000_WaveletFilterX"

    # Model fields
    seismic_fcl_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    wavelet_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
