from app.config import db
from app.graphql_types import UserType, UserInput

async def get_users() -> list[UserType]:
    users = await db.users.find().to_list(100)

    result = []
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]
        result.append(UserType(**user))

    return result


async def create_user(input: UserInput) -> UserType:
    data = input.__dict__
    result = await db.users.insert_one(data)

    return UserType(
        id=str(result.inserted_id),
        **data
    )
