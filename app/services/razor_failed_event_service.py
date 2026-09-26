from datetime import datetime

from sqlalchemy.orm import Session

from app.models.razor_failed_event import RazorFailedEvent
from app.repositories.razor_failed_event_repository import (
    RazorFailedEventRepository,
)
from app.schemas.razor_failed_event import RazorFailedEventCreate


class RazorFailedEventService:

    def __init__(self):
        self.repository = RazorFailedEventRepository()

    def get_all(self, db: Session):
        return self.repository.get_all(db)

    def get_by_id(self, db: Session, failed_event_id: int):
        return self.repository.get_by_id(db, failed_event_id)

    def create(
        self,
        db: Session,
        data: RazorFailedEventCreate,
    ):
        failed_event = RazorFailedEvent(
            raw_data=data.raw_data,
            error_message=data.error_message,
            created_date=datetime.now(),
        )

        return self.repository.create(db, failed_event)