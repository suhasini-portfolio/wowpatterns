from datetime import datetime

from app.models.inquiry import Inquiry
from app.repositories.inquiry_repository import InquiryRepository
from app.schemas.inquiry import InquiryCreate, InquiryUpdate


class InquiryService:
    def __init__(self, repository: InquiryRepository):
        self.repository = repository

    def get_inquiry(self, inquiry_id: int):
        inquiry = self.repository.get_by_id(inquiry_id)

        if not inquiry:
            raise ValueError("Inquiry not found")

        return inquiry

    def get_all_inquiries(self):
        return self.repository.get_all()

    def create_inquiry(self, data: InquiryCreate, user_id: int):
        inquiry = Inquiry(
            name=data.name,
            company=data.company,
            country=data.country,
            email=data.email,
            mobile=data.mobile,
            mobile_country_id=data.mobile_country_id,
            mobile_country_code=data.mobile_country_code,
            product_id=data.product_id,
            inquiry_type=data.inquiry_type,
            message=data.message,
            order_id=data.order_id,
            design=data.design,
            note=data.note,
            created_by=user_id,
            created_date=datetime.now(),
        )

        return self.repository.create(inquiry)

    def update_inquiry(
        self,
        inquiry_id: int,
        data: InquiryUpdate,
    ):
        inquiry = self.get_inquiry(inquiry_id)

        update_data = data.model_dump(exclude_unset=True)

        return self.repository.update(
            inquiry,
            update_data
        )