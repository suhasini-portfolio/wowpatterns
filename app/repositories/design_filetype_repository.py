from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.design_filetype import DesignFileType


class DesignFileTypeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, design_file_type_id: int):
        stmt = select(DesignFileType).where(
            DesignFileType.design_file_type_id == design_file_type_id
        )
        return self.db.scalar(stmt)

    def get_all(self, active_only: bool = True):
        stmt = select(DesignFileType)

        if active_only:
            stmt = stmt.where(
                DesignFileType.is_active.is_(True)
            )

        return self.db.scalars(stmt).all()

    def create(self, file_type: DesignFileType):
        self.db.add(file_type)
        self.db.commit()
        self.db.refresh(file_type)
        return file_type

    def update(self, file_type: DesignFileType, update_data: dict):
        for field, value in update_data.items():
            setattr(file_type, field, value)

        self.db.commit()
        self.db.refresh(file_type)
        return file_type

    def deactivate(self, file_type: DesignFileType):
        file_type.is_active = False

        self.db.commit()
        self.db.refresh(file_type)
        return file_type