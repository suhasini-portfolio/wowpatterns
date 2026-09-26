from datetime import datetime
from sqlalchemy import DateTime, Integer, Float, String, Numeric, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class OrderItem(Base):
    __tablename__ = "orderitems"

    order_item_id: Mapped[int] = mapped_column(
        "OrderItemID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    order_id: Mapped[int] = mapped_column(
        "OrderID",
        Integer,
        nullable=False
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False
    )

    product_type: Mapped[str] = mapped_column(
        "ProductType",
        String(5),
        nullable=False
    )

    fabric_product_id: Mapped[int | None] = mapped_column(
        "FabricProductID",
        Integer,
        nullable=True,
        default=0
    )

    quantity: Mapped[int] = mapped_column(
        "Quantity",
        Integer,
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        "Price",
        Float,
        nullable=False
    )

    print_quality: Mapped[str | None] = mapped_column(
        "PrintQuality",
        String(5),
        nullable=True
    )

    artist_commission_percentage: Mapped[int | None] = mapped_column(
        "ArtistCommissionPercentage",
        Numeric(8, 0),
        nullable=True,
        default=0
    )

    artist_commission: Mapped[int | None] = mapped_column(
        "ArtistCommission",
        Numeric(8, 0),
        nullable=True,
        default=0
    )

    shipping_status_id: Mapped[int] = mapped_column(
        "ShippingStatusID",
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

    created_date: Mapped[datetime] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=False
    )

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate",
        DateTime,
        nullable=True
    )