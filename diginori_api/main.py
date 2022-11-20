import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from diginori_api.internal.lotto import predict_lotto_number


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


@app.get("/meaning_of_names")
async def meaning_of_names():
    """the meaning of a name

    - https://themomstory.co.kr/%EB%82%A8%EC%9E%90%EC%98%81%EC%96%B4%EC%9D%B4%EB%A6%84/

    Returns:
        _type_: [{name, meaning}]
    """
    return [
        {"name": "Aiden", "meaning": "작은 불"},
        {"name": "Benjamin", "meaning": "옳은, 가장 소중한 아들"},
        {"name": "Chistopher", "meaning": "그리스도를 짊어지는 자"},
        {"name": "Danial", "meaning": "신은 나의 심판자"},
        {"name": "Ethan", "meaning": "의지가 곧은, 강한, 자기만의 색깔이 강한"},
        {"name": "Francisco", "meaning": "프랑스에서 온"},
        {"name": "Gabriel", "meaning": "신은 나의 힘의 원천"},
        {"name": "Henry", "meaning": "영주, 집의 주인"},
        {"name": "Ian", "meaning": "자비로운 신"},
        {"name": "Jayden", "meaning": "감사 할 줄 아는"},
        {"name": "Kevin", "meaning": "온화하면서 개구장이 느낌"},
        {"name": "Liam", "meaning": "바람의 용사"},
        {"name": "Matthew", "meaning": "신의 선물"},
        {"name": "Noah", "meaning": "휴식처"},
        {"name": "Oliver", "meaning": "올리브 나무, 엘프 전사"},
        {"name": "Parker", "meaning": "공원 지키는 자"},
        {"name": "Quincy", "meaning": "라틴어로 ‘5’를 의미"},
        {"name": "Ryan", "meaning": "작은 왕"},
        {"name": "Samuel", "meaning": "하나님이 찾는자"},
        {"name": "Thomas", "meaning": "쌍둥이, 좋은 친구란 뜻"},
        {"name": "Ucal", "meaning": "힘이 센"},
        {"name": "Vincent", "meaning": "정복자"},
        {"name": "William", "meaning": "강한 의지의 용사, 평화의 옹호자"},
        {"name": "Xavier", "meaning": "새 집, 구조자"},
        {"name": "Yadiel", "meaning": "씨를 뿌린다"},
        {"name": "Xavier", "meaning": "새 집, 구조자"},
        {"name": "Zachary", "meaning": "신은 기억하고 있다"},
    ]


@app.get("/predict_lotto")
async def predict_lotto():
    """predict lotto number 6/45

    Returns:
        _type_: [1,2,3,4,5,45]
    """
    return predict_lotto_number()
