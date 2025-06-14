from fastapi import APIRouter
from agora_api.controller import health

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World from controller"}
