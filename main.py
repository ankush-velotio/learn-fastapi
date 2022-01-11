from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    """This function return hello world"""

    return {"message": "Hello World"}


# Fixed path routes must be declared before the routes with path parameters
# to avoid the conflicts
@app.get("/hello/me")
async def say_hello_to_me():
    """This function says hello to current user"""

    return {"message": "Hello current user"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """This function says hello"""

    return {"message": f"Hello {name}"}


class User(BaseModel):
    name: str
    email: str


@app.post("/user")
async def create_user(user: User):
    """This function creates new user"""

    return user
