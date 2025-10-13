"""
PgAttrdef Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_attrdef
Generated on: 2025-10-09T21:15:05.103208
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgAttrdef(BaseModel):
    """
    pg_catalog.pg_attrdef model.

    Represents data from the pg_catalog.pg_attrdef schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_attrdef"
    _schema_id = "#/definitions/pg_catalog_pg_attrdef"
    _sql_table_name = "pg_catalog_pg_attrdef"

    # Model fields
    adrelid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    adnum: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    adbin: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    adsrc: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
