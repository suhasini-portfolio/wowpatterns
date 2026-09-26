from app.models.design_filetype import DesignFileType
from app.repositories.design_filetype_repository import DesignFileTypeRepository
from app.schemas.design_filetype import (
    DesignFileTypeCreate,
    DesignFileTypeUpdate,
)


class DesignFileTypeService:
    def __init__(self, repository: DesignFileTypeRepository):
        self.repository = repository

    def create_file_type(self, data: DesignFileTypeCreate):
        file_type = DesignFileType(
            design_file_type=data.design_file_type,
            is_active=data.is_active,
        )

        return self.repository.create(file_type)

    def get_file_type(self, design_file_type_id: int):
        file_type = self.repository.get_by_id(design_file_type_id)

        if not file_type:
            raise ValueError("No design file type exists")

        return file_type

    def get_file_types(self, active_only: bool = True):
        return self.repository.get_all(active_only)

    def update_file_type(
        self,
        design_file_type_id: int,
        data: DesignFileTypeUpdate,
    ):
        file_type = self.repository.get_by_id(design_file_type_id)

        if not file_type:
            raise ValueError("No design file type exists")

        update_data = data.model_dump(exclude_unset=True)

        return self.repository.update(
            file_type,
            update_data,
        )

    def deactivate_file_type(self, design_file_type_id: int):
        file_type = self.repository.get_by_id(design_file_type_id)

        if not file_type:
            raise ValueError("No design file type exists")

        return self.repository.deactivate(file_type)