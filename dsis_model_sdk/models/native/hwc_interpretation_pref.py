"""
HwcInterpretationPref Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.HwcInterpretationPref
Generated on: 2025-10-09T21:15:04.742197
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class HwcInterpretationPref(BaseModel):
    """
    OW5000.HwcInterpretationPref model.

    Represents data from the OW5000.HwcInterpretationPref schema.
    """

    # Schema metadata
    _schema_title = "OW5000.HwcInterpretationPref"
    _schema_id = "#/definitions/OW5000_HwcInterpretationPref"
    _sql_table_name = "OW5000_HwcInterpretationPref"

    # Model fields
    well_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=31)
    pick_surf_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=255)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    hwc_intrp_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    row_lock_ind: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
