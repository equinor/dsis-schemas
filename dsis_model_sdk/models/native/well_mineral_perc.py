"""
WellMineralPerc Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.WellMineralPerc
Generated on: 2025-10-09T21:15:05.019319
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class WellMineralPerc(BaseModel):
    """
    OW5000.WellMineralPerc model.

    Represents data from the OW5000.WellMineralPerc schema.
    """

    # Schema metadata
    _schema_title = "OW5000.WellMineralPerc"
    _schema_id = "#/definitions/OW5000_WellMineralPerc"
    _sql_table_name = "OW5000_WellMineralPerc"

    # Model fields
    wellid: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=31)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    sample_alys_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    mineral: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    mineral_perc: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    mineral_perc_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2000)
    row_lock_ind: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
