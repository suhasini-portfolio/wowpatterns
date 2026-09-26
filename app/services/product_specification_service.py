"""
Product Specification service.
"""

from datetime import datetime

from app.models.product_specification import ProductSpecification
from app.repositories.product_specification_repository import (
    ProductSpecificationRepository,
)
from app.schemas.product_specification import ProductSpecificationCreate


class ProductSpecificationService:
    def __init__(self, repository: ProductSpecificationRepository):
        self.repository = repository

    def create_specification(
        self,
        data: ProductSpecificationCreate,
        created_by: int,
    ):
        specification_data = data.model_dump()

        specification = ProductSpecification(
            **specification_data,
            created_by=created_by,
            created_date=datetime.now(),
        )

        return self.repository.create(specification)

    def get_specification(self, specification_id: int):
        specification = self.repository.get_by_id(specification_id)

        if not specification:
            raise ValueError("No product specification exists")

        return specification

    def get_specifications(self):
        return self.repository.get_all()

    def get_product_specifications(self, product_id: int):
        return self.repository.get_by_product_id(product_id)