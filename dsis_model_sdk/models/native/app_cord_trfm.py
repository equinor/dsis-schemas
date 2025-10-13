"""
AppCordTrfm Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.AppCordTrfm
Generated on: 2025-10-09T21:15:04.594570
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class AppCordTrfm(BaseModel):
    """
    OW5000.AppCordTrfm model.

    Represents data from the OW5000.AppCordTrfm schema.
    """

    # Schema metadata
    _schema_title = "OW5000.AppCordTrfm"
    _schema_id = "#/definitions/OW5000_AppCordTrfm"
    _sql_table_name = "OW5000_AppCordTrfm"

    # Model fields
    app_cord_trfm_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    coordinate_trfm_nm: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    r_geod_source_nm: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    source_cord_sys: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    target_cord_sys: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    ref_value_status: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
