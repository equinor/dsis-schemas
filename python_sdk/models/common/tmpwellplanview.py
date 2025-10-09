"""
Tmpwellplanview Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.tmpwellplanview
Generated on: 2025-10-09T21:14:54.993057
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Tmpwellplanview(BaseModel):
    """
    OpenWorksCommonModel.tmpwellplanview model.

    Represents data from the OpenWorksCommonModel.tmpwellplanview schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.tmpwellplanview"
    _schema_id = "#/definitions/OpenWorksCommonModel_tmpwellplanview"
    _sql_table_name = "OpenWorksCommonModel_tmpwellplanview"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    wellbore_native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    location_type: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    parent_location_type: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    platform_native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
