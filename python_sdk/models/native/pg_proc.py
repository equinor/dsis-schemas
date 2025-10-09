"""
PgProc Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.pg_proc
Generated on: 2025-10-09T21:15:05.111654
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class PgProc(BaseModel):
    """
    pg_catalog.pg_proc model.

    Represents data from the pg_catalog.pg_proc schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.pg_proc"
    _schema_id = "#/definitions/pg_catalog_pg_proc"
    _sql_table_name = "pg_catalog_pg_proc"

    # Model fields
    oid: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    proname: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    proretset: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    prorettype: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    pronargs: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    proargtypes: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    proargnames: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    proargmodes: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    proallargtypes: Optional[str] = Field(default=None, description="SQL Type: NONE", max_length=2147483647)
    pronamespace: Optional[int] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
