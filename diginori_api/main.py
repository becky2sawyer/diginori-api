import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware

@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:9000",
    "https://diginori.com",
    "https://www.diginori.com",
    "https://diginori-universe.github.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


@app.get("/")
async def root():
    return {"message": "digiNORI"}
