from datetime import datetime

from app.models.shipping_price import ShippingPrice
from app.repositories.shipping_price_repository import ShippingPriceRepository
from app.schemas.shipping_price import (
    ShippingPriceCreate,
    ShippingPriceUpdate,
)


class ShippingPriceService:
    def __init__(self, repository: ShippingPriceRepository):
        self.repository = repository

    def get_shipping_price(self, shipping_price_id: int):
        shipping_price = self.repository.get_by_id(shipping_price_id)

        if not shipping_price:
            raise ValueError("Shipping price not found")

        return shipping_price

    def get_all_shipping_prices(self, active_only: bool = True):
        return self.repository.get_all(active_only=active_only)

    def create_shipping_price(
        self,
        data: ShippingPriceCreate,
        user_id: int,
    ):
        now = datetime.now()

        shipping_price = ShippingPrice(
            shipping_type=data.shipping_type,
            country_id=data.country_id,
            shipping_amount=data.shipping_amount,
            shipping_price=data.shipping_price,
            is_active=True,
            delivery_period=data.delivery_period,
            extra_item_price=data.extra_item_price,
            created_by=user_id,
            created_date=now,
            updated_by=user_id,
            updated_date=None,
        )

        return self.repository.create(shipping_price)

    def update_shipping_price(
        self,
        shipping_price_id: int,
        data: ShippingPriceUpdate,
        user_id: int,
    ):
        shipping_price = self.get_shipping_price(shipping_price_id)

        update_data = data.model_dump(exclude_unset=True)

        update_data["updated_by"] = user_id
        update_data["updated_date"] = datetime.now()

        return self.repository.update(
            shipping_price,
            update_data,
        )

    def deactivate_shipping_price(
        self,
        shipping_price_id: int,
        user_id: int,
    ):
        shipping_price = self.get_shipping_price(shipping_price_id)

        shipping_price.updated_by = user_id
        shipping_price.updated_date = datetime.now()

        return self.repository.deactivate(shipping_price)