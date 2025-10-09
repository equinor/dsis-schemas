"""
CurveMnemonicGroupMember Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.CurveMnemonicGroupMember
Generated on: 2025-10-09T21:15:04.622438
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class CurveMnemonicGroupMember(BaseModel):
    """
    OW5000.CurveMnemonicGroupMember model.

    Represents data from the OW5000.CurveMnemonicGroupMember schema.
    """

    # Schema metadata
    _schema_title = "OW5000.CurveMnemonicGroupMember"
    _schema_id = "#/definitions/OW5000_CurveMnemonicGroupMember"
    _sql_table_name = "OW5000_CurveMnemonicGroupMember"

    # Model fields
    crv_group_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    priority_seq: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    member_crv_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=25)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
