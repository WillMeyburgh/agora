from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from agora_api.database.db import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    discussion_id = Column(Integer, ForeignKey("discussions.id"))
    agent_id = Column(Integer, ForeignKey("agents.id"))
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    discussion = relationship("Discussion")
    agent = relationship("Agent")
