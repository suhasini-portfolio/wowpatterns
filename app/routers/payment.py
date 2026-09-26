from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.schemas.payment import PaymentCreate, PaymentResponse, PaymentVerify
from app.services.payment_service import PaymentService


router = APIRouter(
    prefix="/payments",
    tags=["Payments"],
)

service = PaymentService()


@router.post(
    "/create",
    response_model=PaymentResponse,
)
def create_payment(
    data: PaymentCreate,
    db: Session = Depends(get_db),
    current_customer=Depends(get_current_customer),
):
    razorpay_order = service.create_razorpay_order(
        db=db,
        order_id=data.order_id,
        customer_id=current_customer.customer_id,
    )

    if not razorpay_order:
        raise HTTPException(
            status_code=404,
            detail="Payable order not found",
        )

    return PaymentResponse(
        order_id=data.order_id,
        razorpay_order_id=razorpay_order["id"],
        amount=razorpay_order["amount"],
        currency=razorpay_order["currency"],
        status=razorpay_order["status"],
    )

@router.post("/verify")
def verify_payment(
    data: PaymentVerify,
    db: Session = Depends(get_db),
    current_customer=Depends(get_current_customer),
):
    try:
        order = service.get_payable_order(
            db=db,
            order_id=data.order_id,
            customer_id=current_customer.customer_id,
        )

        if not order:
            raise HTTPException(
                status_code=404,
                detail="Payable order not found",
            )

        service.verify_payment_signature(
            db=db,
            order_id=data.order_id,
            razorpay_order_id=data.razorpay_order_id,
            razorpay_payment_id=data.razorpay_payment_id,
            razorpay_signature=data.razorpay_signature,
        )

        return {
            "status": "paid",
            "message": "Payment verified and order updated successfully",
            "order_id": data.order_id,
            "razorpay_payment_id": data.razorpay_payment_id,
            "razor_status": "paid",
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Payment signature verification failed",
        )