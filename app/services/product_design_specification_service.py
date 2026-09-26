from datetime import datetime

from app.models.product_design_specification import ProductDesignSpecification
from app.repositories.product_design_specification_repository import (
    ProductDesignSpecificationRepository,
)
from app.schemas.product_design_specification import (
    ProductDesignSpecificationCreate,
    ProductDesignSpecificationUpdate,
)


class ProductDesignSpecificationService:
    def __init__(
        self,
        repository: ProductDesignSpecificationRepository,
    ):
        self.repository = repository

    def create_specification(
        self,
        data: ProductDesignSpecificationCreate,
    ):
        specification = ProductDesignSpecification(
            product_id=data.product_id,
            artist_id=data.artist_id,
            design_id=data.design_id,
            is_individual_design_price=data.is_individual_design_price,
            design_price=data.design_price,
            is_repeatable=data.is_repeatable,
            design_file_type_id=data.design_file_type_id,
            file_name=data.file_name,
            is_active=data.is_active,
            created_by=data.created_by,
            created_date=datetime.now(),
        )

        return self.repository.create(specification)

    def get_specification(
        self,
        design_specification_id: int,
    ):
        specification = self.repository.get_by_id(
            design_specification_id
        )

        if not specification:
            raise ValueError(
                "No product design specification exists"
            )

        return specification

    def get_specifications(
        self,
        active_only: bool = True,
    ):
        return self.repository.get_all(active_only)

    def get_product_specifications(
        self,
        product_id: int,
        active_only: bool = True,
    ):
        return self.repository.get_by_product_id(
            product_id,
            active_only,
        )

    def update_specification(
        self,
        design_specification_id: int,
        data: ProductDesignSpecificationUpdate,
    ):
        specification = self.repository.get_by_id(
            design_specification_id
        )

        if not specification:
            raise ValueError(
                "No product design specification exists"
            )

        update_data = data.model_dump(exclude_unset=True)

        update_data.pop("created_by", None)

        specification.updated_date = datetime.now()

        return self.repository.update(
            specification,
            update_data,
        )

    def deactivate_specification(
        self,
        design_specification_id: int,
    ):
        specification = self.repository.get_by_id(
            design_specification_id
        )

        if not specification:
            raise ValueError(
                "No product design specification exists"
            )

        specification.updated_date = datetime.now()

        return self.repository.deactivate(specification)