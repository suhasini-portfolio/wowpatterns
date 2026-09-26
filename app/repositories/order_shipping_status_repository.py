from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order_shipping_status import OrderShippingStatus


class OrderShippingStatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, order_shipping_status_id: int):
        stmt = select(OrderShippingStatus).where(
            OrderShippingStatus.order_shipping_status_id
            == order_shipping_status_id
        )
        return self.db.scalar(stmt)

    def get_by_order_id(self, order_id: int):
        stmt = (
            select(OrderShippingStatus)
            .where(OrderShippingStatus.order_id == order_id)
            .order_by(OrderShippingStatus.created_date.asc())
        )
        return self.db.scalars(stmt).all()

    def get_by_order_item_id(self, order_item_id: int):
        stmt = (
            select(OrderShippingStatus)
            .where(OrderShippingStatus.order_item_id == order_item_id)
            .order_by(OrderShippingStatus.created_date.asc())
        )
        return self.db.scalars(stmt).all()

    def create(self, shipping_status: OrderShippingStatus):
        self.db.add(shipping_status)
        self.db.commit()
        self.db.refresh(shipping_status)
        return shipping_status

    def update(
        self,
        shipping_status: OrderShippingStatus,
        update_data: dict,
    ):
        for field, value in update_data.items():
            setattr(shipping_status, field, value)

        self.db.commit()
        self.db.refresh(shipping_status)
        return shipping_status