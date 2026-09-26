from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.product_design_specification_repository import (
    ProductDesignSpecificationRepository,
)
from app.schemas.product_design_specification import (
    ProductDesignSpecificationCreate,
    ProductDesignSpecificationResponse,
    ProductDesignSpecificationUpdate,
)
from app.services.product_design_specification_service import (
    ProductDesignSpecificationService,
)


router = APIRouter(
    prefix="/product_design_specifications",
    tags=["Product Design Specifications"],
)


def get_product_design_specification_service(
    db: Session = Depends(get_db),
):
    repository = ProductDesignSpecificationRepository(db)
    return ProductDesignSpecificationService(repository)


@router.get(
    "/",
    response_model=list[ProductDesignSpecificationResponse],
)
def get_specifications(
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    return service.get_specifications()


@router.get(
    "/product/{product_id}",
    response_model=list[ProductDesignSpecificationResponse],
)
def get_product_specifications(
    product_id: int,
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    return service.get_product_specifications(product_id)


@router.get(
    "/{design_specification_id}",
    response_model=ProductDesignSpecificationResponse,
)
def get_specification(
    design_specification_id: int,
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    try:
        return service.get_specification(
            design_specification_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=ProductDesignSpecificationResponse,
)
def create_specification(
    data: ProductDesignSpecificationCreate,
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    return service.create_specification(data)


@router.put(
    "/{design_specification_id}",
    response_model=ProductDesignSpecificationResponse,
)
def update_specification(
    design_specification_id: int,
    data: ProductDesignSpecificationUpdate,
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    try:
        return service.update_specification(
            design_specification_id,
            data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/{design_specification_id}/deactivate",
    response_model=ProductDesignSpecificationResponse,
)
def deactivate_specification(
    design_specification_id: int,
    service: ProductDesignSpecificationService = Depends(
        get_product_design_specification_service
    ),
):
    try:
        return service.deactivate_specification(
            design_specification_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )