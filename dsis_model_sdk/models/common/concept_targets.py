"""
ConceptTargets Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.ConceptTargets
Generated on: 2025-10-09T21:14:54.895375
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class ConceptTargets(BaseModel):
    """
    OpenWorksCommonModel.ConceptTargets model.

    Represents data from the OpenWorksCommonModel.ConceptTargets schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.ConceptTargets"
    _schema_id = "#/definitions/OpenWorksCommonModel_ConceptTargets"
    _sql_table_name = "OpenWorksCommonModel_ConceptTargets"

    # Model fields
    target_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    target_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    project_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
