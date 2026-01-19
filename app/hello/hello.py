from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["hello"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
