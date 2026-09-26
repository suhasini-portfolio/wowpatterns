from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer_address import CustomerAddress


class CustomerAddressRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, customer_address_id: int):
        stmt = select(CustomerAddress).where(
            CustomerAddress.customer_address_id == customer_address_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(CustomerAddress)

        if active_only:
            stmt = stmt.where(
                CustomerAddress.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def get_by_customer_id(
        self,
        customer_id: int,
        active_only: bool = True,
    ):
        stmt = select(CustomerAddress).where(
            CustomerAddress.customer_id == customer_id
        )

        if active_only:
            stmt = stmt.where(
                CustomerAddress.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def create(self, address: CustomerAddress):
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address

    def update(self, address: CustomerAddress, update_data: dict):
        for field, value in update_data.items():
            setattr(address, field, value)

        self.db.commit()
        self.db.refresh(address)
        return address

    def deactivate(self, address: CustomerAddress):
        address.is_active = False

        self.db.commit()
        self.db.refresh(address)
        return address