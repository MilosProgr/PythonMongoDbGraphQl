# services/user_service.py
from app.models import User
from app.repo import get_all_users, create_user,update_user,delete_user,get_user_by_id
from bson import ObjectId

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

    return User(
        id=str(user["_id"]),
        name=user["name"],
        email=user["email"],
        age=user["age"]
    )

async def add_user(data: dict):
    result = await create_user(data)
    print("Rezultat: ", data)
    return {
        "id": result.inserted_id,
        **data
    }

async def update_user_service(self,id: str, input_data: dict):
    user = await update_user(self,id, input_data)

    if not user:
        raise Exception("User not found")  # kasnije možeš GraphQL error

    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"]
    }

async def delete_user_service(self,id:str):
    user = await delete_user(self=self,id=id)
    print("s",user)
    if not user:
        raise Exception("User not found")
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"]
    }