"""
SeismicChangeLog Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.SeismicChangeLog
Generated on: 2025-10-09T21:15:04.941334
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SeismicChangeLog(BaseModel):
    """
    OW5000.SeismicChangeLog model.

    Represents data from the OW5000.SeismicChangeLog schema.
    """

    # Schema metadata
    _schema_title = "OW5000.SeismicChangeLog"
    _schema_id = "#/definitions/OW5000_SeismicChangeLog"
    _sql_table_name = "OW5000_SeismicChangeLog"

    # Model fields
    seismic_change_sequence: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    seismic_data_set_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    seismic_update_user_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    seismic_update_timestamp: datetime = Field(description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
