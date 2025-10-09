"""
PgRewrite Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_rewrite
Generated on: 2025-10-09T21:15:05.112125
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgRewrite(BaseModel):
    """
    pg_catalog.pg_rewrite model.

    Represents data from the pg_catalog.pg_rewrite schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_rewrite"
    _schema_id = "#/definitions/pg_catalog_pg_rewrite"
    _sql_table_name = "pg_catalog_pg_rewrite"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    ev_class: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    rulename: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
