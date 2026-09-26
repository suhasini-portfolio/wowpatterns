from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.models.customer import Customer
from app.repositories.customer_download_repository import CustomerDownloadRepository
from app.schemas.customer_download import (
    CustomerDownloadCreate,
    CustomerDownloadResponse,
)
from app.services.customer_download_service import CustomerDownloadService


router = APIRouter(
    prefix="/customer_downloads",
    tags=["Customer Downloads"],
)


def get_customer_download_service(
    db: Session = Depends(get_db),
):
    repository = CustomerDownloadRepository(db)
    return CustomerDownloadService(repository)


@router.get(
    "/",
    response_model=list[CustomerDownloadResponse],
)
def get_downloads(
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerDownloadService = Depends(
        get_customer_download_service
    ),
):
    return service.get_customer_downloads(
        current_customer.customer_id
    )


@router.get(
    "/{download_id}",
    response_model=CustomerDownloadResponse,
)
def get_download(
    download_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerDownloadService = Depends(
        get_customer_download_service
    ),
):
    try:
        download = service.get_download(download_id)

        if download.customer_id != current_customer.customer_id:
            raise HTTPException(
                status_code=403,
                detail="You can only access your own downloads",
            )

        return download

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.get(
    "/product/{product_id}",
    response_model=CustomerDownloadResponse | None,
)
def get_product_download(
    product_id: int,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerDownloadService = Depends(
        get_customer_download_service
    ),
):
    return service.repository.get_by_customer_and_product(
        customer_id=current_customer.customer_id,
        product_id=product_id,
    )


@router.post(
    "/",
    response_model=CustomerDownloadResponse,
)
def record_download(
    data: CustomerDownloadCreate,
    current_customer: Customer = Depends(get_current_customer),
    service: CustomerDownloadService = Depends(
        get_customer_download_service
    ),
):
    return service.record_download(
        data,
        customer_id=current_customer.customer_id,
    )