"""
PgAm Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_am
Generated on: 2025-10-09T21:15:05.102703
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgAm(BaseModel):
    """
    pg_catalog.pg_am model.

    Represents data from the pg_catalog.pg_am schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_am"
    _schema_id = "#/definitions/pg_catalog_pg_am"
    _sql_table_name = "pg_catalog_pg_am"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    amname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
