"""
Product Category Schemas
"""

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ProductCategoryCreate(BaseModel):
    url: str = Field(..., max_length=255)
    category_name: str = Field(..., max_length=255)
    category_icon: bytes | None = None
    category_color_class: str | None = Field(default=None, max_length=255)
    h1_title: str = Field(..., max_length=255)
    description: str
    parent_product_category_id: int = 0
    product_category_type_id: int = 0
    meta_title: str = Field(..., max_length=255)
    meta_description: str | None = None
    meta_keywords: str = Field(..., max_length=255)
    sale_type: int = 1
    is_active: bool = True
    trending: bool = False
    featured: bool = False
    show_on_home: bool = False
    plain: bool = False
    organic: bool = False
    reusable: bool = False

    

class ProductCategoryResponse(BaseModel):
    product_category_id: int
    url: str
    category_name: str
    category_icon: bytes | None
    category_color_class: str | None
    h1_title: str
    description: str
    parent_product_category_id: int
    product_category_type_id: int
    meta_title: str
    meta_description: str | None
    meta_keywords: str
    sale_type: int
    is_active: bool
    trending: bool
    featured: bool
    show_on_home: bool
    plain: bool
    organic: bool
    reusable: bool
    created_by: int
    created_date: datetime
    updated_by: int | None
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)

class ProductCategoryUpdate(BaseModel):
    url: str | None = Field(default=None, max_length=255)
    category_name: str | None = Field(default=None, max_length=255)
    category_icon: bytes | None = None
    category_color_class: str | None = Field(default=None, max_length=255)
    h1_title: str | None = Field(default=None, max_length=255)
    description: str | None = None
    parent_product_category_id: int | None = None
    product_category_type_id: int | None = None
    meta_title: str | None = Field(default=None, max_length=255)
    meta_description: str | None = None
    meta_keywords: str | None = Field(default=None, max_length=255)
    sale_type: int | None = None
    is_active: bool | None = None
    trending: bool | None = None
    featured: bool | None = None
    show_on_home: bool | None = None
    plain: bool | None = None
    organic: bool | None = None
    reusable: bool | None = None
    
    
