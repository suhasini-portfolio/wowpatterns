from datetime import datetime

from app.models.shopping_bag import ShoppingBag
from app.repositories.shopping_bag_repository import ShoppingBagRepository
from app.schemas.shopping_bag import (
    ShoppingBagCreate,
    ShoppingBagUpdate,
)


class ShoppingBagService:
    def __init__(self, repository: ShoppingBagRepository):
        self.repository = repository

    def add_to_bag(
        self,
        data: ShoppingBagCreate,
        user_id: int,
    ):
        existing_item = self.repository.get_existing_item(
            user_id=user_id,
            product_id=data.product_id,
            product_type=data.product_type,
            fabric_product_id=data.fabric_product_id,
            print_quality=data.print_quality,
        )

        if existing_item:
            existing_item.quantity += data.quantity
            existing_item.user_browser = data.user_browser
            existing_item.updated_date = datetime.now()

            self.repository.db.commit()
            self.repository.db.refresh(existing_item)

            return existing_item

        shopping_bag = ShoppingBag(
            product_id=data.product_id,
            product_type=data.product_type,
            fabric_product_id=data.fabric_product_id,
            quantity=data.quantity,
            print_quality=data.print_quality,
            user_id=user_id,
            user_browser=data.user_browser,
            created_date=datetime.now(),
        )

        return self.repository.create(shopping_bag)

    def get_bag_item(
        self,
        shopping_bag_id: int,
        user_id: int,
    ):
        item = self.repository.get_by_id(shopping_bag_id)

        if not item or item.user_id != user_id:
            raise ValueError("Shopping bag item not found")

        return item

    def get_user_bag(self, user_id: int):
        return self.repository.get_by_user_id(user_id)

    def update_bag_item(
        self,
        shopping_bag_id: int,
        data: ShoppingBagUpdate,
        user_id: int,
    ):
        item = self.get_bag_item(
            shopping_bag_id=shopping_bag_id,
            user_id=user_id,
        )

        update_data = data.model_dump(exclude_unset=True)

        item.updated_date = datetime.now()

        return self.repository.update(
            item,
            update_data,
        )

    def remove_from_bag(
        self,
        shopping_bag_id: int,
        user_id: int,
    ):
        item = self.get_bag_item(
            shopping_bag_id=shopping_bag_id,
            user_id=user_id,
        )

        self.repository.delete(item)

        return True