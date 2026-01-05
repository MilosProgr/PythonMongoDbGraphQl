import strawberry
from typing import List
from app.resolvers import find_user, get_users,create_user,update_user,delete_user
from app.graphql_types import UserType

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=get_users)
    find_user: UserType = strawberry.field(resolver=find_user)

@strawberry.type
class Mutation:
    create_user: UserType = strawberry.mutation(resolver=create_user)
    update_user: UserType = strawberry.mutation(resolver=update_user)
    delete_user: UserType = strawberry.mutation(resolver=delete_user)
   



schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)