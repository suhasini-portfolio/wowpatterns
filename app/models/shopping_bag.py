from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ShoppingBag(Base):
    __tablename__ = "shoppingbag"

    shopping_bag_id: Mapped[int] = mapped_column(
        "ShoppingBagID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False,
    )

    product_type: Mapped[str] = mapped_column(
        "ProductType",
        String(50),
        nullable=False,
        default="O",
    )

    fabric_product_id: Mapped[int | None] = mapped_column(
        "FabricProductID",
        Integer,
        nullable=True,
        default=0,
    )

    quantity: Mapped[int] = mapped_column(
        "Quantity",
        Integer,
        nullable=False,
    )

    print_quality: Mapped[str | None] = mapped_column(
        "PrintQuality",
        String(5),
        nullable=True,
        default="N",
    )

    user_id: Mapped[int | None] = mapped_column(
        "UserID",
        Integer,
        nullable=True,
    )

    user_browser: Mapped[str | None] = mapped_column(
        "UserBrowser",
        String(40),
        nullable=True,
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