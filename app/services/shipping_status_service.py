from app.models.shipping_status import ShippingStatus
from app.repositories.shipping_status_repository import ShippingStatusRepository
from app.schemas.shipping_status import (
    ShippingStatusCreate,
    ShippingStatusUpdate,
)


class ShippingStatusService:
    def __init__(self, repository: ShippingStatusRepository):
        self.repository = repository

    def get_shipping_status(self, shipping_status_id: int):
        shipping_status = self.repository.get_by_id(
            shipping_status_id
        )

        if not shipping_status:
            raise ValueError("Shipping status not found")

        return shipping_status

    def get_all_shipping_statuses(self):
        return self.repository.get_all()

    def create_shipping_status(
        self,
        data: ShippingStatusCreate
    ):
        shipping_status = ShippingStatus(
            shipping_status=data.shipping_status,
            priority=data.priority,
            status=data.status,
            email_subject=data.email_subject,
        )

        return self.repository.create(shipping_status)

    def update_shipping_status(
        self,
        shipping_status_id: int,
        data: ShippingStatusUpdate
    ):
        shipping_status = self.get_shipping_status(
            shipping_status_id
        )

        update_data = data.model_dump(exclude_unset=True)

        return self.repository.update(
            shipping_status,
            update_data
        )