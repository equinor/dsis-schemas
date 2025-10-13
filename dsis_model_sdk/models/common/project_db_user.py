"""
ProjectDBUser Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.ProjectDBUser
Generated on: 2025-10-09T21:14:54.943110
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class ProjectDBUser(BaseModel):
    """
    OpenWorksCommonModel.ProjectDBUser model.

    Represents data from the OpenWorksCommonModel.ProjectDBUser schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.ProjectDBUser"
    _schema_id = "#/definitions/OpenWorksCommonModel_ProjectDBUser"
    _sql_table_name = "OpenWorksCommonModel_ProjectDBUser"

    # Model fields
    user_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=33)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=33)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
