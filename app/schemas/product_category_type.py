from pydantic import BaseModel, Field, ConfigDict


class ProductCategoryTypeCreate(BaseModel):
    product_category_type: str = Field(..., max_length=20)
    is_active: bool = True

class ProductCategoryTypeUpdate(BaseModel):
    product_category_type: str | None = Field(default=None, max_length=20)
    is_active: bool | None = None

class ProductCategoryTypeResponse(BaseModel):
    product_category_type_id: int
    product_category_type: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)