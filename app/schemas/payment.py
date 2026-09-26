from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: int


class PaymentResponse(BaseModel):
    order_id: int
    razorpay_order_id: str
    amount: int
    currency: str
    status: str

class PaymentVerify(BaseModel):
    order_id: int
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str