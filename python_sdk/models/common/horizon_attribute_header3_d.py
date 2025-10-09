"""
HorizonAttributeHeader3D Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.HorizonAttributeHeader3D
Generated on: 2025-10-09T21:14:54.921634
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class HorizonAttributeHeader3D(BaseModel):
    """
    OpenWorksCommonModel.HorizonAttributeHeader3D model.

    Represents data from the OpenWorksCommonModel.HorizonAttributeHeader3D schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.HorizonAttributeHeader3D"
    _schema_id = "#/definitions/OpenWorksCommonModel_HorizonAttributeHeader3D"
    _sql_table_name = "OpenWorksCommonModel_HorizonAttributeHeader3D"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    horizon_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    data_source: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    horizon_attribute_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    interpretation_version_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    seismic_survey_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    name_state: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=10)
