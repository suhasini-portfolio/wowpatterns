from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.design_filetype_repository import DesignFileTypeRepository
from app.schemas.design_filetype import (
    DesignFileTypeCreate,
    DesignFileTypeResponse,
    DesignFileTypeUpdate,
)
from app.services.design_filetype_service import DesignFileTypeService


router = APIRouter(
    prefix="/design_filetypes",
    tags=["Design File Types"],
)


def get_design_filetype_service(
    db: Session = Depends(get_db),
):
    repository = DesignFileTypeRepository(db)
    return DesignFileTypeService(repository)


@router.get(
    "/",
    response_model=list[DesignFileTypeResponse],
)
def get_file_types(
    service: DesignFileTypeService = Depends(
        get_design_filetype_service
    ),
):
    return service.get_file_types()


@router.get(
    "/{design_file_type_id}",
    response_model=DesignFileTypeResponse,
)
def get_file_type(
    design_file_type_id: int,
    service: DesignFileTypeService = Depends(
        get_design_filetype_service
    ),
):
    try:
        return service.get_file_type(design_file_type_id)
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.post(
    "/",
    response_model=DesignFileTypeResponse,
)
def create_file_type(
    data: DesignFileTypeCreate,
    service: DesignFileTypeService = Depends(
        get_design_filetype_service
    ),
):
    return service.create_file_type(data)


@router.put(
    "/{design_file_type_id}",
    response_model=DesignFileTypeResponse,
)
def update_file_type(
    design_file_type_id: int,
    data: DesignFileTypeUpdate,
    service: DesignFileTypeService = Depends(
        get_design_filetype_service
    ),
):
    try:
        return service.update_file_type(
            design_file_type_id,
            data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.patch(
    "/{design_file_type_id}/deactivate",
    response_model=DesignFileTypeResponse,
)
def deactivate_file_type(
    design_file_type_id: int,
    service: DesignFileTypeService = Depends(
        get_design_filetype_service
    ),
):
    try:
        return service.deactivate_file_type(
            design_file_type_id
        )
    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )