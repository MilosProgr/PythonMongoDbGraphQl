# services/user_service.py
from models import User
from repo import get_all_users, create_user

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


async def add_user(data: dict):
    result = await create_user(data)
    return {
        "id": result.inserted_id,
        **data
    }
