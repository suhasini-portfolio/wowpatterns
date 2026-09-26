from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product_image import ProductImage


class ProductImageRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_image_id: int):
        stmt = select(ProductImage).where(
            ProductImage.product_image_id == product_image_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(ProductImage)

        if active_only:
            stmt = stmt.where(
                ProductImage.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def get_by_product_id(
        self,
        product_id: int,
        active_only: bool = True,
    ):
        stmt = select(ProductImage).where(
            ProductImage.product_id == product_id
        )

        if active_only:
            stmt = stmt.where(
                ProductImage.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def create(self, image: ProductImage):
        self.db.add(image)
        self.db.commit()
        self.db.refresh(image)
        return image

    def update(self, image: ProductImage, update_data: dict):
        for field, value in update_data.items():
            setattr(image, field, value)

        self.db.commit()
        self.db.refresh(image)
        return image

    def deactivate(self, image: ProductImage):
        image.is_active = False
        self.db.commit()
        self.db.refresh(image)
        return image