from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ShoppingBagCreate(BaseModel):
    product_id: int
    product_type: str = Field(default="O", max_length=50)
    fabric_product_id: int | None = 0
    quantity: int = Field(..., gt=0)
    print_quality: str | None = Field(default="N", max_length=5)
    user_browser: str | None = Field(default=None, max_length=40)


class ShoppingBagUpdate(BaseModel):
    quantity: int | None = Field(default=None, gt=0)
    print_quality: str | None = Field(default=None, max_length=5)
    user_browser: str | None = Field(default=None, max_length=40)


class ShoppingBagResponse(BaseModel):
    shopping_bag_id: int
    product_id: int
    product_type: str
    fabric_product_id: int | None
    quantity: int
    print_quality: str | None
    user_id: int | None
    user_browser: str | None
    created_date: datetime
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)