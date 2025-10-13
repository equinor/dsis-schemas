"""
WellList Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.WellList
Generated on: 2025-10-09T21:14:54.977658
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class WellList(BaseModel):
    """
    OpenWorksCommonModel.WellList model.

    Represents data from the OpenWorksCommonModel.WellList schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.WellList"
    _schema_id = "#/definitions/OpenWorksCommonModel_WellList"
    _sql_table_name = "OpenWorksCommonModel_WellList"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=128)
    name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=80)
    type_field: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=15, alias="type")
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    original_data_source: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    alternate_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
