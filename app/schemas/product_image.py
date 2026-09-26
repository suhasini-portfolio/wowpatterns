from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ProductImageCreate(BaseModel):
    file_name: str = Field(..., max_length=255)
    alt_text: str = Field(..., max_length=255)
    product_id: int
    is_default: bool = False
    is_active: bool = True


class ProductImageUpdate(BaseModel):
    file_name: str | None = Field(default=None, max_length=255)
    alt_text: str | None = Field(default=None, max_length=255)
    product_id: int | None = None
    is_default: bool | None = None
    is_active: bool | None = None


class ProductImageResponse(BaseModel):
    product_image_id: int
    file_name: str
    alt_text: str
    product_id: int
    is_default: bool
    is_active: bool
    created_by: int
    created_date: datetime
    updated_by: int
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)