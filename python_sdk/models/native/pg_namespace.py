"""
PgNamespace Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_namespace
Generated on: 2025-10-09T21:15:05.110879
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgNamespace(BaseModel):
    """
    pg_catalog.pg_namespace model.

    Represents data from the pg_catalog.pg_namespace schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_namespace"
    _schema_id = "#/definitions/pg_catalog_pg_namespace"
    _sql_table_name = "pg_catalog_pg_namespace"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    nspname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    nspowner: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
