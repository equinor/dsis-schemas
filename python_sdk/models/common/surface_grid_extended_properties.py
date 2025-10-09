"""
SurfaceGridExtendedProperties Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.SurfaceGridExtendedProperties
Generated on: 2025-10-09T21:14:54.962819
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class SurfaceGridExtendedProperties(BaseModel):
    """
    OpenWorksCommonModel.SurfaceGridExtendedProperties model.

    Represents data from the OpenWorksCommonModel.SurfaceGridExtendedProperties schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.SurfaceGridExtendedProperties"
    _schema_id = "#/definitions/OpenWorksCommonModel_SurfaceGridExtendedProperties"
    _sql_table_name = "OpenWorksCommonModel_SurfaceGridExtendedProperties"

    # Model fields
    grid_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    extended_properties: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
