from datetime import datetime
from sqlalchemy.orm import Session

from app.core.razorpay import razorpay_client
from app.repositories.order_repository import OrderRepository


class PaymentService:

    def get_payable_order(
        self,
        db: Session,
        order_id: int,
        customer_id: int,
    ):
        order_repository = OrderRepository(db)

        order = order_repository.get_by_id(order_id)

        if not order:
            return None

        if order.customer_id != customer_id:
            return None

        if not order.is_active:
            return None

        return order

    def create_razorpay_order(
        self,
        db: Session,
        order_id: int,
        customer_id: int,
    ):
        order = self.get_payable_order(
            db=db,
            order_id=order_id,
            customer_id=customer_id,
        )

        if not order:
            return None

        amount_in_paise = int(round(float(order.grand_total) * 100))

        razorpay_order = razorpay_client.order.create(
            {
                "amount": amount_in_paise,
                "currency": "INR",
                "receipt": f"order_{order.order_id}",
            }
        )

        return razorpay_order

    def verify_payment_signature(
        self,
        db: Session,
        order_id: int,
        razorpay_order_id: str,
        razorpay_payment_id: str,
        razorpay_signature: str,
    ):
        order_repository = OrderRepository(db)

        order = order_repository.get_by_id(order_id)

        if not order:
            return None

        razorpay_client.utility.verify_payment_signature(
            {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature,
            }
        )

        updated_order = order_repository.update(
            order,
            {
                "razorpay_payment_id": razorpay_payment_id,
                "razor_status": "paid",
                "razor_updated_date": datetime.now(),
            },
        )

        return updated_order