from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductSpecificationCreate(BaseModel):
    product_id: int
    specification_name: str = Field(..., max_length=255)
    specification_value: str = Field(..., max_length=255)


class ProductSpecificationResponse(BaseModel):
    specification_id: int
    product_id: int
    specification_name: str
    specification_value: str
    created_by: int
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)