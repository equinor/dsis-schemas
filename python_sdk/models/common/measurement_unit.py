"""
MeasurementUnit Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.MeasurementUnit
Generated on: 2025-10-09T21:14:54.933729
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class MeasurementUnit(BaseModel):
    """
    OpenWorksCommonModel.MeasurementUnit model.

    Represents data from the OpenWorksCommonModel.MeasurementUnit schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.MeasurementUnit"
    _schema_id = "#/definitions/OpenWorksCommonModel_MeasurementUnit"
    _sql_table_name = "OpenWorksCommonModel_MeasurementUnit"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    unit_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    unit_type_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=30)
    unit_abbreviation: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    data_source: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=5)
    epsg_code: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2000)
