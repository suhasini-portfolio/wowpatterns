from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.models.customer import Customer
from app.repositories.customer_address_repository import CustomerAddressRepository
from app.schemas.customer_address import (
    CustomerAddressCreate,
    CustomerAddressResponse,
    CustomerAddressUpdate,
)
from app.services.customer_address_service import CustomerAddressService


router = APIRouter(
    prefix="/customer_addresses",
    tags=["Customer Addresses"],
)


def get_customer_address_service(
    db: Session = Depends(get_db),
):
    repository = CustomerAddressRepository(db)
    return CustomerAddressService(repository)


@router.get(
    "/",
    response_model=list[CustomerAddressResponse],
)
def get_addresses(
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    return service.get_addresses()


@router.get(
    "/{customer_address_id}",
    response_model=CustomerAddressResponse,
)
def get_address(
    customer_address_id: int,
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    try:
        return service.get_address(customer_address_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get(
    "/customer/{customer_id}",
    response_model=list[CustomerAddressResponse],
)
def get_customer_addresses(
    customer_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    # A customer can access only their own addresses.
    if customer_id != current_customer.customer_id:
        raise HTTPException(
            status_code=403,
            detail="You can only access your own addresses",
        )

    return service.get_customer_addresses(customer_id)


@router.post(
    "/",
    response_model=CustomerAddressResponse,
)
def create_address(
    data: CustomerAddressCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    return service.create_address(
        data,
        customer_id=current_customer.customer_id,
    )


@router.put(
    "/{customer_address_id}",
    response_model=CustomerAddressResponse,
)
def update_address(
    customer_address_id: int,
    data: CustomerAddressUpdate,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    try:
        address = service.get_address(customer_address_id)

        if address.customer_id != current_customer.customer_id:
            raise HTTPException(
                status_code=403,
                detail="You can only update your own address",
            )

        return service.update_address(
            customer_address_id,
            data,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/{customer_address_id}/deactivate",
    response_model=CustomerAddressResponse,
)
def deactivate_address(
    customer_address_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerAddressService = Depends(
        get_customer_address_service
    ),
):
    try:
        address = service.get_address(customer_address_id)

        if address.customer_id != current_customer.customer_id:
            raise HTTPException(
                status_code=403,
                detail="You can only deactivate your own address",
            )

        return service.deactivate_address(
            customer_address_id,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )