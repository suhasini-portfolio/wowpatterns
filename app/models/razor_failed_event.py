from datetime import datetime

from sqlalchemy import DateTime, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RazorFailedEvent(Base):
    __tablename__ = "razorfailedevents"

    razor_failed_event_id: Mapped[int] = mapped_column(
        "RazorFailedEventID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    raw_data: Mapped[str | None] = mapped_column(
        "RawData",
        Text,
        nullable=True
    )

    error_message: Mapped[str | None] = mapped_column(
        "ErrorMessage",
        Text,
        nullable=True
    )

    created_date: Mapped[datetime | None] = mapped_column(
        "CreatedDate",
        DateTime,
        nullable=True
    )