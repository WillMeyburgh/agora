from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel

from agora_api.database.agent import Agent # Import SQLAlchemy model

# Pydantic Models
class AgentBase(BaseModel):
    name: str
    persona_prompt: str

class AgentCreate(AgentBase):
    pass

class AgentUpdate(AgentBase):
    name: Optional[str] = None
    persona_prompt: Optional[str] = None

class AgentSchema(AgentBase): # Renamed to AgentSchema to avoid conflict with SQLAlchemy Agent
    id: int

    class Config:
        orm_mode = True

# CRUD Operations
def get_agent(db_session: Session, agent_id: int):
    return db_session.query(Agent).filter(Agent.id == agent_id).first()

def get_agents(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(Agent).offset(skip).limit(limit).all()

def create_agent(db_session: Session, agent: AgentCreate):
    db_agent = Agent(name=agent.name, persona_prompt=agent.persona_prompt)
    db_session.add(db_agent)
    db_session.commit()
    db_session.refresh(db_agent)
    return db_agent

def update_agent(db_session: Session, agent_id: int, agent: AgentUpdate):
    db_agent = db_session.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent:
        for var, value in vars(agent).items():
            if value is not None:
                setattr(db_agent, var, value)
        db_session.add(db_agent)
        db_session.commit()
        db_session.refresh(db_agent)
    return db_agent

def delete_agent(db_session: Session, agent_id: int):
    db_agent = db_session.query(Agent).filter(Agent.id == agent_id).first()
    if db_agent:
        db_session.delete(db_agent)
        db_session.commit()
        return True
    return False
