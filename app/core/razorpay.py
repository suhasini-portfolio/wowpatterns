import razorpay

from app.core.config import settings


razorpay_client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET,
    )
)


def verify_webhook_signature(
    payload: bytes,
    signature: str,
):
    razorpay_client.utility.verify_webhook_signature(
        payload.decode("utf-8"),
        signature,
        settings.RAZORPAY_KEY_SECRET,
    )

    return True