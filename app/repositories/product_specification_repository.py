from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product_specification import ProductSpecification


class ProductSpecificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, specification_id: int):
        stmt = select(ProductSpecification).where(
            ProductSpecification.specification_id == specification_id
        )
        return self.db.scalar(stmt)

    def get_all(self):
        stmt = select(ProductSpecification)
        return self.db.scalars(stmt).all()

    def get_by_product_id(self, product_id: int):
        stmt = select(ProductSpecification).where(
            ProductSpecification.product_id == product_id
        )
        return self.db.scalars(stmt).all()

    def create(self, specification: ProductSpecification):
        self.db.add(specification)
        self.db.commit()
        self.db.refresh(specification)
        return specification