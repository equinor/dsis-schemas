"""
PgPreparedXacts Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_prepared_xacts
Generated on: 2025-10-09T21:15:05.111291
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgPreparedXacts(BaseModel):
    """
    pg_catalog.pg_prepared_xacts model.

    Represents data from the pg_catalog.pg_prepared_xacts schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_prepared_xacts"
    _schema_id = "#/definitions/pg_catalog_pg_prepared_xacts"
    _sql_table_name = "pg_catalog_pg_prepared_xacts"

    # Model fields
    transaction: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    gid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    owner: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    database: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
