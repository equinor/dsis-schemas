"""
AnalysisLogUse Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.AnalysisLogUse
Generated on: 2025-10-09T21:15:04.593435
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class AnalysisLogUse(BaseModel):
    """
    OW5000.AnalysisLogUse model.

    Represents data from the OW5000.AnalysisLogUse schema.
    """

    # Schema metadata
    _schema_title = "OW5000.AnalysisLogUse"
    _schema_id = "#/definitions/OW5000_AnalysisLogUse"
    _sql_table_name = "OW5000_AnalysisLogUse"

    # Model fields
    log_trace_anal_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    log_curve_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
