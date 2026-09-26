from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ProductImage(Base):
    __tablename__ = "product_images"

    product_image_id: Mapped[int] = mapped_column(
        "ProductImageID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    file_name: Mapped[str] = mapped_column(
        "FileName",
        String(255),
        nullable=False,
    )

    alt_text: Mapped[str] = mapped_column(
        "AltText",
        String(255),
        nullable=False,
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False,
        default=0,
    )

    is_default: Mapped[bool] = mapped_column(
        "IsDefault",
        Boolean,
        nullable=False,
        default=False,
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        nullable=False,
        default=True,
    )

    created_by: Mapped[int] = mapped_column(
        "CreatedBy",
        Integer,
        nullable=False,
        default=0,
    )

    created_date: Mapped[datetime] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=False,
    )

    updated_by: Mapped[int] = mapped_column(
        "UpdatedBy",
        Integer,
        nullable=False,
        default=0,
    )

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate",
        DateTime,
        nullable=True,
    )