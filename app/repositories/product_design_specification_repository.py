from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product_design_specification import ProductDesignSpecification


class ProductDesignSpecificationRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, design_specification_id: int):
        stmt = select(ProductDesignSpecification).where(
            ProductDesignSpecification.design_specification_id
            == design_specification_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(ProductDesignSpecification)

        if active_only:
            stmt = stmt.where(
                ProductDesignSpecification.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def get_by_product_id(
        self,
        product_id: int,
        active_only: bool = True,
    ):
        stmt = select(ProductDesignSpecification).where(
            ProductDesignSpecification.product_id == product_id
        )

        if active_only:
            stmt = stmt.where(
                ProductDesignSpecification.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def create(
        self,
        specification: ProductDesignSpecification,
    ):
        self.db.add(specification)
        self.db.commit()
        self.db.refresh(specification)
        return specification

    def update(
        self,
        specification: ProductDesignSpecification,
        update_data: dict,
    ):
        for field, value in update_data.items():
            setattr(specification, field, value)

        self.db.commit()
        self.db.refresh(specification)
        return specification

    def deactivate(
        self,
        specification: ProductDesignSpecification,
    ):
        specification.is_active = False

        self.db.commit()
        self.db.refresh(specification)
        return specification