from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Inquiry(Base):
    __tablename__ = "inquiries"

    inquiry_id: Mapped[int] = mapped_column(
        "InquiryID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str | None] = mapped_column(
        "Name",
        String(100),
        nullable=True
    )

    company: Mapped[str | None] = mapped_column(
        "Company",
        String(100),
        nullable=True
    )

    country: Mapped[str | None] = mapped_column(
        "Country",
        String(100),
        nullable=True
    )

    email: Mapped[str | None] = mapped_column(
        "Email",
        String(100),
        nullable=True
    )

    mobile: Mapped[str | None] = mapped_column(
        "Mobile",
        String(15),
        nullable=True
    )

    mobile_country_id: Mapped[int | None] = mapped_column(
        "MobileCountryID",
        Integer,
        nullable=True,
        default=0
    )

    mobile_country_code: Mapped[int | None] = mapped_column(
        "MobileCountryCode",
        Integer,
        nullable=True
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False,
        default=0
    )

    inquiry_type: Mapped[str] = mapped_column(
        "InquiryType",
        String(5),
        nullable=False,
        default="G"
    )

    message: Mapped[str | None] = mapped_column(
        "Message",
        Text,
        nullable=True
    )

    order_id: Mapped[int] = mapped_column(
        "OrderID",
        Integer,
        nullable=False,
        default=0
    )

    design: Mapped[str | None] = mapped_column(
        "Design",
        String(250),
        nullable=True
    )

    note: Mapped[str | None] = mapped_column(
        "Note",
        Text,
        nullable=True
    )

    created_by: Mapped[int] = mapped_column(
        "CreatedBy",
        Integer,
        nullable=False,
        default=0
    )

    created_date: Mapped[datetime] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=False
    )