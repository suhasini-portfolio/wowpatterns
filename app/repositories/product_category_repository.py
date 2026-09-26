from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product_category import ProductCategory


class ProductCategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_category_id: int):
        stmt = select(ProductCategory).where(
            ProductCategory.product_category_id == product_category_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(ProductCategory)

        if active_only:
            stmt = stmt.where(ProductCategory.is_active.is_(True))

        return self.db.scalars(stmt).all()

    def create(self, category: ProductCategory):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def update(self, category: ProductCategory, update_data: dict):
        for field, value in update_data.items():
            setattr(category, field, value)

        category.updated_date = datetime.now()

        self.db.commit()
        self.db.refresh(category)

        return category

    def deactivate(self, category: ProductCategory):
        category.is_active = False

        self.db.commit()
        self.db.refresh(category)

        return category