"""
Product repository.
"""
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int):
        stmt = select(Product).where(
            Product.product_id == product_id
        )

        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(Product)
        if active_only:
            stmt = stmt.where(Product.is_active == True)
        return self.db.scalars(stmt).all()

    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

        return product

    def update(self, product: Product, update_data: dict):
        for field, value in update_data.items():
            setattr(product, field, value)

        product.updated_date = datetime.now()

        self.db.commit()
        self.db.refresh(product)

        return product

    def deactivate(self, product: Product):
        product.is_active = False
        
        self.db.commit()
        self.db.refresh(product)
        
        return product