from datetime import datetime

from app.models.order_item import OrderItem
from app.repositories.order_item_repository import OrderItemRepository
from app.repositories.order_repository import OrderRepository
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate


class OrderItemService:
    def __init__(
        self,
        repository: OrderItemRepository,
        order_repository: OrderRepository
    ):
        self.repository = repository
        self.order_repository = order_repository

    def _get_customer_order(self, order_id: int, customer_id: int):
        order = self.order_repository.get_by_id(order_id)

        if not order or order.customer_id != customer_id:
            raise ValueError("Order not found")

        return order

    def get_order_items(self, order_id: int, customer_id: int):
        self._get_customer_order(order_id, customer_id)

        return self.repository.get_by_order_id(order_id)

    def get_order_item(self, order_item_id: int, customer_id: int):
        order_item = self.repository.get_by_id(order_item_id)

        if not order_item:
            raise ValueError("Order item not found")

        self._get_customer_order(order_item.order_id, customer_id)

        return order_item

    def create_order_item(
        self,
        data: OrderItemCreate,
        customer_id: int
    ):
        self._get_customer_order(data.order_id, customer_id)

        order_item = OrderItem(
            order_id=data.order_id,
            product_id=data.product_id,
            product_type=data.product_type,
            fabric_product_id=data.fabric_product_id,
            quantity=data.quantity,
            price=data.price,
            print_quality=data.print_quality,
            artist_commission_percentage=data.artist_commission_percentage,
            artist_commission=data.artist_commission,
            shipping_status_id=data.shipping_status_id,
            created_date=datetime.now(),
        )

        return self.repository.create(order_item)

    def update_order_item(
        self,
        order_item_id: int,
        data: OrderItemUpdate,
        customer_id: int
    ):
        order_item = self.get_order_item(
            order_item_id=order_item_id,
            customer_id=customer_id
        )

        update_data = data.model_dump(exclude_unset=True)

        order_item.updated_date = datetime.now()

        return self.repository.update(
            order_item,
            update_data
        )

    def deactivate_order_item(
        self,
        order_item_id: int,
        customer_id: int
    ):
        order_item = self.get_order_item(
            order_item_id=order_item_id,
            customer_id=customer_id
        )

        order_item.updated_date = datetime.now()

        return self.repository.deactivate(order_item)