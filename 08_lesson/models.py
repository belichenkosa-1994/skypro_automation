from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class ProjectCreateRequest(BaseModel):
    """Модель для создания проекта."""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class ProjectUpdateRequest(BaseModel):
    """Модель для обновления проекта."""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class ProjectResponse(BaseModel):
    """Модель ответа API для проекта."""
    id: str
    title: str
    description: Optional[str]
    companyId: str
    createdAt: datetime
    updatedAt: datetime
    archive: bool
    
    class Config:
        """Конфигурация Pydantic модели."""
        allow_population_by_field_name = True