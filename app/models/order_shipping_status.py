from datetime import datetime

from sqlalchemy import DateTime, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class OrderShippingStatus(Base):
    __tablename__ = "ordershippingstatuses"

    order_shipping_status_id: Mapped[int] = mapped_column(
        "OrderShippingStatusID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    order_id: Mapped[int] = mapped_column(
        "OrderID",
        Integer,
        nullable=False,
        default=0,
    )

    order_item_id: Mapped[int] = mapped_column(
        "OrderItemID",
        Integer,
        nullable=False,
        default=0,
    )

    shipping_status_id: Mapped[int] = mapped_column(
        "ShippingStatusID",
        Integer,
        nullable=False,
        default=1,
    )

    messages: Mapped[str | None] = mapped_column(
        "Messages",
        Text,
        nullable=True,
    )

    updated_by: Mapped[int] = mapped_column(
        "UpdatedBy",
        Integer,
        nullable=False,
        default=0,
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

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate",
        DateTime,
        nullable=True,
    )