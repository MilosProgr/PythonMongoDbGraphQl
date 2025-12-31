import strawberry
from typing import List
from app.graphql_types import UserType
from app.resolvers import get_users, create_user

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=get_users)


@strawberry.type
class Mutation:
    create_user: UserType = strawberry.mutation(resolver=create_user)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
