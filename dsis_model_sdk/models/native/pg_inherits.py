"""
PgInherits Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_inherits
Generated on: 2025-10-09T21:15:05.110203
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgInherits(BaseModel):
    """
    pg_catalog.pg_inherits model.

    Represents data from the pg_catalog.pg_inherits schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_inherits"
    _schema_id = "#/definitions/pg_catalog_pg_inherits"
    _sql_table_name = "pg_catalog_pg_inherits"

    # Model fields
    inhrelid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    inhparent: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    inhseqno: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
