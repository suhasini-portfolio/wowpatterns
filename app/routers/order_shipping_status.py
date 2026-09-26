from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.order_shipping_status_repository import (
    OrderShippingStatusRepository,
)
from app.schemas.order_shipping_status import (
    OrderShippingStatusCreate,
    OrderShippingStatusResponse,
    OrderShippingStatusUpdate,
)
from app.services.order_shipping_status_service import (
    OrderShippingStatusService,
)


router = APIRouter(
    prefix="/order_shipping_statuses",
    tags=["Order Shipping Statuses"],
)


def get_service(db: Session = Depends(get_db)):
    repository = OrderShippingStatusRepository(db)
    return OrderShippingStatusService(repository)


@router.get(
    "/order/{order_id}",
    response_model=list[OrderShippingStatusResponse],
)
def get_order_shipping_statuses(
    order_id: int,
    service: OrderShippingStatusService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    return service.get_order_shipping_statuses(order_id)


@router.get(
    "/item/{order_item_id}",
    response_model=list[OrderShippingStatusResponse],
)
def get_order_item_shipping_statuses(
    order_item_id: int,
    service: OrderShippingStatusService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    return service.get_order_item_shipping_statuses(order_item_id)


@router.get(
    "/{order_shipping_status_id}",
    response_model=OrderShippingStatusResponse,
)
def get_order_shipping_status(
    order_shipping_status_id: int,
    service: OrderShippingStatusService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.get_shipping_status(order_shipping_status_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post(
    "/",
    response_model=OrderShippingStatusResponse,
    status_code=201,
)
def create_order_shipping_status(
    data: OrderShippingStatusCreate,
    service: OrderShippingStatusService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    return service.create_shipping_status(
        data,
        current_customer.customer_id,
    )


@router.put(
    "/{order_shipping_status_id}",
    response_model=OrderShippingStatusResponse,
)
def update_order_shipping_status(
    order_shipping_status_id: int,
    data: OrderShippingStatusUpdate,
    service: OrderShippingStatusService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.update_shipping_status(
            order_shipping_status_id,
            data,
            current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))