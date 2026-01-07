# services/user_service.py
import strawberry
from strawberry.types import unset
from app.graphql_types import UserUpdateInput
from app.models import User,CreateUserModel
from app.repo import get_all_users, search_user,create_user,delete_user,get_user_by_id,update_user
from pydantic import ValidationError

async def list_users() -> list[User]:
    users = await get_all_users()

    result = []
    for u in users:
        result.append(
            User(
                id=u["_id"],
                name=u["name"],
                email=u["email"],
                age=u["age"]
            )
        )

    return result

async def get_user(id: str) -> User:
    user = await get_user_by_id(id)
    if not user:
        raise Exception("User not found")
    if len(user["name"]) > 4:
        print("Ime je dugacko yay")

    return User(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        age=user["age"]
    )
async def add_user(data: dict) -> User:
    try:
        validated = CreateUserModel(**data)
    except ValidationError as e:
        raise Exception(e.errors())

    result = await create_user(validated.model_dump())

    return User(
        id=str(result.inserted_id),
        name=validated.name,
        email=validated.email,
        age=validated.age
    )

async def update_user_service(
    id: str,
    input: "UserUpdateInput"
) -> "User":
    # Convert to dict
    update_data: dict = strawberry.asdict(input)
    
    # Filter out fields that are UNSET
    update_data = {k: v for k, v in update_data.items() if v is not strawberry.UNSET}

    if not update_data:
        raise Exception("No fields provided for update")

    result = await update_user(id, update_data)

    if not result:
        raise Exception("User not found")

    return User(
        id=str(result["_id"]),
        name=result["name"],
        email=result["email"],
        age=result["age"]
    )
async def delete_user_service(self,id:str) -> User:
    user = await delete_user(self=self,id=id)
    print("s",user)
    if not user:
        raise Exception("User not found")
    return User(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        age=user["age"]
    )
    # return {
    #     "id": str(user["_id"]),
    #     "name": user["name"],
    #     "email": user["email"],
    #     "age": user["age"]
    # }

async def search_user_service(input:str) -> list[User]:
    users = await search_user(input=input)
    return [User(
        id= str(user["_id"]),
        name=user["name"],
        email=user["email"],
        age=user["age"]
    )
        for user in users
    ]



