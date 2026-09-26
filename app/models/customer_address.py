from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class CustomerAddress(Base):
    __tablename__ = "customer_addresses"

    customer_address_id: Mapped[int] = mapped_column(
        "CustomerAddressID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    customer_id: Mapped[int] = mapped_column(
        "CustomerID",
        Integer,
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        "FullName",
        String(100),
        nullable=False,
    )

    mobile_country_id: Mapped[int] = mapped_column(
        "MobileCountryID",
        Integer,
        nullable=False,
    )

    mobile_country_code: Mapped[int] = mapped_column(
        "MobileCountryCode",
        Integer,
        nullable=False,
    )

    mobile: Mapped[str] = mapped_column(
        "Mobile",
        String(15),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        "Email",
        String(50),
        nullable=False,
    )

    country_id: Mapped[int] = mapped_column(
        "CountryID",
        Integer,
        nullable=False,
    )

    state_id: Mapped[int] = mapped_column(
        "StateID",
        Integer,
        nullable=False,
    )

    city_id: Mapped[int] = mapped_column(
        "CityID",
        Integer,
        nullable=False,
    )

    zip_code: Mapped[str] = mapped_column(
        "ZipCode",
        String(20),
        nullable=False,
    )

    landmark: Mapped[str | None] = mapped_column(
        "Landmark",
        String(500),
        nullable=True,
    )

    address: Mapped[str] = mapped_column(
        "Address",
        Text,
        nullable=False,
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