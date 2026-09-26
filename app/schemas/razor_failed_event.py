from datetime import datetime

from pydantic import BaseModel


class RazorFailedEventCreate(BaseModel):
    raw_data: str | None = None
    error_message: str | None = None


class RazorFailedEventResponse(BaseModel):
    razor_failed_event_id: int
    raw_data: str | None
    error_message: str | None
    created_date: datetime | None

    model_config = {
        "from_attributes": True
    }