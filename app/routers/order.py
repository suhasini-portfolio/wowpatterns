from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.order_repository import OrderRepository
from app.schemas.order import (
    OrderCreate,
    OrderResponse,
    OrderUpdate,
)
from app.services.order_service import OrderService


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


def get_service(db: Session = Depends(get_db)):
    repository = OrderRepository(db)
    return OrderService(repository)


@router.get(
    "/",
    response_model=list[OrderResponse],
)
def get_my_orders(
    current_customer=Depends(get_current_customer),
    service: OrderService = Depends(get_service),
):
    return service.get_customer_orders(
        current_customer.customer_id
    )


@router.get(
    "/{order_id}",
    response_model=OrderResponse,
)
def get_order(
    order_id: int,
    current_customer=Depends(get_current_customer),
    service: OrderService = Depends(get_service),
):
    try:
        return service.get_order(
            order_id=order_id,
            customer_id=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=OrderResponse,
    status_code=201,
)
def create_order(
    data: OrderCreate,
    current_customer=Depends(get_current_customer),
    service: OrderService = Depends(get_service),
):
    return service.create_order(
        data=data,
        customer_id=current_customer.customer_id,
    )


@router.put(
    "/{order_id}",
    response_model=OrderResponse,
)
def update_order(
    order_id: int,
    data: OrderUpdate,
    current_customer=Depends(get_current_customer),
    service: OrderService = Depends(get_service),
):
    try:
        return service.update_order(
            order_id=order_id,
            data=data,
            customer_id=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/{order_id}/deactivate",
    response_model=OrderResponse,
)
def deactivate_order(
    order_id: int,
    current_customer=Depends(get_current_customer),
    service: OrderService = Depends(get_service),
):
    try:
        return service.deactivate_order(
            order_id=order_id,
            customer_id=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )