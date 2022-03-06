from fastapi import APIRouter
from enum import Enum

router = APIRouter(tags=["lesson1"])


class Names(str, Enum):
    first = "Kirill"
    second = "Denis"


@router.get("/")
def home():
    return {"message": "Wellcome home"}


@router.get("/name/{name}")
def get_name(name: str):
    return {"name": name}


@router.get('/name/get_name/{name}')
def get_name_from_list(name: Names):
    if name == Names.first:
        return {"message": "This name is your teacher name"}
    elif name == Names.second:
        return {"message": "This pupil does not exist"}
    return {"message": "Wrong name"}

    