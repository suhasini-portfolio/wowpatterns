from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductDesignSpecificationCreate(BaseModel):
    product_id: int
    artist_id: int
    design_id: int
    is_individual_design_price: bool = True
    design_price: Decimal = Field(..., max_digits=8, decimal_places=2)
    is_repeatable: bool = False
    design_file_type_id: int = 0
    file_name: str = Field(..., max_length=255)
    is_active: bool = True
    created_by: int = 0


class ProductDesignSpecificationUpdate(BaseModel):
    product_id: int | None = None
    artist_id: int | None = None
    design_id: int | None = None
    is_individual_design_price: bool | None = None
    design_price: Decimal | None = Field(
        default=None,
        max_digits=8,
        decimal_places=2,
    )
    is_repeatable: bool | None = None
    design_file_type_id: int | None = None
    file_name: str | None = Field(
        default=None,
        max_length=255,
    )
    is_active: bool | None = None
    updated_by: int | None = None


class ProductDesignSpecificationResponse(BaseModel):
    design_specification_id: int
    product_id: int
    artist_id: int
    design_id: int
    is_individual_design_price: bool
    design_price: Decimal
    is_repeatable: bool
    design_file_type_id: int
    file_name: str
    is_active: bool
    created_by: int
    created_date: datetime
    updated_by: int | None
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)