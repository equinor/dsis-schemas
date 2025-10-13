"""
DstRftFluid Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OW5000.DstRftFluid
Generated on: 2025-10-09T21:15:04.634427
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class DstRftFluid(BaseModel):
    """
    OW5000.DstRftFluid model.

    Represents data from the OW5000.DstRftFluid schema.
    """

    # Schema metadata
    _schema_title = "OW5000.DstRftFluid"
    _schema_id = "#/definitions/OW5000_DstRftFluid"
    _sql_table_name = "OW5000_DstRftFluid"

    # Model fields
    wellid: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=31)
    dst_rft_test_no: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    fluid_type: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=20)
    fluid_amt: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    fluid_unit_meas: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    perc_oil: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    perc_oil_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    perc_other: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    perc_other_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    perc_wtr: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    perc_wtr_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    wtr_salinity: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    wtr_salinity_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    specific_gravity: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    api_temp: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.0001)
    api_temp_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    resistivity: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    resistivity_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    resistivity_temp: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.0001)
    resistivity_temp_dsdsunit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
    remark: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=2000)
    create_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    create_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    update_date: Optional[datetime] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('TIMESTAMP')")
    update_user_id: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=32)
    row_lock_ind: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=1)
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
