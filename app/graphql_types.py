import strawberry
from typing import List


@strawberry.type
class UserType:
    id: str
    name: str
    email: str
    age: int

@strawberry.input
class UserInput:
    name: str
    email: str
    age: int