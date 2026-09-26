from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ProductDesignSpecification(Base):
    __tablename__ = "product_design_specifications"

    design_specification_id: Mapped[int] = mapped_column(
        "DesignSpecificationID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False,
        default=0,
    )

    artist_id: Mapped[int] = mapped_column(
        "ArtistID",
        Integer,
        nullable=False,
        default=0,
    )

    design_id: Mapped[int] = mapped_column(
        "DesignID",
        Integer,
        nullable=False,
    )

    is_individual_design_price: Mapped[bool] = mapped_column(
        "IsIndividualDesignPrice",
        Boolean,
        nullable=False,
        default=True,
    )

    design_price: Mapped[Decimal] = mapped_column(
        "DesignPrice",
        Numeric(8, 2),
        nullable=False,
    )

    is_repeatable: Mapped[bool] = mapped_column(
        "IsRepeatable",
        Boolean,
        nullable=False,
        default=False,
    )

    design_file_type_id: Mapped[int] = mapped_column(
        "DesignFileTypeID",
        Integer,
        nullable=False,
        default=0,
    )

    file_name: Mapped[str] = mapped_column(
        "FileName",
        String(255),
        nullable=False,
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

    updated_by: Mapped[int | None] = mapped_column(
        "UpdatedBy",
        Integer,
        nullable=True,
        default=0,
    )

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate",
        DateTime,
        nullable=True,
    )