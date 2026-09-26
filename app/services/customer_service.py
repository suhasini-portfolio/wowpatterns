"""
Customer Service

Contains business logic related to customers.
"""

from datetime import datetime
from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository
from app.schemas.customer import CustomerRegisterRequest, CustomerLoginRequest, CustomerProfileUpdateRequest
from app.core.security import hash_password, verify_password, create_access_token
from app.core.code_generator import generate_code


class CustomerService:

    def __init__(self, repository: CustomerRepository):
        self.repository = repository

    def register_customer(self, request: CustomerRegisterRequest):

        # Check whether email already exists
        existing_customer = self.repository.get_by_email(request.email)

        if existing_customer:
            raise ValueError("Email already exists")

        # Temporary customer code
        customer_code = generate_code(
            db=self.repository.db,
            model=Customer,
            code_column="customer_code",
            prefix="Cst-",
            digits=6
        )

        # Create customer object
        customer = Customer(
            customer_code=customer_code,
            full_name=request.full_name,
            email=request.email,
            password=hash_password(request.password),          # We'll hash it in the next step
            mobile_country_id=request.mobile_country_id,
            mobile_country_code=request.mobile_country_code,
            mobile=request.mobile,
            joining_date=datetime.now(),
            is_active=True
        )

        return self.repository.create(customer)

    def login(self, request: CustomerLoginRequest):
        # 1. Find customer by email
        customer = self.repository.get_by_email(request.email)

        if not customer:
            raise ValueError("Invalid email or password")

        # 2. Verify password
        if not verify_password(request.password, customer.password):
            raise ValueError("Invalid email or password")

        # 3. Check whether customer is active
        if not customer.is_active:
            raise ValueError("Customer account is inactive")

        # 4. Create JWT token
        access_token = create_access_token(
            data={"sub": str(customer.customer_id)}
        )

        # 5. Return token
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    def update_profile(self, customer: Customer, request: CustomerProfileUpdateRequest):
        return self.repository.update_profile(
            customer=customer,
            full_name=request.full_name,
            mobile_country_id=request.mobile_country_id,
            mobile_country_code=request.mobile_country_code,
            mobile=request.mobile,
        )