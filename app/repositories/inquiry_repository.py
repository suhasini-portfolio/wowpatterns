from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.inquiry import Inquiry


class InquiryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, inquiry_id: int):
        stmt = select(Inquiry).where(
            Inquiry.inquiry_id == inquiry_id
        )
        return self.db.scalar(stmt)

    def get_all(self):
        stmt = select(Inquiry).order_by(
            Inquiry.inquiry_id.desc()
        )
        return self.db.scalars(stmt).all()

    def create(self, inquiry: Inquiry):
        self.db.add(inquiry)
        self.db.commit()
        self.db.refresh(inquiry)
        return inquiry

    def update(self, inquiry: Inquiry, update_data: dict):
        for field, value in update_data.items():
            setattr(inquiry, field, value)

        self.db.commit()
        self.db.refresh(inquiry)

        return inquiry