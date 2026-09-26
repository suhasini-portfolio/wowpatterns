from datetime import datetime

from app.models.customer_download import CustomerDownload
from app.repositories.customer_download_repository import CustomerDownloadRepository
from app.schemas.customer_download import CustomerDownloadCreate


class CustomerDownloadService:
    def __init__(self, repository: CustomerDownloadRepository):
        self.repository = repository

    def record_download(
        self,
        data: CustomerDownloadCreate,
        customer_id: int,
    ):
        existing_download = self.repository.get_by_customer_and_product(
            customer_id=customer_id,
            product_id=data.product_id,
        )

        if existing_download:
            existing_download.download_count += 1
            existing_download.last_download = datetime.now()

            self.repository.db.commit()
            self.repository.db.refresh(existing_download)

            return existing_download

        download = CustomerDownload(
            customer_id=customer_id,
            product_id=data.product_id,
            download_count=1,
            last_download=datetime.now(),
        )

        return self.repository.create(download)

    def get_download(self, download_id: int):
        download = self.repository.get_by_id(download_id)

        if not download:
            raise ValueError("No customer download exists")

        return download

    def get_downloads(self):
        return self.repository.get_all()

    def get_customer_downloads(self, customer_id: int):
        return self.repository.get_by_customer_id(customer_id)