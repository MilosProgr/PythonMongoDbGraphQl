from pydantic import BaseModel
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
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