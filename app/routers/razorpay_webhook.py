from fastapi import APIRouter, Depends, HTTPException, Request, Header, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.razorpay_webhook_repository import (
    RazorpayWebhookRepository,
)
from app.schemas.razorpay_webhook import (
    RazorpayWebhookCreate,
    RazorpayWebhookResponse,
    RazorpayWebhookUpdate,
)
from app.services.razorpay_webhook_service import (
    RazorpayWebhookService,
)
from app.schemas.razor_failed_event import RazorFailedEventCreate
from app.services.razor_failed_event_service import RazorFailedEventService
from app.core.razorpay import verify_webhook_signature
import json

router = APIRouter(
    prefix="/razorpay_webhooks",
    tags=["Razorpay Webhooks"],
)


def get_razorpay_webhook_service(
    db: Session = Depends(get_db),
):
    repository = RazorpayWebhookRepository(db)
    return RazorpayWebhookService(repository)


@router.get(
    "/",
    response_model=list[RazorpayWebhookResponse],
)
def get_all_webhooks(
    service: RazorpayWebhookService = Depends(
        get_razorpay_webhook_service
    ),
    current_customer=Depends(get_current_customer),
):
    return service.get_all_webhooks()


@router.get(
    "/{webhook_id}",
    response_model=RazorpayWebhookResponse,
)
def get_webhook(
    webhook_id: int,
    service: RazorpayWebhookService = Depends(
        get_razorpay_webhook_service
    ),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.get_webhook(webhook_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=RazorpayWebhookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_webhook(
    data: RazorpayWebhookCreate,
    service: RazorpayWebhookService = Depends(
        get_razorpay_webhook_service
    ),
    current_customer=Depends(get_current_customer),
):
    return service.create_webhook(data)


@router.put(
    "/{webhook_id}",
    response_model=RazorpayWebhookResponse,
)
def update_webhook(
    webhook_id: int,
    data: RazorpayWebhookUpdate,
    service: RazorpayWebhookService = Depends(
        get_razorpay_webhook_service
    ),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.update_webhook(
            webhook_id,
            data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )

@router.post("/receive")
async def receive_razorpay_webhook(
    request: Request,
    x_razorpay_signature: str | None = Header(
        default=None,
        alias="X-Razorpay-Signature",
    ),
    db: Session = Depends(get_db),
):
    payload = await request.body()

    if not x_razorpay_signature:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Missing Razorpay webhook signature",
        )

    try:
        verify_webhook_signature(
            payload=payload,
            signature=x_razorpay_signature,
        )

        webhook_data = json.loads(
            payload.decode("utf-8")
        )

        service = get_razorpay_webhook_service(db)

        webhook = service.process_webhook_event(
            db=db,
            payload=webhook_data,
            webhook_signature=x_razorpay_signature,
        )

        return {
            "status": "received",
            "message": "Webhook verified and saved successfully",
            "webhook_id": webhook.razorpay_webhook_id,
            "event": webhook.webhook_event,
            "payment_id": webhook.razorpay_payment_id,
        }

    except HTTPException:
        raise

    except Exception as exc:
        failed_event_service = RazorFailedEventService()

        failed_event_service.create(
            db=db,
            data=RazorFailedEventCreate(
                raw_data=payload.decode("utf-8"),
                error_message=str(exc),
            ),
        )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Webhook processing failed",
        )