"""
Product Category routes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.product_category_repository import ProductCategoryRepository
from app.services.product_category_service import ProductCategoryService
from app.schemas.product_category import (
    ProductCategoryCreate,
    ProductCategoryUpdate,
    ProductCategoryResponse,
)
from app.core.security import get_current_customer
from app.models.customer import Customer


router = APIRouter(
    prefix="/product_categories",
    tags=["Product Categories"]
)


def get_product_category_service(
    db: Session = Depends(get_db)
):
    repository = ProductCategoryRepository(db)
    return ProductCategoryService(repository)


@router.get("/", response_model=list[ProductCategoryResponse])
def get_categories(
    service: ProductCategoryService = Depends(get_product_category_service)
):
    categories = service.get_categories()
    return categories


@router.get("/{category_id}", response_model=ProductCategoryResponse)
def get_category(
    category_id: int,
    service: ProductCategoryService = Depends(get_product_category_service)
):
    try:
        category = service.get_category(category_id)
        return category

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post("/", response_model=ProductCategoryResponse)
def create_category(
    data: ProductCategoryCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductCategoryService = Depends(get_product_category_service)
):
    category = service.create_category(
        data,
        created_by=current_customer.customer_id
    )

    return category


@router.put("/{category_id}", response_model=ProductCategoryResponse)
def update_category(
    category_id: int,
    data: ProductCategoryUpdate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductCategoryService = Depends(get_product_category_service)
):
    try:
        category = service.update_category(
            category_id,
            data,
            updated_by=current_customer.customer_id
        )

        return category

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.patch("/{category_id}/deactivate", response_model=ProductCategoryResponse)
def deactivate_category(
    category_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductCategoryService = Depends(get_product_category_service)
):
    try:
        category = service.deactivate_category(
            category_id,
            updated_by=current_customer.customer_id
        )

        return category

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )