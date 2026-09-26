from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.shipping_price_repository import ShippingPriceRepository
from app.schemas.shipping_price import (
    ShippingPriceCreate,
    ShippingPriceResponse,
    ShippingPriceUpdate,
)
from app.services.shipping_price_service import ShippingPriceService


router = APIRouter(
    prefix="/shipping_prices",
    tags=["Shipping Prices"],
)


def get_service(db: Session = Depends(get_db)):
    repository = ShippingPriceRepository(db)
    return ShippingPriceService(repository)


@router.get(
    "/",
    response_model=list[ShippingPriceResponse],
)
def get_shipping_prices(
    service: ShippingPriceService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    return service.get_all_shipping_prices()


@router.get(
    "/{shipping_price_id}",
    response_model=ShippingPriceResponse,
)
def get_shipping_price(
    shipping_price_id: int,
    service: ShippingPriceService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.get_shipping_price(shipping_price_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post(
    "/",
    response_model=ShippingPriceResponse,
    status_code=201,
)
def create_shipping_price(
    data: ShippingPriceCreate,
    service: ShippingPriceService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    return service.create_shipping_price(
        data,
        current_customer.customer_id,
    )


@router.put(
    "/{shipping_price_id}",
    response_model=ShippingPriceResponse,
)
def update_shipping_price(
    shipping_price_id: int,
    data: ShippingPriceUpdate,
    service: ShippingPriceService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.update_shipping_price(
            shipping_price_id,
            data,
            current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.patch(
    "/{shipping_price_id}/deactivate",
    response_model=ShippingPriceResponse,
)
def deactivate_shipping_price(
    shipping_price_id: int,
    service: ShippingPriceService = Depends(get_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.deactivate_shipping_price(
            shipping_price_id,
            current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))