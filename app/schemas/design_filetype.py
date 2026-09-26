from pydantic import BaseModel, ConfigDict, Field


class DesignFileTypeCreate(BaseModel):
    design_file_type: str = Field(..., max_length=20)
    is_active: bool = True


class DesignFileTypeUpdate(BaseModel):
    design_file_type: str | None = Field(default=None, max_length=20)
    is_active: bool | None = None


class DesignFileTypeResponse(BaseModel):
    design_file_type_id: int
    design_file_type: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)