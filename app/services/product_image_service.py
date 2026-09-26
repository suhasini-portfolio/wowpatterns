"""
Product Image service.
"""

from datetime import datetime

from app.models.product_image import ProductImage
from app.repositories.product_image_repository import ProductImageRepository
from app.schemas.product_image import (
    ProductImageCreate,
    ProductImageUpdate,
)


class ProductImageService:
    def __init__(self, repository: ProductImageRepository):
        self.repository = repository

    def create_image(
        self,
        data: ProductImageCreate,
        created_by: int,
    ):
        image_data = data.model_dump()

        image = ProductImage(
            **image_data,
            created_by=created_by,
            created_date=datetime.now(),
        )

        return self.repository.create(image)

    def get_image(self, product_image_id: int):
        image = self.repository.get_by_id(product_image_id)

        if not image:
            raise ValueError("No product image exists")

        return image

    def get_images(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def get_product_images(
        self,
        product_id: int,
        active_only: bool = True,
    ):
        return self.repository.get_by_product_id(
            product_id,
            active_only,
        )

    def update_image(
        self,
        product_image_id: int,
        data: ProductImageUpdate,
        updated_by: int,
    ):
        image = self.repository.get_by_id(product_image_id)

        if not image:
            raise ValueError("No product image exists")

        image_data = data.model_dump(
            exclude_unset=True
        )

        image.updated_by = updated_by
        image.updated_date = datetime.now()

        return self.repository.update(
            image,
            image_data,
        )

    def deactivate_image(
        self,
        product_image_id: int,
        updated_by: int,
    ):
        image = self.repository.get_by_id(product_image_id)

        if not image:
            raise ValueError("No product image exists")

        image.updated_by = updated_by
        image.updated_date = datetime.now()

        return self.repository.deactivate(image)