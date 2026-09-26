from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.shipping_status import ShippingStatus


class ShippingStatusRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, shipping_status_id: int):
        stmt = select(ShippingStatus).where(
            ShippingStatus.shipping_status_id == shipping_status_id
        )
        return self.db.scalar(stmt)

    def get_all(self):
        stmt = (
            select(ShippingStatus)
            .order_by(ShippingStatus.priority.asc())
        )
        return self.db.scalars(stmt).all()

    def create(self, shipping_status: ShippingStatus):
        self.db.add(shipping_status)
        self.db.commit()
        self.db.refresh(shipping_status)
        return shipping_status

    def update(
        self,
        shipping_status: ShippingStatus,
        update_data: dict
    ):
        for field, value in update_data.items():
            setattr(shipping_status, field, value)

        self.db.commit()
        self.db.refresh(shipping_status)
        return shipping_status