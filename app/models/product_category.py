from datetime import datetime

from sqlalchemy import Integer, String, Text, LargeBinary, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    product_category_id: Mapped[int] = mapped_column(
            "ProductCategoryID",
            Integer,
            primary_key=True,
            autoincrement=True
        )
    
    url: Mapped[str] = mapped_column(
            "Url",
            String(255),
            nullable=False
    )
    
    category_name: Mapped[str] = mapped_column(
            "CategoryName",
            String(255),
            nullable=False
    )
    
    category_icon: Mapped[bytes | None] = mapped_column(
            "CategoryIcon",
            LargeBinary,
            nullable=True
    )
    
    category_color_class: Mapped[str | None] = mapped_column(
            "CategoryColorClass",
            String(255),
            nullable=True
    )
    
    h1_title: Mapped[str] = mapped_column(
            "H1Title",
            String(255),
            nullable=False
    )
    
    description: Mapped[str] = mapped_column(
            "Description",
            Text,
            nullable=False
    )
    
    parent_product_category_id: Mapped[int] = mapped_column(
            "ParentProductCategoryID",
            Integer,
            nullable=False,
            default=0
    )
    
    product_category_type_id: Mapped[int] = mapped_column(
            "ProductCategoryTypeID",
            Integer,
            nullable=False,
            default=0
    )
    
    meta_title: Mapped[str] = mapped_column(
            "MetaTitle",
            String(255),
            nullable=False
    )
    
    meta_description: Mapped[str | None] = mapped_column(
            "MetaDescription",
            Text,
            nullable=True
    )
    
    meta_keywords: Mapped[str] = mapped_column(
            "MetaKeywords",
            String(255),
            nullable=False
    )
    
    trending: Mapped[bool] = mapped_column(
            "IsTrending",
            Boolean,
            nullable=False,
            default=False
    )
    
    featured: Mapped[bool] = mapped_column(
            "IsFeatured",
            Boolean,
            nullable=False,
            default=False
    )
    
    show_on_home: Mapped[bool] = mapped_column(
            "ShowOnHome",
            Boolean,
            nullable=False,
            default=False
    )
    
    plain: Mapped[bool] = mapped_column(
           "IsPlain",
            Boolean,
            nullable=False,
            default=False
    )
    
    organic: Mapped[bool] = mapped_column(
            "IsOrganic",
            Boolean,
            nullable=False,
            default=False
    )
    
    reusable: Mapped[bool] = mapped_column(
            "IsReusable",
            Boolean,
            nullable=False,
            default=False
    )
    
    sale_type: Mapped[int] = mapped_column(
            "SaleType",
            Integer,
            nullable=False,
            default=1
    )
    
    is_active: Mapped[bool] = mapped_column(
            "IsActive",
            Boolean,
            nullable=False,
            default=True
    )
    
    created_by: Mapped[int] = mapped_column(
            "CreatedBy",
            Integer,
            nullable=False
    )
    
    created_date: Mapped[datetime] = mapped_column(
            "CreatedDate",
            DateTime,
            nullable=False
    )
    
    updated_by: Mapped[int | None] = mapped_column(
            "UpdatedBy",
            Integer,
            nullable=True
    )
    
    updated_date: Mapped[datetime | None] = mapped_column(
            "UpdatedDate",
            DateTime,
            nullable=True
    )
    
        