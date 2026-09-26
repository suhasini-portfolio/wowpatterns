from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_customer
from app.repositories.shopping_bag_repository import ShoppingBagRepository
from app.schemas.shopping_bag import (
    ShoppingBagCreate,
    ShoppingBagResponse,
    ShoppingBagUpdate,
)
from app.services.shopping_bag_service import ShoppingBagService


router = APIRouter(
    prefix="/shopping_bag",
    tags=["Shopping Bag"],
)


def get_service(db: Session = Depends(get_db)):
    repository = ShoppingBagRepository(db)
    return ShoppingBagService(repository)


@router.get(
    "/",
    response_model=list[ShoppingBagResponse],
)
def get_my_bag(
    current_customer=Depends(get_current_customer),
    service: ShoppingBagService = Depends(get_service),
):
    return service.get_user_bag(current_customer.customer_id)


@router.get(
    "/{shopping_bag_id}",
    response_model=ShoppingBagResponse,
)
def get_bag_item(
    shopping_bag_id: int,
    current_customer=Depends(get_current_customer),
    service: ShoppingBagService = Depends(get_service),
):
    try:
        return service.get_bag_item(
            shopping_bag_id=shopping_bag_id,
            user_id=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=ShoppingBagResponse,
    status_code=201,
)
def add_to_bag(
    data: ShoppingBagCreate,
    current_customer=Depends(get_current_customer),
    service: ShoppingBagService = Depends(get_service),
):
    return service.add_to_bag(
        data=data,
        user_id=current_customer.customer_id,
    )


@router.put(
    "/{shopping_bag_id}",
    response_model=ShoppingBagResponse,
)
def update_bag_item(
    shopping_bag_id: int,
    data: ShoppingBagUpdate,
    current_customer=Depends(get_current_customer),
    service: ShoppingBagService = Depends(get_service),
):
    try:
        return service.update_bag_item(
            shopping_bag_id=shopping_bag_id,
            data=data,
            user_id=current_customer.customer_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{shopping_bag_id}",
)
def remove_from_bag(
    shopping_bag_id: int,
    current_customer=Depends(get_current_customer),
    service: ShoppingBagService = Depends(get_service),
):
    try:
        service.remove_from_bag(
            shopping_bag_id=shopping_bag_id,
            user_id=current_customer.customer_id,
        )

        return {
            "message": "Shopping bag item removed successfully"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )