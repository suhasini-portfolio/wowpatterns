from datetime import datetime

from app.models.order_shipping_status import OrderShippingStatus
from app.repositories.order_shipping_status_repository import (
    OrderShippingStatusRepository,
)
from app.schemas.order_shipping_status import (
    OrderShippingStatusCreate,
    OrderShippingStatusUpdate,
)


class OrderShippingStatusService:
    def __init__(self, repository: OrderShippingStatusRepository):
        self.repository = repository

    def get_shipping_status(self, order_shipping_status_id: int):
        shipping_status = self.repository.get_by_id(order_shipping_status_id)

        if not shipping_status:
            raise ValueError("Order shipping status not found")

        return shipping_status

    def get_order_shipping_statuses(self, order_id: int):
        return self.repository.get_by_order_id(order_id)

    def get_order_item_shipping_statuses(self, order_item_id: int):
        return self.repository.get_by_order_item_id(order_item_id)

    def create_shipping_status(
        self,
        data: OrderShippingStatusCreate,
        user_id: int,
    ):
        now = datetime.now()

        shipping_status = OrderShippingStatus(
            order_id=data.order_id,
            order_item_id=data.order_item_id,
            shipping_status_id=data.shipping_status_id,
            messages=data.messages,
            created_by=user_id,
            updated_by=user_id,
            created_date=now,
        )

        return self.repository.create(shipping_status)

    def update_shipping_status(
        self,
        order_shipping_status_id: int,
        data: OrderShippingStatusUpdate,
        user_id: int,
    ):
        shipping_status = self.get_shipping_status(order_shipping_status_id)

        update_data = data.model_dump(exclude_unset=True)

        update_data["updated_by"] = user_id
        update_data["updated_date"] = datetime.now()

        return self.repository.update(
            shipping_status,
            update_data,
        )