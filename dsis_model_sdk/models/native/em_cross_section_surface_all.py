"""
EmCrossSectionSurfaceAll Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.EmCrossSectionSurfaceAll
Generated on: 2025-10-09T21:15:04.647637
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class EmCrossSectionSurfaceAll(BaseModel):
    """
    OW5000.EmCrossSectionSurfaceAll model.

    Represents data from the OW5000.EmCrossSectionSurfaceAll schema.
    """

    # Schema metadata
    _schema_title = "OW5000.EmCrossSectionSurfaceAll"
    _schema_id = "#/definitions/OW5000_EmCrossSectionSurfaceAll"
    _sql_table_name = "OW5000_EmCrossSectionSurfaceAll"

    # Model fields
    cross_section_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    surface_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    surface_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=30)
    structural_model_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2000)
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
