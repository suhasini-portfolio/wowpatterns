"""
Product Image routes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.models.customer import Customer
from app.repositories.product_image_repository import ProductImageRepository
from app.schemas.product_image import (
    ProductImageCreate,
    ProductImageUpdate,
    ProductImageResponse,
)
from app.services.product_image_service import ProductImageService


router = APIRouter(
    prefix="/product_images",
    tags=["Product Images"],
)


def get_product_image_service(
    db: Session = Depends(get_db),
):
    repository = ProductImageRepository(db)
    return ProductImageService(repository)


@router.get(
    "/",
    response_model=list[ProductImageResponse],
)
def get_images(
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    return service.get_images()


@router.get(
    "/{product_image_id}",
    response_model=ProductImageResponse,
)
def get_image(
    product_image_id: int,
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    try:
        return service.get_image(product_image_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get(
    "/product/{product_id}",
    response_model=list[ProductImageResponse],
)
def get_product_images(
    product_id: int,
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    return service.get_product_images(product_id)


@router.post(
    "/",
    response_model=ProductImageResponse,
)
def create_image(
    data: ProductImageCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    return service.create_image(
        data,
        created_by=current_customer.customer_id,
    )


@router.put(
    "/{product_image_id}",
    response_model=ProductImageResponse,
)
def update_image(
    product_image_id: int,
    data: ProductImageUpdate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    try:
        return service.update_image(
            product_image_id,
            data,
            updated_by=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/{product_image_id}/deactivate",
    response_model=ProductImageResponse,
)
def deactivate_image(
    product_image_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductImageService = Depends(
        get_product_image_service
    ),
):
    try:
        return service.deactivate_image(
            product_image_id,
            updated_by=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )