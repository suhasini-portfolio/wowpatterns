"""
Product Specification routes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.models.customer import Customer
from app.repositories.product_specification_repository import (
    ProductSpecificationRepository,
)
from app.schemas.product_specification import (
    ProductSpecificationCreate,
    ProductSpecificationResponse,
)
from app.services.product_specification_service import (
    ProductSpecificationService,
)


router = APIRouter(
    prefix="/product_specifications",
    tags=["Product Specifications"],
)


def get_product_specification_service(
    db: Session = Depends(get_db),
):
    repository = ProductSpecificationRepository(db)
    return ProductSpecificationService(repository)


@router.get(
    "/",
    response_model=list[ProductSpecificationResponse],
)
def get_specifications(
    service: ProductSpecificationService = Depends(
        get_product_specification_service
    ),
):
    return service.get_specifications()


@router.get(
    "/{specification_id}",
    response_model=ProductSpecificationResponse,
)
def get_specification(
    specification_id: int,
    service: ProductSpecificationService = Depends(
        get_product_specification_service
    ),
):
    try:
        return service.get_specification(specification_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get(
    "/product/{product_id}",
    response_model=list[ProductSpecificationResponse],
)
def get_product_specifications(
    product_id: int,
    service: ProductSpecificationService = Depends(
        get_product_specification_service
    ),
):
    return service.get_product_specifications(product_id)


@router.post(
    "/",
    response_model=ProductSpecificationResponse,
)
def create_specification(
    data: ProductSpecificationCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductSpecificationService = Depends(
        get_product_specification_service
    ),
):
    return service.create_specification(
        data,
        created_by=current_customer.customer_id,
    )