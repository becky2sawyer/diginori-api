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

description = """
### The world of **dreams**, **love**, and **coding**. β
### To Infinity, and Beyond! π

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
        {"name": "Aiden", "meaning": "μμ λΆ"},
        {"name": "Benjamin", "meaning": "μ³μ, κ°μ₯ μμ€ν μλ€"},
        {"name": "Chistopher", "meaning": "κ·Έλ¦¬μ€λλ₯Ό μ§μ΄μ§λ μ"},
        {"name": "Danial", "meaning": "μ μ λμ μ¬νμ"},
        {"name": "Ethan", "meaning": "μμ§κ° κ³§μ, κ°ν, μκΈ°λ§μ μκΉμ΄ κ°ν"},
        {"name": "Francisco", "meaning": "νλμ€μμ μ¨"},
        {"name": "Gabriel", "meaning": "μ μ λμ νμ μμ²"},
        {"name": "Henry", "meaning": "μμ£Ό, μ§μ μ£ΌμΈ"},
        {"name": "Ian", "meaning": "μλΉλ‘μ΄ μ "},
        {"name": "Jayden", "meaning": "κ°μ¬ ν  μ€ μλ"},
        {"name": "Kevin", "meaning": "μ¨ννλ©΄μ κ°κ΅¬μ₯μ΄ λλ"},
        {"name": "Liam", "meaning": "λ°λμ μ©μ¬"},
        {"name": "Matthew", "meaning": "μ μ μ λ¬Ό"},
        {"name": "Noah", "meaning": "ν΄μμ²"},
        {"name": "Oliver", "meaning": "μ¬λ¦¬λΈ λλ¬΄, μν μ μ¬"},
        {"name": "Parker", "meaning": "κ³΅μ μ§ν€λ μ"},
        {"name": "Quincy", "meaning": "λΌν΄μ΄λ‘ β5βλ₯Ό μλ―Έ"},
        {"name": "Ryan", "meaning": "μμ μ"},
        {"name": "Samuel", "meaning": "νλλμ΄ μ°Ύλμ"},
        {"name": "Thomas", "meaning": "μλ₯μ΄, μ’μ μΉκ΅¬λ λ»"},
        {"name": "Ucal", "meaning": "νμ΄ μΌ"},
        {"name": "Vincent", "meaning": "μ λ³΅μ"},
        {"name": "William", "meaning": "κ°ν μμ§μ μ©μ¬, ννμ μΉνΈμ"},
        {"name": "Xavier", "meaning": "μ μ§, κ΅¬μ‘°μ"},
        {"name": "Yadiel", "meaning": "μ¨λ₯Ό λΏλ¦°λ€"},
        {"name": "Xavier", "meaning": "μ μ§, κ΅¬μ‘°μ"},
        {"name": "Zachary", "meaning": "μ μ κΈ°μ΅νκ³  μλ€"},
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
