"""
Product service.
"""

from datetime import datetime

from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:

    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def create_product(self, data: ProductCreate, created_by: int):
        product_data = data.model_dump()

        product = Product(
            **product_data,
            created_by=created_by,
            created_date=datetime.now()
        )

        return self.repository.create(product)

    def get_product(self, product_id: int):
        product = self.repository.get_by_id(product_id)

        if not product:
            raise ValueError("No product exists")

        return product

    def get_products(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def update_product(self, product_id: int, data: ProductUpdate, updated_by: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("No product exists")
        product_data = data.model_dump(exclude_unset=True)
        product.updated_by = updated_by
        return self.repository.update(product, product_data)

    def deactivate_product(self, product_id: int, updated_by: int):
        product = self.repository.get_by_id(product_id)
        if not product:
            raise ValueError("No product exists")
        product.updated_by = updated_by
        product.updated_date = datetime.now()
        return self.repository.deactivate(product)