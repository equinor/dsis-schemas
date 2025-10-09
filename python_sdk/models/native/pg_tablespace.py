"""
PgTablespace Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_tablespace
Generated on: 2025-10-09T21:15:05.115963
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgTablespace(BaseModel):
    """
    pg_catalog.pg_tablespace model.

    Represents data from the pg_catalog.pg_tablespace schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_tablespace"
    _schema_id = "#/definitions/pg_catalog_pg_tablespace"
    _sql_table_name = "pg_catalog_pg_tablespace"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    spcname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    spcowner: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    spcacl: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    spcoptions: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
