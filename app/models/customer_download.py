from datetime import datetime

from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class CustomerDownload(Base):
    __tablename__ = "customer_downloads"

    download_id: Mapped[int] = mapped_column(
        "DownloadID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    customer_id: Mapped[int] = mapped_column(
        "CustomerID",
        Integer,
        nullable=False,
    )

    product_id: Mapped[int] = mapped_column(
        "ProductID",
        Integer,
        nullable=False,
    )

    download_count: Mapped[int] = mapped_column(
        "DownloadCount",
        Integer,
        nullable=False,
    )

    last_download: Mapped[datetime] = mapped_column(
        "LastDownload",
        DateTime,
        nullable=False,
    )