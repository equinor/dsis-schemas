"""
GeometryColumns Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: SYS.GEOMETRY_COLUMNS
Generated on: 2025-10-09T21:15:05.062282
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class GeometryColumns(BaseModel):
    """
    SYS.GEOMETRY_COLUMNS model.

    Represents data from the SYS.GEOMETRY_COLUMNS schema.
    """

    # Schema metadata
    _schema_title = "SYS.GEOMETRY_COLUMNS"
    _schema_id = "#/definitions/SYS_GEOMETRY_COLUMNS"
    _sql_table_name = "SYS_GEOMETRY_COLUMNS"

    # Model fields
    F_TABLE_CATALOG: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_TABLE_SCHEMA: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_TABLE_NAME: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    F_GEOMETRY_COLUMN: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=256)
    COORD_DIMENSION: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    SRID: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    TYPE: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=30)
