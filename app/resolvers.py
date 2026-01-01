# graphql/resolvers.py
from graphql_types import UserType, UserInput
from service import list_users, add_user

async def get_users() -> list[UserType]:
    users = await list_users()
    return [
        UserType(
            id=str(u.id),
            name=u.name,
            email=u.email,
            age=u.age
            
        )
        for u in users
        
    ]


async def create_user(input: UserInput) -> UserType:
    user = await add_user(input.__dict__)
    return UserType(
        id=str(user["id"]),
        name=user["name"],
        email=user["email"],
        age=user["age"]
    )
