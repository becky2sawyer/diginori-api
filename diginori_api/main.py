import strawberry
from fastapi import FastAPI, Query
from pydantic import Required
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from diginori_api.internal.lotto import predict_lotto_number
from diginori_api.database.crud import select, insert_config, insert_name_card


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

description = """
### The world of **dreams**, **love**, and **coding**. ☕
### To Infinity, and Beyond! 🚀

![diginori](https://diginori.com/diginori-2-ink.png)

### You will be able to:

* **Get Lotto Numbering**.
* **Get your own satellite coordinates** (_not implemented_).

### GraphQL
- [digiNORI_GraphQL](/graphql)

----
"""
app = FastAPI(
    title="digiNORI API",
    description=description,
    version="0.3.0",
    contact={
        "name": "Visit the digiNORI.com",
        "url": "https://diginori.com",
        # "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

origins = [
    "https://diginori.com",
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


@app.get("/get_satellite_coordinates")
async def get_satellite_coordinates():
    """get your own satellite coordinates DUMMY

    - https://www.celestis.com/resources/faq/what-are-the-azimuth-and-elevation-of-a-satellite/
    - https://www.sciencedirect.com/topics/physics-and-astronomy/elevation-angle
    - https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=karipr&logNo=221347805831
    - elevation - height
    - azimuth
    - angle - ceiling distance
    - angular_speed

    """
    import random
    return {
        "elevation": random.random(),
        "azimuth": random.random(),
        "angle": random.random(),
        "angular_speed": random.random(),
    }


@app.get("/m2o/dag")
async def get_satellite_coordinates():
    return [
        {"name": "ingest_abc_def_1", "cron": "* 1 * * *"},
        {"name": "ingest_abc_def_2", "cron": "* 2 * * *"},
       
    ]


@app.get("/db/test")
async def select_test():
    r = select("SELECT id,name,config from test order by id desc")
    return r


@app.put("/db/insert")
async def insert_conf(id: int, name: str, config: str):
    results = {"id": id, "name": name, "config": config}
    insert_config(id=id, name=name, config=config)
    return results


@app.put("/db/add_name_card")
async def add_name_card(name: str, age: int):
    results = {"name": name, "age": age}
    insert_name_card(name=name, age=age)
    return results


@app.get("/db/name_card")
async def select_test():
    r = select("SELECT name, age from name_card order by age desc")
    return r

