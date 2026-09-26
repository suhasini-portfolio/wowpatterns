from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.shipping_status_repository import ShippingStatusRepository
from app.schemas.shipping_status import (
    ShippingStatusCreate,
    ShippingStatusResponse,
    ShippingStatusUpdate,
)
from app.services.shipping_status_service import ShippingStatusService


router = APIRouter(
    prefix="/shipping_statuses",
    tags=["Shipping Statuses"]
)


def get_service(db: Session = Depends(get_db)):
    repository = ShippingStatusRepository(db)
    return ShippingStatusService(repository)


@router.get(
    "/",
    response_model=list[ShippingStatusResponse]
)
def get_shipping_statuses(
    service: ShippingStatusService = Depends(get_service)
):
    return service.get_all_shipping_statuses()


@router.get(
    "/{shipping_status_id}",
    response_model=ShippingStatusResponse
)
def get_shipping_status(
    shipping_status_id: int,
    service: ShippingStatusService = Depends(get_service)
):
    try:
        return service.get_shipping_status(
            shipping_status_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.post(
    "/",
    response_model=ShippingStatusResponse,
    status_code=201
)
def create_shipping_status(
    data: ShippingStatusCreate,
    service: ShippingStatusService = Depends(get_service)
):
    return service.create_shipping_status(data)


@router.put(
    "/{shipping_status_id}",
    response_model=ShippingStatusResponse
)
def update_shipping_status(
    shipping_status_id: int,
    data: ShippingStatusUpdate,
    service: ShippingStatusService = Depends(get_service)
):
    try:
        return service.update_shipping_status(
            shipping_status_id,
            data
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )