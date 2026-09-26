from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.order_item_repository import OrderItemRepository
from app.repositories.order_repository import OrderRepository
from app.schemas.order_item import (
    OrderItemCreate,
    OrderItemResponse,
    OrderItemUpdate,
)
from app.services.order_item_service import OrderItemService


router = APIRouter(
    prefix="/order_items",
    tags=["Order Items"]
)


def get_service(db: Session = Depends(get_db)):
    repository = OrderItemRepository(db)
    order_repository = OrderRepository(db)

    return OrderItemService(
        repository=repository,
        order_repository=order_repository
    )


@router.get(
    "/order/{order_id}",
    response_model=list[OrderItemResponse]
)
def get_order_items(
    order_id: int,
    current_customer=Depends(get_current_customer),
    service: OrderItemService = Depends(get_service)
):
    try:
        return service.get_order_items(
            order_id=order_id,
            customer_id=current_customer.customer_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get(
    "/{order_item_id}",
    response_model=OrderItemResponse
)
def get_order_item(
    order_item_id: int,
    current_customer=Depends(get_current_customer),
    service: OrderItemService = Depends(get_service)
):
    try:
        return service.get_order_item(
            order_item_id=order_item_id,
            customer_id=current_customer.customer_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post(
    "/",
    response_model=OrderItemResponse,
    status_code=201
)
def create_order_item(
    data: OrderItemCreate,
    current_customer=Depends(get_current_customer),
    service: OrderItemService = Depends(get_service)
):
    try:
        return service.create_order_item(
            data=data,
            customer_id=current_customer.customer_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.put(
    "/{order_item_id}",
    response_model=OrderItemResponse
)
def update_order_item(
    order_item_id: int,
    data: OrderItemUpdate,
    current_customer=Depends(get_current_customer),
    service: OrderItemService = Depends(get_service)
):
    try:
        return service.update_order_item(
            order_item_id=order_item_id,
            data=data,
            customer_id=current_customer.customer_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.patch(
    "/{order_item_id}/deactivate",
    response_model=OrderItemResponse
)
def deactivate_order_item(
    order_item_id: int,
    current_customer=Depends(get_current_customer),
    service: OrderItemService = Depends(get_service)
):
    try:
        return service.deactivate_order_item(
            order_item_id=order_item_id,
            customer_id=current_customer.customer_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )