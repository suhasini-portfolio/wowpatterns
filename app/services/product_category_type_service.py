"""
Product Category Type service.
"""

from app.models.product_category_type import ProductCategoryType
from app.repositories.product_category_type_repository import (
    ProductCategoryTypeRepository,
)
from app.schemas.product_category_type import (
    ProductCategoryTypeCreate,
    ProductCategoryTypeUpdate,
)


class ProductCategoryTypeService:
    def __init__(self, repository: ProductCategoryTypeRepository):
        self.repository = repository

    def create_category_type(self, data: ProductCategoryTypeCreate):
        category_type_data = data.model_dump()

        category_type = ProductCategoryType(
            **category_type_data
        )

        return self.repository.create(category_type)

    def get_category_type(self, product_category_type_id: int):
        category_type = self.repository.get_by_id(
            product_category_type_id
        )

        if not category_type:
            raise ValueError("No product category type exists")

        return category_type

    def get_category_types(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def update_category_type(
        self,
        product_category_type_id: int,
        data: ProductCategoryTypeUpdate,
    ):
        category_type = self.repository.get_by_id(
            product_category_type_id
        )

        if not category_type:
            raise ValueError("No product category type exists")

        category_type_data = data.model_dump(
            exclude_unset=True
        )

        return self.repository.update(
            category_type,
            category_type_data
        )

    def deactivate_category_type(
        self,
        product_category_type_id: int,
    ):
        category_type = self.repository.get_by_id(
            product_category_type_id
        )

        if not category_type:
            raise ValueError("No product category type exists")

        return self.repository.deactivate(category_type)