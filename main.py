from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """This function return hello world"""

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """This function says hello"""

    return {"message": f"Hello {name}"}
