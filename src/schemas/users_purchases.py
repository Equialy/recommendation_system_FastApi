from datetime import date, datetime

from pydantic import BaseModel, Field


class UsersPurchasesSchema(BaseModel):
    id: int = Field(..., ge=1)
    user_id: int = Field(..., ge=1 )
    item_id: int = Field(..., ge=1 )
    category: str = Field(..., min_length=1, max_length=255)
    purchase_date: datetime

    class Config:
        from_attributes = True


class CartSchema(BaseModel):
    item_id: int = Field(..., ge=1)
    category: str = Field(..., min_length=1, max_length=255)

    class Config:
        from_attributes = True

class UsersPurchasesSchemaAdd(BaseModel):
    user_id: int = Field(..., ge=1)
    cart: list[CartSchema]


    class Config:
        from_attributes = True