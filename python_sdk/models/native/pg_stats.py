"""
PgStats Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_stats
Generated on: 2025-10-09T21:15:05.115070
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgStats(BaseModel):
    """
    pg_catalog.pg_stats model.

    Represents data from the pg_catalog.pg_stats schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_stats"
    _schema_id = "#/definitions/pg_catalog_pg_stats"
    _sql_table_name = "pg_catalog_pg_stats"

    # Model fields
    schemaname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    tablename: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    attname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
