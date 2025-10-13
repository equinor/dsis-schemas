"""
UniqueSeisDataSetName Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.UniqueSeisDataSetName
Generated on: 2025-10-09T21:15:04.986177
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class UniqueSeisDataSetName(BaseModel):
    """
    OW5000.UniqueSeisDataSetName model.

    Represents data from the OW5000.UniqueSeisDataSetName schema.
    """

    # Schema metadata
    _schema_title = "OW5000.UniqueSeisDataSetName"
    _schema_id = "#/definitions/OW5000_UniqueSeisDataSetName"
    _sql_table_name = "OW5000_UniqueSeisDataSetName"

    # Model fields
    seis_data_set_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    seismic_version_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
