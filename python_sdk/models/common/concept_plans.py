"""
ConceptPlans Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.ConceptPlans
Generated on: 2025-10-09T21:14:54.894016
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class ConceptPlans(BaseModel):
    """
    OpenWorksCommonModel.ConceptPlans model.

    Represents data from the OpenWorksCommonModel.ConceptPlans schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.ConceptPlans"
    _schema_id = "#/definitions/OpenWorksCommonModel_ConceptPlans"
    _sql_table_name = "OpenWorksCommonModel_ConceptPlans"

    # Model fields
    plan_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    plan_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    project_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
