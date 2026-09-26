from datetime import datetime

from app.models.razorpay_webhook import RazorpayWebhook
from app.repositories.order_repository import OrderRepository
from app.repositories.razorpay_webhook_repository import (
    RazorpayWebhookRepository,
)
from app.schemas.razorpay_webhook import (
    RazorpayWebhookCreate,
    RazorpayWebhookUpdate,
)


class RazorpayWebhookService:
    def __init__(self, repository: RazorpayWebhookRepository):
        self.repository = repository

    def get_webhook(self, webhook_id: int):
        webhook = self.repository.get_by_id(webhook_id)

        if not webhook:
            raise ValueError("Razorpay webhook not found")

        return webhook

    def get_all_webhooks(self):
        return self.repository.get_all()

    def create_webhook(self, data: RazorpayWebhookCreate):
        webhook = RazorpayWebhook(
            created_date=data.created_date or datetime.now(),
            status=data.status,
            webhook_signature=data.webhook_signature,
            webhook_event=data.webhook_event,
            razorpay_payment_id=data.razorpay_payment_id,
            amount=data.amount,
            currency=data.currency,
            base_amount=data.base_amount,
            event_status=data.event_status,
            order_id=data.order_id,
            ck_order_id=data.ck_order_id,
            is_captured=data.is_captured,
            description=data.description,
            event_created_at=data.event_created_at,
            amount_refunded=data.amount_refunded,
            refund_status=data.refund_status,
        )

        return self.repository.create(webhook)

    def process_webhook_event(
        self,
        db,
        payload: dict,
        webhook_signature: str,
    ):
        event = payload.get("event")

        payment_payload = (
            payload.get("payload", {})
            .get("payment", {})
            .get("entity", {})
        )

        payment_id = payment_payload.get("id")
        amount = payment_payload.get("amount", 0)
        currency = payment_payload.get("currency", "INR")
        payment_status = payment_payload.get("status")

        order_id = payment_payload.get("order_id")

        order_repository = OrderRepository(db)

        webhook_data = RazorpayWebhookCreate(
            status=True,
            webhook_signature=webhook_signature,
            webhook_event=event,
            razorpay_payment_id=payment_id,
            amount=amount / 100,
            currency=currency,
            base_amount=amount,
            event_status=payment_status,
            order_id=str(order_id) if order_id else None,
            is_captured=(event == "payment.captured"),
            description=payment_payload.get("description"),
        )

        if event == "payment.captured" and order_id:
            order = order_repository.get_by_id(int(order_id))

            if order:
                order_repository.update(
                    order,
                    {
                        "razorpay_payment_id": payment_id,
                        "razor_status": "paid",
                        "razor_updated_date": datetime.now(),
                    },
                )

        return self.create_webhook(webhook_data)

    def update_webhook(
        self,
        webhook_id: int,
        data: RazorpayWebhookUpdate,
    ):
        webhook = self.get_webhook(webhook_id)

        update_data = data.model_dump(exclude_unset=True)

        return self.repository.update(
            webhook,
            update_data,
        )