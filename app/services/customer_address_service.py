from datetime import datetime

from app.models.customer_address import CustomerAddress
from app.repositories.customer_address_repository import CustomerAddressRepository
from app.schemas.customer_address import (
    CustomerAddressCreate,
    CustomerAddressUpdate,
)


class CustomerAddressService:
    def __init__(self, repository: CustomerAddressRepository):
        self.repository = repository

    def create_address(
        self,
        data: CustomerAddressCreate,
        customer_id: int,
    ):
        address_data = data.model_dump()

        # Customer ID comes from the authenticated customer,
        # not from the request body.
        address_data["customer_id"] = customer_id

        address = CustomerAddress(
            **address_data,
            created_date=datetime.now(),
        )

        return self.repository.create(address)

    def get_address(self, customer_address_id: int):
        address = self.repository.get_by_id(customer_address_id)

        if not address:
            raise ValueError("No customer address exists")

        return address

    def get_addresses(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def get_customer_addresses(
        self,
        customer_id: int,
        active_only: bool = True,
    ):
        return self.repository.get_by_customer_id(
            customer_id,
            active_only,
        )

    def update_address(
        self,
        customer_address_id: int,
        data: CustomerAddressUpdate,
    ):
        address = self.repository.get_by_id(customer_address_id)

        if not address:
            raise ValueError("No customer address exists")

        address_data = data.model_dump(exclude_unset=True)

        # CustomerID should not be changed through update.
        address_data.pop("customer_id", None)

        address.updated_date = datetime.now()

        return self.repository.update(
            address,
            address_data,
        )

    def deactivate_address(
        self,
        customer_address_id: int,
    ):
        address = self.repository.get_by_id(customer_address_id)

        if not address:
            raise ValueError("No customer address exists")

        address.updated_date = datetime.now()

        return self.repository.deactivate(address)