"""
Customer model.
"""

from datetime import datetime

from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.base import Base

class Customer(Base):
    __tablename__ = "customers"

    customer_id: Mapped[int] = mapped_column(
        "CustomerID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    customer_code: Mapped[str] = mapped_column(
        "CustomerCode",
        String(20),
        unique=True,
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        "FullName",
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        "Email",
        String(150),
        unique=True,
        nullable=False
    )

    is_email_verified: Mapped[bool] = mapped_column(
        "IsEmailVerified",
        Boolean,
        default=False,
    )

    mobile_country_id: Mapped[int] = mapped_column(
        "MobileCountryID",
        Integer,
        nullable=False
    )

    mobile_country_code: Mapped[str] = mapped_column(
        "MobileCountryCode",
        String(10),
        nullable=False
    )

    mobile: Mapped[str] = mapped_column(
        "Mobile",
        String(20),
        nullable=False
    )

    password: Mapped[str] = mapped_column(
        "Password",
        String(255),
        nullable=False
    )

    google_id: Mapped[str | None] = mapped_column(
        "GoogleID",
        String(100),
        nullable=True,
    )

    joining_date: Mapped[datetime] = mapped_column(
        "JoiningDate",
        DateTime,
        nullable=False
    )

    is_subscribe_to_newsletter: Mapped[bool] = mapped_column(
        "IsSubscribeToNewsletter",
        Boolean,
        default=False,
    )

    is_active: Mapped[int] = mapped_column(
        "IsActive",
        Boolean,
        default=1
    )

    platform: Mapped[str] = mapped_column(
        "Platform",
        String(15),
        default="web",
    )

    forgot_password_link_expiry_date: Mapped[datetime | None] = mapped_column(
        "ForgotPasswordLinkExpiryDate",
        DateTime,
        nullable=True,
    )

    is_forgot_password_link_expired: Mapped[bool] = mapped_column(
        "IsForgotPasswordLinkExpired",
        Boolean,
        default=False,
    )

    updated_by: Mapped[int | None] = mapped_column(
        "UpdatedBy",
        Integer,
        nullable=True,
    )

    updated_date: Mapped[datetime | None] = mapped_column(
        "UpdatedDate",
        DateTime,
        nullable=True,
    )