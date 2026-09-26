from datetime import datetime

from app.models.order import Order
from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderCreate, OrderUpdate


class OrderService:
    def __init__(self, repository: OrderRepository):
        self.repository = repository

    def create_order(
        self,
        data: OrderCreate,
        customer_id: int,
    ):
        order = Order(
            customer_id=customer_id,
            order_status=data.order_status,
            total_price=data.total_price,
            discount=data.discount,
            gst_price=data.gst_price,
            grand_total=data.grand_total,
            shipping_full_name=data.shipping_full_name,
            shipping_mobile_country_id=data.shipping_mobile_country_id,
            shipping_mobile_country_code=data.shipping_mobile_country_code,
            shipping_mobile=data.shipping_mobile,
            shipping_country_id=data.shipping_country_id,
            shipping_state_id=data.shipping_state_id,
            shipping_city_id=data.shipping_city_id,
            shipping_zip_code=data.shipping_zip_code,
            shipping_email=data.shipping_email,
            shipping_landmark=data.shipping_landmark,
            shipping_address=data.shipping_address,
            order_type=data.order_type,
            created_date=datetime.now(),
        )

        return self.repository.create(order)

    def get_order(
        self,
        order_id: int,
        customer_id: int,
    ):
        order = self.repository.get_by_id(order_id)

        if not order or order.customer_id != customer_id:
            raise ValueError("Order not found")

        return order

    def get_customer_orders(self, customer_id: int):
        return self.repository.get_by_customer_id(customer_id)

    def update_order(
        self,
        order_id: int,
        data: OrderUpdate,
        customer_id: int,
    ):
        order = self.get_order(
            order_id=order_id,
            customer_id=customer_id,
        )

        update_data = data.model_dump(exclude_unset=True)

        order.updated_date = datetime.now()

        return self.repository.update(
            order,
            update_data,
        )

    def deactivate_order(
        self,
        order_id: int,
        customer_id: int,
    ):
        order = self.get_order(
            order_id=order_id,
            customer_id=customer_id,
        )

        order.updated_date = datetime.now()

        return self.repository.deactivate(order)