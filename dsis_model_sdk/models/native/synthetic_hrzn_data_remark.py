"""
SyntheticHrznDataRemark Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.SyntheticHrznDataRemark
Generated on: 2025-10-09T21:15:04.975651
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SyntheticHrznDataRemark(BaseModel):
    """
    OW5000.SyntheticHrznDataRemark model.

    Represents data from the OW5000.SyntheticHrznDataRemark schema.
    """

    # Schema metadata
    _schema_title = "OW5000.SyntheticHrznDataRemark"
    _schema_id = "#/definitions/OW5000_SyntheticHrznDataRemark"
    _sql_table_name = "OW5000_SyntheticHrznDataRemark"

    # Model fields
    syn_hrzn_data_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    syn_hrzn_data_rmk_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    long_remark_nchar: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    long_remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CLOB', 'LONGVARCHAR', 'LONGNVARCHAR', 'NCLOB', 'SQLXML')", max_length=8)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
