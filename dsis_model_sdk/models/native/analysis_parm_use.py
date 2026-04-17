"""
AnalysisParmUse Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.AnalysisParmUse
Generated on: 2026-04-17T09:03:28.411292
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class AnalysisParmUse(BaseModel):
    """
    OW5000.AnalysisParmUse model.

    Represents data from the OW5000.AnalysisParmUse schema.
    """

    # Schema metadata
    _schema_title = "OW5000.AnalysisParmUse"
    _schema_id = "#/definitions/OW5000_AnalysisParmUse"
    _sql_table_name = "OW5000_AnalysisParmUse"

    # Model fields
    log_trace_anal_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    petro_parm_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=3)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
