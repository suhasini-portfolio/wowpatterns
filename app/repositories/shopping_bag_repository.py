from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.shopping_bag import ShoppingBag


class ShoppingBagRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, shopping_bag_id: int):
        stmt = select(ShoppingBag).where(
            ShoppingBag.shopping_bag_id == shopping_bag_id
        )
        return self.db.scalar(stmt)

    def get_by_user_id(self, user_id: int):
        stmt = select(ShoppingBag).where(
            ShoppingBag.user_id == user_id
        )
        return self.db.scalars(stmt).all()

    def get_existing_item(
        self,
        user_id: int,
        product_id: int,
        product_type: str,
        fabric_product_id: int | None,
        print_quality: str | None,
    ):
        stmt = select(ShoppingBag).where(
            ShoppingBag.user_id == user_id,
            ShoppingBag.product_id == product_id,
            ShoppingBag.product_type == product_type,
            ShoppingBag.fabric_product_id == fabric_product_id,
            ShoppingBag.print_quality == print_quality,
        )
        return self.db.scalar(stmt)

    def create(self, shopping_bag: ShoppingBag):
        self.db.add(shopping_bag)
        self.db.commit()
        self.db.refresh(shopping_bag)
        return shopping_bag

    def update(self, shopping_bag: ShoppingBag, update_data: dict):
        for field, value in update_data.items():
            setattr(shopping_bag, field, value)

        self.db.commit()
        self.db.refresh(shopping_bag)
        return shopping_bag

    def delete(self, shopping_bag: ShoppingBag):
        self.db.delete(shopping_bag)
        self.db.commit()