from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.razor_failed_event import (
    RazorFailedEventCreate,
    RazorFailedEventResponse,
)
from app.services.razor_failed_event_service import RazorFailedEventService


router = APIRouter(
    prefix="/razor_failed_events",
    tags=["Razor Failed Events"],
)

service = RazorFailedEventService()


@router.get(
    "/",
    response_model=list[RazorFailedEventResponse],
)
def get_failed_events(
    db: Session = Depends(get_db),
):
    return service.get_all(db)


@router.get(
    "/{failed_event_id}",
    response_model=RazorFailedEventResponse,
)
def get_failed_event(
    failed_event_id: int,
    db: Session = Depends(get_db),
):
    failed_event = service.get_by_id(db, failed_event_id)

    if not failed_event:
        raise HTTPException(
            status_code=404,
            detail="Razor failed event not found",
        )

    return failed_event


@router.post(
    "/",
    response_model=RazorFailedEventResponse,
    status_code=201,
)
def create_failed_event(
    data: RazorFailedEventCreate,
    db: Session = Depends(get_db),
):
    return service.create(db, data)