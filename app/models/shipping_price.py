from datetime import datetime
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ShippingPrice(Base):
    __tablename__ = "shipping_prices"

    shipping_price_id: Mapped[int] = mapped_column(
        "ShippingPriceID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    shipping_type: Mapped[str | None] = mapped_column(
        "ShippingType",
        String(20),
        nullable=True,
    )

    country_id: Mapped[int] = mapped_column(
        "CountryID",
        Integer,
        nullable=False,
        default=0,
    )

    shipping_amount: Mapped[Decimal] = mapped_column(
        "ShippingAmount",
        Numeric(10, 2),
        nullable=False,
        default=Decimal("0.00"),
    )

    shipping_price: Mapped[Decimal | None] = mapped_column(
        "ShippingPrice",
        Numeric(10, 2),
        nullable=True,
        default=Decimal("0.00"),
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        nullable=True,
        default=True,
    )

    delivery_period: Mapped[str | None] = mapped_column(
        "DeliveryPeriod",
        String(255),
        nullable=True,
        default="",
    )

    extra_item_price: Mapped[Decimal | None] = mapped_column(
        "ExtraItemPrice",
        Numeric(10, 2),
        nullable=True,
        default=Decimal("0.00"),
    )

    created_by: Mapped[int] = mapped_column(
        "CreatedBy",
        Integer,
        nullable=False,
        default=0,
    )

    created_date: Mapped[datetime | None] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=True,
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