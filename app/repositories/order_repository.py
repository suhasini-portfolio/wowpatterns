from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Order


class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, order_id: int):
        stmt = select(Order).where(
            Order.order_id == order_id
        )
        return self.db.scalar(stmt)

    def get_by_customer_id(self, customer_id: int):
        stmt = (
            select(Order)
            .where(Order.customer_id == customer_id)
            .order_by(Order.order_id.desc())
        )
        return self.db.scalars(stmt).all()

    def get_all(self, active_only: bool = True):
        stmt = select(Order)

        if active_only:
            stmt = stmt.where(Order.is_active == True)

        stmt = stmt.order_by(Order.order_id.desc())

        return self.db.scalars(stmt).all()

    def create(self, order: Order):
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def update(self, order: Order, update_data: dict):
        for field, value in update_data.items():
            setattr(order, field, value)

        self.db.commit()
        self.db.refresh(order)

        return order

    def deactivate(self, order: Order):
        order.is_active = False

        self.db.commit()
        self.db.refresh(order)

        return order