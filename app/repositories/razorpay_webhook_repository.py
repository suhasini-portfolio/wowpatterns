from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.razorpay_webhook import RazorpayWebhook


class RazorpayWebhookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, razorpay_webhook_id: int):
        stmt = select(RazorpayWebhook).where(
            RazorpayWebhook.razorpay_webhook_id == razorpay_webhook_id
        )
        return self.db.scalar(stmt)

    def get_all(self):
        stmt = select(RazorpayWebhook).order_by(
            RazorpayWebhook.razorpay_webhook_id.desc()
        )
        return self.db.scalars(stmt).all()

    def create(self, webhook: RazorpayWebhook):
        self.db.add(webhook)
        self.db.commit()
        self.db.refresh(webhook)
        return webhook

    def update(self, webhook: RazorpayWebhook, update_data: dict):
        for field, value in update_data.items():
            setattr(webhook, field, value)

        self.db.commit()
        self.db.refresh(webhook)

        return webhook