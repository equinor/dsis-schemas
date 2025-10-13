"""
CorePropertyAlysDetail Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.CorePropertyAlysDetail
Generated on: 2025-10-09T21:15:04.616708
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class CorePropertyAlysDetail(BaseModel):
    """
    OW5000.CorePropertyAlysDetail model.

    Represents data from the OW5000.CorePropertyAlysDetail schema.
    """

    # Schema metadata
    _schema_title = "OW5000.CorePropertyAlysDetail"
    _schema_id = "#/definitions/OW5000_CorePropertyAlysDetail"
    _sql_table_name = "OW5000_CorePropertyAlysDetail"

    # Model fields
    wellid: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=31)
    core_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    analysis_obs_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    sample_number: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    sample_analysis_obs_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    prop_alys_obs_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    alys_detail_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    value1: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    value2: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    value3: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    value4: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    original_data_source: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    row_lock_ind: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
