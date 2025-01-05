from pydantic import BaseModel, Field


class RecommendationsSchema(BaseModel):
    id: int = Field(..., ge=1)
    user_id: int = Field(..., ge=1)
    item_id: int = Field(..., ge=1)

    class Config:
        from_attributes = True


class RecommendationsRequestSchema(BaseModel):
    user_id: int = Field(..., ge=1)

    class Config:
        from_attributes = True
