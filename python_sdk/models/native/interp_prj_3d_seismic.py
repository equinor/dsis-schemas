"""
InterpPrj3DSeismic Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.InterpPrj3DSeismic
Generated on: 2025-10-09T21:15:04.755968
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class InterpPrj3DSeismic(BaseModel):
    """
    OW5000.InterpPrj3DSeismic model.

    Represents data from the OW5000.InterpPrj3DSeismic schema.
    """

    # Schema metadata
    _schema_title = "OW5000.InterpPrj3DSeismic"
    _schema_id = "#/definitions/OW5000_InterpPrj3DSeismic"
    _sql_table_name = "OW5000_InterpPrj3DSeismic"

    # Model fields
    interpretation_project_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    seismic_3d_survey_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
