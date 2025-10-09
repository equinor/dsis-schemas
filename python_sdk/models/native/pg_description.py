"""
PgDescription Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_description
Generated on: 2025-10-09T21:15:05.105369
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgDescription(BaseModel):
    """
    pg_catalog.pg_description model.

    Represents data from the pg_catalog.pg_description schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_description"
    _schema_id = "#/definitions/pg_catalog_pg_description"
    _sql_table_name = "pg_catalog_pg_description"

    # Model fields
    objoid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    classoid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    objsubid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    description: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
