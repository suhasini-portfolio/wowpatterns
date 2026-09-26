"""
Product Schemas
"""

from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    product_category_id: int

    product_sku: str = Field(..., max_length=255)
    product_slug: str = Field(..., max_length=255)
    product_title: str = Field(..., max_length=255)

    product_description: str | None = None

    meta_title: str = Field(..., max_length=255)
    meta_description: str | None = None
    meta_keywords: str = Field(..., max_length=255)

    stock: bool = True

    price: Decimal
    print_price: Decimal
    premium_print_price: Decimal | None = None

    measuring_unit_code: str | None = Field(
        default=None,
        max_length=5
    )

    custom_text: str | None = Field(
        default=None,
        max_length=255
    )

    sale_type: int = 1

    is_active: bool = True
    is_published: bool = False
    trending: bool = False

    width: int = 0
    weight: int = 0

    composition: str | None = Field(
        default=None,
        max_length=100
    )

class ProductResponse(BaseModel):
    product_id: int
    product_category_id:int
    product_sku: str
    product_slug: str
    product_title: str
    product_description: str | None
    meta_title: str
    meta_description: str | None
    meta_keywords: str
    stock: bool
    price: Decimal
    print_price: Decimal
    premium_print_price: Decimal | None
    measuring_unit_code: str | None
    custom_text: str | None
    sale_type: int
    is_active:bool
    is_published:bool
    trending:bool
    width:int
    weight:int
    composition:str | None
    created_by:int
    created_date: datetime
    updated_by: int | None
    updated_date: datetime | None

    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    product_category_id: int | None = None
    
    product_sku: str | None = Field(default=None, max_length=255)
    product_slug: str | None = Field(default=None, max_length=255)
    product_title: str | None = Field(default=None, max_length=255)
        
    product_description: str | None = None
        
    meta_title: str | None = Field(default=None, max_length=255)
    meta_description: str | None = None
    meta_keywords: str | None = Field(default=None, max_length=255)
        
    stock: bool | None = None
        
    price: Decimal | None = None
    print_price: Decimal | None = None
    premium_print_price: Decimal | None = None
        
    measuring_unit_code: str | None = Field(
        default=None,
        max_length=5
    )
        
    custom_text: str | None = Field(
        default=None,
        max_length=255
    )
        
    sale_type: int | None = None
        
    is_active: bool | None = None
    is_published: bool | None = None
    trending: bool | None = None
        
    width: int | None = None
    weight: int | None = None
        
    composition: str | None = Field(
        default=None,
        max_length=100
    )
