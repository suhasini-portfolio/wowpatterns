"""
Product Category service.
"""

from datetime import datetime

from app.models.product_category import ProductCategory
from app.repositories.product_category_repository import ProductCategoryRepository
from app.schemas.product_category import ProductCategoryCreate, ProductCategoryUpdate


class ProductCategoryService:

    def __init__(self, repository: ProductCategoryRepository):
        self.repository = repository

    def create_category(self, data: ProductCategoryCreate, created_by: int):
        category_data = data.model_dump()

        product_category = ProductCategory(
            **category_data,
            created_by=created_by,
            created_date=datetime.now()
        )

        return self.repository.create(product_category)

    def get_category(self, product_category_id: int):
        category = self.repository.get_by_id(product_category_id)

        if not category:
            raise ValueError("No product category exists")
        
        return category

    def get_categories(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def update_category(self, product_category_id: int, data: ProductCategoryUpdate, updated_by: int):
        category = self.repository.get_by_id(product_category_id)

        if not category:
            raise ValueError("No product category exists")
        
        category_data = data.model_dump(exclude_unset=True)
        
        category.updated_by = updated_by

        return self.repository.update(category, category_data)

    def deactivate_category(self, product_category_id: int, updated_by: int):
        category = self.repository.get_by_id(product_category_id)

        if not category:
            raise ValueError("No product category exists")
        
        category.updated_by = updated_by
        category.updated_date = datetime.now()

        return self.repository.deactivate(category)