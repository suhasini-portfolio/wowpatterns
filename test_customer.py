from app.core.database import SessionLocal
from app.repositories.customer_repository import CustomerRepository

db = SessionLocal()

repo = CustomerRepository(db)

customer = repo.get_by_email("suha@igreensystems.com")

if customer:
    print(customer.full_name)
    print(customer.email)
else:
    print("Customer not found")

db.close()