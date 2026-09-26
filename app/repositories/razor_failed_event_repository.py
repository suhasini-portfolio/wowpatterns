from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.razor_failed_event import RazorFailedEvent


class RazorFailedEventRepository:

    def get_all(self, db: Session):
        statement = select(RazorFailedEvent).order_by(
            RazorFailedEvent.razor_failed_event_id.desc()
        )
        return db.scalars(statement).all()

    def get_by_id(self, db: Session, failed_event_id: int):
        return db.get(RazorFailedEvent, failed_event_id)

    def create(self, db: Session, failed_event: RazorFailedEvent):
        db.add(failed_event)
        db.commit()
        db.refresh(failed_event)
        return failed_event