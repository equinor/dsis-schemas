"""
Wellplanlocation Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.wellplanlocation
Generated on: 2026-10-04T18:51:25.788638
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Wellplanlocation(BaseModel):
    """
    OpenWorksCommonModel.wellplanlocation model.

    Represents data from the OpenWorksCommonModel.wellplanlocation schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.wellplanlocation"
    _schema_id = "#/definitions/OpenWorksCommonModel_wellplanlocation"
    _sql_table_name = "OpenWorksCommonModel_wellplanlocation"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    spatial: Optional[Dict[str, Any]] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BINARY', 'BLOB', 'LONGVARBINARY', 'VARBINARY')")
