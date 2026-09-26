from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class DesignFileType(Base):
    __tablename__ = "design_filetypes"

    design_file_type_id: Mapped[int] = mapped_column(
        "DesignFileTypeID",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    design_file_type: Mapped[str] = mapped_column(
        "DesignFileType",
        String(20),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        nullable=False,
        default=True,
    )