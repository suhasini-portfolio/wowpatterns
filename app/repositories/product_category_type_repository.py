from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product_category_type import ProductCategoryType


class ProductCategoryTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_category_type_id: int):
        stmt = select(ProductCategoryType).where(
            ProductCategoryType.product_category_type_id == product_category_type_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(ProductCategoryType)

        if active_only:
            stmt = stmt.where(
                ProductCategoryType.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def create(self, category_type: ProductCategoryType):
        self.db.add(category_type)
        self.db.commit()
        self.db.refresh(category_type)
        return category_type

    def update(self, category_type: ProductCategoryType, update_data: dict):
        for field, value in update_data.items():
            setattr(category_type, field, value)

        self.db.commit()
        self.db.refresh(category_type)
        return category_type

    def deactivate(self, category_type: ProductCategoryType):
        category_type.is_active = False

        self.db.commit()
        self.db.refresh(category_type)
        return category_type