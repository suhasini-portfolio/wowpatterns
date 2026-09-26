from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order_item import OrderItem


class OrderItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, order_item_id: int):
        stmt = select(OrderItem).where(
            OrderItem.order_item_id == order_item_id
        )
        return self.db.scalar(stmt)

    def get_by_order_id(self, order_id: int):
        stmt = (
            select(OrderItem)
            .where(OrderItem.order_id == order_id)
            .order_by(OrderItem.order_item_id.desc())
        )
        return self.db.scalars(stmt).all()

    def create(self, order_item: OrderItem):
        self.db.add(order_item)
        self.db.commit()
        self.db.refresh(order_item)
        return order_item

    def update(self, order_item: OrderItem, update_data: dict):
        for field, value in update_data.items():
            setattr(order_item, field, value)

        self.db.commit()
        self.db.refresh(order_item)
        return order_item

    def deactivate(self, order_item: OrderItem):
        order_item.is_active = False

        self.db.commit()
        self.db.refresh(order_item)
        return order_item