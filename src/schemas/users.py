from pydantic import BaseModel, Field


class UsersSchema(BaseModel):
    id: int = Field(..., ge=1 )
    username: str = Field(..., min_length=1, max_length=255 )


    class Config:
        from_attributes = True



class UsersSchemaAdd(BaseModel):
    username: str = Field(..., min_length=1, max_length=255)
    class Config:
        from_attributes = True
