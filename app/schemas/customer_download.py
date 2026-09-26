from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CustomerDownloadCreate(BaseModel):
    customer_id: int
    product_id: int
    download_count: int
    last_download: datetime


class CustomerDownloadResponse(BaseModel):
    download_id: int
    customer_id: int
    product_id: int
    download_count: int
    last_download: datetime

    model_config = ConfigDict(from_attributes=True)