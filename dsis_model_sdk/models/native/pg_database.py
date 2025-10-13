"""
PgDatabase Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_database
Generated on: 2025-10-09T21:15:05.104741
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgDatabase(BaseModel):
    """
    pg_catalog.pg_database model.

    Represents data from the pg_catalog.pg_database schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_database"
    _schema_id = "#/definitions/pg_catalog_pg_database"
    _sql_table_name = "pg_catalog_pg_database"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    datname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    encoding: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    datlastsysoid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    datallowconn: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    datconfig: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    datacl: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    datdba: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    dattablespace: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
