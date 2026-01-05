from fastapi import FastAPI
from strawberry.asgi import GraphQL
from app.graphql_schema import schema
from app.config import connect_to_mongo, close_mongo_connection
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    await connect_to_mongo("mongodb://localhost:27017")
    print(" Application started")

    yield  # ⬅️ aplikacija radi između startup i shutdown

    # SHUTDOWN
    await close_mongo_connection()
    print(" Application stopped")


app = FastAPI(lifespan=lifespan)

# GraphQL endpoint
graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
