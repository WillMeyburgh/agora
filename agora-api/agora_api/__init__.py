from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from .database.db import engine, Base
from .controller import index, health, agent, llm
from .database import models

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(index.router)
app.include_router(health.router)
app.include_router(agent.router)
app.include_router(llm.router)
