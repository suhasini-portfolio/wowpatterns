from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.customer_download import CustomerDownload


class CustomerDownloadRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, download_id: int):
        stmt = select(CustomerDownload).where(
            CustomerDownload.download_id == download_id
        )
        return self.db.scalar(stmt)

    def get_all(self):
        stmt = select(CustomerDownload)
        return self.db.scalars(stmt).all()

    def get_by_customer_id(self, customer_id: int):
        stmt = select(CustomerDownload).where(
            CustomerDownload.customer_id == customer_id
        )
        return self.db.scalars(stmt).all()

    def get_by_customer_and_product(
        self,
        customer_id: int,
        product_id: int,
    ):
        stmt = select(CustomerDownload).where(
            CustomerDownload.customer_id == customer_id,
            CustomerDownload.product_id == product_id,
        )
        return self.db.scalar(stmt)

    def create(self, download: CustomerDownload):
        self.db.add(download)
        self.db.commit()
        self.db.refresh(download)
        return download