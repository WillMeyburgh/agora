from sqlalchemy import Column, Integer, String
from agora_api.database.db import Base

class Discussion(Base):
    __tablename__ = "discussions"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, index=True)
