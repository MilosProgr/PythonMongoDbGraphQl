# graphql/resolvers.py
from app.graphql_types import UserType, UserInput, UserUpdateInput
from app.service import list_users, add_user,update_user_service,delete_user_service,get_user,search_user_service

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

async def find_user(id: str) -> UserType:
    user = await get_user(id)

    return UserType(
        id=user.id,
        name=user.name,
        email=user.email,
        age=user.age
    )


async def update_user_res(self,id:str,input: UserUpdateInput) -> UserType:
    user = await update_user_service(self, id, input.__dict__)

    return UserType(
        id=str(user.id),
        name=user.name,
        email=user.email,
        age=user.age
    )


async def create_user(input: UserInput) -> UserType:
    user = await add_user(input.__dict__)
    return UserType(
        id=str(user.id),
        name=user.name,
        email=user.email,
        age=user.age
    )

async def delete_user(self, id:str) -> UserType:
    user = await delete_user_service(self=self,id=id)
    return UserType(
        id=str(user.id),
        name=user.name,
        email=user.email,
        age=user.age
    )

async def search_user_resolver(input:str) -> list[UserType]:
    user = await search_user_service(input=input)
    return[
        UserType(
        id=str(u.id),
        name=u.name,
        email=u.email,
        age=u.age
    )
    for u in user
    ] 
        
