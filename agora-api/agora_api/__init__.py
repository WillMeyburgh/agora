from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from .database.db import engine, Base
from .controller import index
from .database import models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(index.router)
