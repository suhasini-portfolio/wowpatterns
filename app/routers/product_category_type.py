"""
Product Category Type routes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.product_category_type_repository import (
    ProductCategoryTypeRepository,
)
from app.services.product_category_type_service import (
    ProductCategoryTypeService,
)
from app.schemas.product_category_type import (
    ProductCategoryTypeCreate,
    ProductCategoryTypeUpdate,
    ProductCategoryTypeResponse,
)


router = APIRouter(
    prefix="/product_category_types",
    tags=["Product Category Types"]
)


def get_product_category_type_service(
    db: Session = Depends(get_db)
):
    repository = ProductCategoryTypeRepository(db)
    return ProductCategoryTypeService(repository)


@router.get(
    "/",
    response_model=list[ProductCategoryTypeResponse]
)
def get_category_types(
    service: ProductCategoryTypeService = Depends(
        get_product_category_type_service
    )
):
    return service.get_category_types()


@router.get(
    "/{category_type_id}",
    response_model=ProductCategoryTypeResponse
)
def get_category_type(
    category_type_id: int,
    service: ProductCategoryTypeService = Depends(
        get_product_category_type_service
    )
):
    try:
        return service.get_category_type(category_type_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post(
    "/",
    response_model=ProductCategoryTypeResponse
)
def create_category_type(
    data: ProductCategoryTypeCreate,
    service: ProductCategoryTypeService = Depends(
        get_product_category_type_service
    )
):
    return service.create_category_type(data)


@router.put(
    "/{category_type_id}",
    response_model=ProductCategoryTypeResponse
)
def update_category_type(
    category_type_id: int,
    data: ProductCategoryTypeUpdate,
    service: ProductCategoryTypeService = Depends(
        get_product_category_type_service
    )
):
    try:
        return service.update_category_type(
            category_type_id,
            data
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.patch(
    "/{category_type_id}/deactivate",
    response_model=ProductCategoryTypeResponse
)
def deactivate_category_type(
    category_type_id: int,
    service: ProductCategoryTypeService = Depends(
        get_product_category_type_service
    )
):
    try:
        return service.deactivate_category_type(
            category_type_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )