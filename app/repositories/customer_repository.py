"""
Customer Repository

Contains all database operations related to customers.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from datetime import datetime

from app.models.customer import Customer


class CustomerRepository:

    def __init__(self, db:Session):
        self.db = db

    def get_by_email(self, email: str) -> Customer | None:
        stmt = select(Customer).where(Customer.email == email)
        return self.db.scalar(stmt)
    
    def create(self, customer: Customer) -> Customer:
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer

    def get_by_id(self, customer_id: int) -> Customer | None:
        stmt = select(Customer).where(
            Customer.customer_id == customer_id
        )

        return self.db.scalar(stmt)

    def update_profile(self, customer: Customer, full_name: str, mobile_country_id: int | None, mobile_country_code: str | None, mobile: str | None) -> Customer:

        customer.full_name = full_name
        customer.mobile_country_id = mobile_country_id
        customer.mobile_country_code = mobile_country_code
        customer.mobile = mobile
        customer.updated_date = datetime.now()

        self.db.commit()
        self.db.refresh(customer)

        return customer