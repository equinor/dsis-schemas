"""
GeographyColumns Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.GEOGRAPHY_COLUMNS
Generated on: 2025-10-08T21:10:50.525125
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class GeographyColumns(BaseModel):
    """
    SYS.GEOGRAPHY_COLUMNS model.
    
    Represents data from the SYS.GEOGRAPHY_COLUMNS schema.
    """
    
    # Schema metadata
    _schema_title = "SYS.GEOGRAPHY_COLUMNS"
    _schema_id = "#/definitions/SYS_GEOGRAPHY_COLUMNS"
    _sql_table_name = "SYS_GEOGRAPHY_COLUMNS"
    
    # Model fields
    F_TABLE_CATALOG: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_TABLE_SCHEMA: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_TABLE_NAME: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_GEOMETRY_COLUMN: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    COORD_DIMENSION: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    SRID: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    TYPE: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=30)
