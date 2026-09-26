from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ProductSpecification(Base):
    __tablename__ = "product_specifications"

    specification_id: Mapped[int] = mapped_column(
        "SpecificationID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False
    )

    specification_name: Mapped[str] = mapped_column(
        "SpecificationName",
        String(255),
        nullable=False
    )

    specification_value: Mapped[str] = mapped_column(
        "SpecificationValue",
        String(255),
        nullable=False
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