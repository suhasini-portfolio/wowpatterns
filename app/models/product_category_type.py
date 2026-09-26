from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class ProductCategoryType(Base):
    __tablename__ = "product_category_types"

    product_category_type_id: Mapped[int] = mapped_column(
        "ProductCategoryTypeID",
        Integer,
        primary_key=True,
        autoincrement=True
    )

    product_category_type: Mapped[str] = mapped_column(
        "ProductCategoryType",
        String(20),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        "IsActive",
        Boolean,
        nullable=False,
        default=True
    )