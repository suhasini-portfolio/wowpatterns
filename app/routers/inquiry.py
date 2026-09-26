from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.inquiry_repository import InquiryRepository
from app.schemas.inquiry import (
    InquiryCreate,
    InquiryResponse,
    InquiryUpdate,
)
from app.services.inquiry_service import InquiryService


router = APIRouter(
    prefix="/inquiries",
    tags=["Inquiries"]
)


def get_inquiry_service(
    db: Session = Depends(get_db),
):
    repository = InquiryRepository(db)
    return InquiryService(repository)


@router.get(
    "/",
    response_model=list[InquiryResponse],
)
def get_all_inquiries(
    service: InquiryService = Depends(get_inquiry_service),
    current_customer=Depends(get_current_customer),
):
    return service.get_all_inquiries()


@router.get(
    "/{inquiry_id}",
    response_model=InquiryResponse,
)
def get_inquiry(
    inquiry_id: int,
    service: InquiryService = Depends(get_inquiry_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.get_inquiry(inquiry_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=InquiryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_inquiry(
    data: InquiryCreate,
    service: InquiryService = Depends(get_inquiry_service),
    current_customer=Depends(get_current_customer),
):
    return service.create_inquiry(
        data,
        current_customer.customer_id,
    )


@router.put(
    "/{inquiry_id}",
    response_model=InquiryResponse,
)
def update_inquiry(
    inquiry_id: int,
    data: InquiryUpdate,
    service: InquiryService = Depends(get_inquiry_service),
    current_customer=Depends(get_current_customer),
):
    try:
        return service.update_inquiry(
            inquiry_id,
            data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )