"""
Plannedwellslots Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.plannedwellslots
Generated on: 2025-10-09T21:14:54.992743
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Plannedwellslots(BaseModel):
    """
    OpenWorksCommonModel.plannedwellslots model.

    Represents data from the OpenWorksCommonModel.plannedwellslots schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.plannedwellslots"
    _schema_id = "#/definitions/OpenWorksCommonModel_plannedwellslots"
    _sql_table_name = "OpenWorksCommonModel_plannedwellslots"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    wellplan_site_native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    slot_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    ground_level: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
