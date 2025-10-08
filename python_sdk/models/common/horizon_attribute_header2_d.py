"""
HorizonAttributeHeader2D Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.HorizonAttributeHeader2D
Generated on: 2025-10-08T21:03:38.755701
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class HorizonAttributeHeader2D(BaseModel):
    """
    OpenWorksCommonModel.HorizonAttributeHeader2D model.
    
    Represents data from the OpenWorksCommonModel.HorizonAttributeHeader2D schema.
    """
    
    # Schema metadata
    _schema_title = "OpenWorksCommonModel.HorizonAttributeHeader2D"
    _schema_id = "#/definitions/OpenWorksCommonModel_HorizonAttributeHeader2D"
    _sql_table_name = "OpenWorksCommonModel_HorizonAttributeHeader2D"
    
    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    horizon_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=60)
    data_source: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    horizon_attribute_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    interpretation_version_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    seismic_survey_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    name_state: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=10)
