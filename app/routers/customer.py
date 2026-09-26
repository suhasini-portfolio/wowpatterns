"""
Customer Router
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerRegisterRequest, CustomerResponse, CustomerLoginRequest, TokenResponse, CustomerProfileResponse, CustomerProfileUpdateRequest
from app.services.customer_service import CustomerService
from app.models.customer import Customer

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post(
    "/register",
    response_model=CustomerResponse,
    status_code=201
)
def register_customer(
    request:CustomerRegisterRequest,
    db: Session = Depends(get_db)
):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    try:
        return service.register_customer(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    request: CustomerLoginRequest,
    db: Session = Depends(get_db)
):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    try:
        return service.login(request)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/me", response_model=CustomerProfileResponse)
def get_my_profile(
    current_customer: Customer = Depends(get_current_customer)
):
    return current_customer

@router.put("/me", response_model=CustomerProfileResponse)
def update_my_profile(
    request: CustomerProfileUpdateRequest,
    current_customer: Customer = Depends(get_current_customer),
    db: Session = Depends(get_db)
):
    repository = CustomerRepository(db)
    service = CustomerService(repository)

    return service.update_profile(
        customer=current_customer,
        request=request
    )

""" def get_my_profile(
    customer_id: int = Depends(get_current_customer_id),
    db: Session = Depends(get_db)
):
    repository = CustomerRepository(db)

    customer = repository.get_by_id(customer_id)

    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer """