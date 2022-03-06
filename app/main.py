from fastapi import FastAPI
from app.routes import lesson1


def get_application():
    _app = FastAPI()
    return _app

app = get_application()

app.include_router(lesson1.router)
