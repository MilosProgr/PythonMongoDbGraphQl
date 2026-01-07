import strawberry
from typing import List
from app.resolvers import get_users,create_user,find_user,update_user_service,delete_user,search_user_resolver
from app.graphql_types import UserType

@strawberry.type
class Query:
    users: List[UserType] = strawberry.field(resolver=get_users)
    user: UserType = strawberry.field(resolver=find_user)
    search_user: List[UserType] = strawberry.field(resolver=search_user_resolver)


@strawberry.type
class Mutation:
    create_user: UserType = strawberry.mutation(resolver=create_user)
    update_user: UserType = strawberry.mutation(resolver=update_user_service)
    delete_user: UserType = strawberry.mutation(resolver=delete_user)
    


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)