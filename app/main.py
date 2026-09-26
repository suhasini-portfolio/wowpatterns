from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from app.core.config import settings

from app.routers.customer import router as customer_router
from app.routers.products import router as products_router
from app.routers.product_category import router as product_category_router
from app.routers.product_category_type import (
    router as product_category_type_router
)
from app.routers.product_specification import (
    router as product_specification_router
)
from app.routers.product_image import (
    router as product_image_router
)
from app.routers.customer_address import router as customer_address_router
from app.routers.customer_download import router as customer_download_router
from app.routers.design_filetype import router as design_filetype_router
from app.routers.product_design_specification import (
    router as product_design_specification_router,
)
from app.routers import shopping_bag
from app.routers import order
from app.routers import order_item
from app.routers import shipping_status
from app.routers import order_shipping_status
from app.routers import shipping_price
from app.routers import inquiry
from app.routers import razorpay_webhook
from app.routers import razor_failed_event
from app.routers import payment

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(customer_router)
app.include_router(products_router)
app.include_router(product_category_router)
app.include_router(product_category_type_router)
app.include_router(product_specification_router)
app.include_router(product_image_router)
app.include_router(customer_address_router)
app.include_router(customer_download_router)
app.include_router(design_filetype_router)
app.include_router(product_design_specification_router)
app.include_router(shopping_bag.router)
app.include_router(order.router)
app.include_router(order_item.router)
app.include_router(shipping_status.router)
app.include_router(order_shipping_status.router)
app.include_router(shipping_price.router)
app.include_router(inquiry.router)
app.include_router(razorpay_webhook.router)
app.include_router(razor_failed_event.router)
app.include_router(payment.router)

@app.get("/")
def root():
    return {"message": "WowPatterns API is running"}


#print(settings.DB_NAME)
#print(settings.DB_HOST)
#print(settings.DATABASE_URL)