from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.shipping_price import ShippingPrice


class ShippingPriceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, shipping_price_id: int):
        stmt = select(ShippingPrice).where(
            ShippingPrice.shipping_price_id == shipping_price_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(ShippingPrice)

        if active_only:
            stmt = stmt.where(ShippingPrice.is_active == True)

        stmt = stmt.order_by(ShippingPrice.shipping_price_id.asc())

        return self.db.scalars(stmt).all()

    def create(self, shipping_price: ShippingPrice):
        self.db.add(shipping_price)
        self.db.commit()
        self.db.refresh(shipping_price)
        return shipping_price

    def update(
        self,
        shipping_price: ShippingPrice,
        update_data: dict,
    ):
        for field, value in update_data.items():
            setattr(shipping_price, field, value)

        self.db.commit()
        self.db.refresh(shipping_price)
        return shipping_price

    def deactivate(self, shipping_price: ShippingPrice):
        shipping_price.is_active = False
        self.db.commit()
        self.db.refresh(shipping_price)
        return shipping_price