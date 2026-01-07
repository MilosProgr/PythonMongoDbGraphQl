from pydantic import BaseModel, Field,EmailStr
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field=None, config=None):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
class User(BaseModel):
    id: PyObjectId = None
    name: str
    email: str
    age: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CreateUserModel(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str = EmailStr
    age: int = Field(gt=18, lt=150)


