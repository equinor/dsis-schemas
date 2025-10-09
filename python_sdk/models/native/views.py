"""
Views Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: pg_catalog.information_schema.views
Generated on: 2025-10-09T21:15:05.081307
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class Views(BaseModel):
    """
    pg_catalog.information_schema.views model.

    Represents data from the pg_catalog.information_schema.views schema.
    """

    # Schema metadata
    _schema_title = "pg_catalog.information_schema.views"
    _schema_id = "#/definitions/pg_catalog_information_schema.views"
    _sql_table_name = "pg_catalog_information_schema_views"

    # Model fields
    table_catalog: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    table_schema: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    table_name: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    check_option: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    is_updatable: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
