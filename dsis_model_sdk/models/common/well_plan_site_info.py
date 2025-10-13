"""
WellPlanSiteInfo Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.WellPlanSiteInfo
Generated on: 2025-10-09T21:14:54.983294
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class WellPlanSiteInfo(BaseModel):
    """
    OpenWorksCommonModel.WellPlanSiteInfo model.

    Represents data from the OpenWorksCommonModel.WellPlanSiteInfo schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.WellPlanSiteInfo"
    _schema_id = "#/definitions/OpenWorksCommonModel_WellPlanSiteInfo"
    _sql_table_name = "OpenWorksCommonModel_WellPlanSiteInfo"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    wellplan_project_native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    cost: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.0001)
    day_rate: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.0001)
    override_cost: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=6)
    override_day_rate: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=6)
    override_slots: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=6)
    slots: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.0001)
    type_field: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=50, alias="type")
    water_depth: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
