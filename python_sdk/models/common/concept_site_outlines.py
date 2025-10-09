"""
ConceptSiteOutlines Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.ConceptSiteOutlines
Generated on: 2025-10-09T21:14:54.894408
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class ConceptSiteOutlines(BaseModel):
    """
    OpenWorksCommonModel.ConceptSiteOutlines model.

    Represents data from the OpenWorksCommonModel.ConceptSiteOutlines schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.ConceptSiteOutlines"
    _schema_id = "#/definitions/OpenWorksCommonModel_ConceptSiteOutlines"
    _sql_table_name = "OpenWorksCommonModel_ConceptSiteOutlines"

    # Model fields
    site_outline_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    concept_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    site_outline_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
    project_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1024)
