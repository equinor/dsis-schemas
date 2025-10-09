"""
MistieFunctionMember Model

Auto-generated from OpenWorks Common Model JSON Schema.
Schema: OpenWorksCommonModel.MistieFunctionMember
Generated on: 2025-10-09T21:14:54.936140
"""

from typing import Optional, Dict, Any
from datetime import datetime, date
from decimal import Decimal
from pydantic import Field
from .base import BaseModel

class MistieFunctionMember(BaseModel):
    """
    OpenWorksCommonModel.MistieFunctionMember model.

    Represents data from the OpenWorksCommonModel.MistieFunctionMember schema.
    """

    # Schema metadata
    _schema_title = "OpenWorksCommonModel.MistieFunctionMember"
    _schema_id = "#/definitions/OpenWorksCommonModel_MistieFunctionMember"
    _sql_table_name = "OpenWorksCommonModel_MistieFunctionMember"

    # Model fields
    native_uid: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=4000)
    mistie_function_hdr_id: int = Field(description="SQL Type: DBAPITYPEOBJECT('BOOLEAN', 'BIGINT', 'BIT', 'INTEGER', 'SMALLINT', 'TINYINT')")
    seis_geom_set_id: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=10)
    shift_hdr_name: str = Field(description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=40)
    trace_number: float = Field(description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    shift_domain: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=12)
    mistie_value: Optional[float] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('FLOAT', 'REAL', 'DOUBLE')", multiple_of=0.001)
    mistie_value_unit: Optional[str] = Field(default=None, description="SQL Type: DBAPITYPEOBJECT('CHAR', 'NCHAR', 'NVARCHAR', 'VARCHAR', 'OTHER')", max_length=64)
