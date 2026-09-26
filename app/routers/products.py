"""
Product routes.
"""

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.core.security import get_current_customer
from app.models.customer import Customer


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

def get_product_service(
    db: Session = Depends(get_db)
):
    repository = ProductRepository(db)
    return ProductService(repository)
    
@router.get("/", response_model=list[ProductResponse])
def get_products(service: ProductService = Depends(get_product_service)):
    products = service.get_products()

    return products

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    try:
        product = service.get_product(product_id)
        return product

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

@router.post("/", response_model=ProductResponse)
def create_product(
    data: ProductCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductService = Depends(get_product_service)
):
    product = service.create_product(
        data,
        created_by=current_customer.customer_id
    )

    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductService = Depends(get_product_service)
):
    product = service.update_product(
        product_id,
        data,
        updated_by=current_customer.customer_id
    )

    return product

@router.patch("/{product_id}/deactivate", response_model=ProductResponse)
def deactivate_product(
    product_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: ProductService = Depends(get_product_service)
):
    try:
        product = service.deactivate_product(
            product_id,
            updated_by=current_customer.customer_id
        )
        return product

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )