"""
LogSampleBlockInfo Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.LogSampleBlockInfo
Generated on: 2025-10-09T21:15:04.781377
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class LogSampleBlockInfo(BaseModel):
    """
    OW5000.LogSampleBlockInfo model.

    Represents data from the OW5000.LogSampleBlockInfo schema.
    """

    # Schema metadata
    _schema_title = "OW5000.LogSampleBlockInfo"
    _schema_id = "#/definitions/OW5000_LogSampleBlockInfo"
    _sql_table_name = "OW5000_LogSampleBlockInfo"

    # Model fields
    log_curve_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    vid: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    blk_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    first_sample_num: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    last_sample_num: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    block_size: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
