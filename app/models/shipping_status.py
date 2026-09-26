from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ShippingStatus(Base):
    __tablename__ = "shippingstatuses"

    shipping_status_id: Mapped[int] = mapped_column(
        "ShippingStatusID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    shipping_status: Mapped[str] = mapped_column(
        "ShippingStatus",
        String(255),
        nullable=False
    )

    priority: Mapped[int] = mapped_column(
        "Priority",
        Integer,
        nullable=False
    )

    status: Mapped[int] = mapped_column(
        "Status",
        Integer,
        nullable=False,
        default=1
    )

    email_subject: Mapped[str] = mapped_column(
        "EmailSubject",
        String(255),
        nullable=False
    )