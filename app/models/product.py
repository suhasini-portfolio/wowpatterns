"""
Product model.
"""

from datetime import datetime
from decimal import Decimal

from sqlalchemy import Integer, String, Text, DateTime, Boolean, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base


class Product(Base):
    __tablename__ = "products"

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    product_category_id: Mapped[int] = mapped_column(
        "ProductCategoryID",
        Integer,
        nullable=False,
        default=0
    )

    product_sku: Mapped[str] = mapped_column(
        "ProductSKU",
        String(255),
        nullable=False
    )

    product_slug: Mapped[str] = mapped_column(
        "ProductSlug",
        String(255),
        nullable=False
    )

    product_title: Mapped[str] = mapped_column(
        "ProductTitle",
        String(255),
        nullable=False
    )

    product_description: Mapped[str | None] = mapped_column(
        "ProductDescription",
        Text,
        nullable=True
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

    stock: Mapped[bool] = mapped_column(
        "Stock",
        Boolean,
        nullable=False,
        default=True
    )

    price: Mapped[Decimal] = mapped_column(
        "Price",
        Numeric(8, 2),
        nullable=False
    )

    print_price: Mapped[Decimal] = mapped_column(
        "PrintPrice",
        Numeric(8, 2),
        nullable=False,
        default=Decimal("0.00")
    )

    premium_print_price: Mapped[Decimal | None] = mapped_column(
        "PremiumPrintPrice",
        Numeric(8, 2),
        nullable=True
    )

    measuring_unit_code: Mapped[str | None] = mapped_column(
        "MeasuringUnitCode",
        String(5),
        nullable=True
    )

    custom_text: Mapped[str | None] = mapped_column(
        "CustomText",
        String(255),
        nullable=True
    )

    sale_type: Mapped[int] = mapped_column(
        "SaleType",
        Integer,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        nullable=False,
        default=True
    )

    is_published: Mapped[bool] = mapped_column(
        "IsPublished",
        Boolean,
        nullable=False,
        default=False
    )

    trending: Mapped[bool] = mapped_column(
        "IsTrending",
        Boolean,
        nullable=False,
        default=False
    )

    width: Mapped[int] = mapped_column(
        "Width",
        Integer,
        nullable=False
    )

    weight: Mapped[int] = mapped_column(
        "Weight",
        Integer,
        nullable=False
    )

    composition: Mapped[str | None] = mapped_column(
        "Composition",
        String(100),
        nullable=True
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