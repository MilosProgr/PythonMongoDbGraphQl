import strawberry
from typing import List
from resolvers import get_users,create_user
from graphql_types import UserType

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