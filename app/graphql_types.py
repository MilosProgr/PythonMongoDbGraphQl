import strawberry
from typing import List, Optional


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

@strawberry.input
class UserUpdateInput:
    name: Optional[str] = strawberry.UNSET
    email: Optional[str] = strawberry.UNSET
    age: Optional[int] = strawberry.UNSET