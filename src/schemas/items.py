

from pydantic import BaseModel, Field


class ItemsSchema(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1, max_length=255)
    category: str = Field(..., min_length=1, max_length=255)

    class Config:
        from_attributes = True

class ItemsSchemaAdd(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    category: str = Field(..., min_length=1, max_length=255)

    class Config:
        from_attributes = True