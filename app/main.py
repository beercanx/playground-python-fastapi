from fastapi import FastAPI
from .hello import hello

application = FastAPI()
application.include_router(hello.router)


@application.get("/", tags=["root"])
async def root():
    return {"message": "Hello, World!"}
