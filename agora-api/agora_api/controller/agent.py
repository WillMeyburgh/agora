from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from agora_api.database import db
from agora_api.database.crud.agent import (
    AgentCreate,
    AgentUpdate,
    AgentSchema, # Import the Pydantic schema for response_model
    get_agent,
    get_agents,
    create_agent,
    update_agent,
    delete_agent
)

router = APIRouter()

@router.post("/agents/", response_model=AgentSchema)
def create_agent_endpoint(agent: AgentCreate, db_session: Session = Depends(db.get_db)):
    return create_agent(db_session=db_session, agent=agent)

@router.get("/agents/{agent_id}", response_model=AgentSchema)
def read_agent_endpoint(agent_id: int, db_session: Session = Depends(db.get_db)):
    db_agent = get_agent(db_session=db_session, agent_id=agent_id)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.get("/agents/", response_model=List[AgentSchema])
def read_agents_endpoint(skip: int = 0, limit: int = 100, db_session: Session = Depends(db.get_db)):
    agents = get_agents(db_session=db_session, skip=skip, limit=limit)
    return agents

@router.put("/agents/{agent_id}", response_model=AgentSchema)
def update_agent_endpoint(agent_id: int, agent: AgentUpdate, db_session: Session = Depends(db.get_db)):
    db_agent = update_agent(db_session=db_session, agent_id=agent_id, agent=agent)
    if db_agent is None:
        raise HTTPException(status_code=404, detail="Agent not found")
    return db_agent

@router.delete("/agents/{agent_id}")
def delete_agent_endpoint(agent_id: int, db_session: Session = Depends(db.get_db)):
    success = delete_agent(db_session=db_session, agent_id=agent_id)
    if not success:
        raise HTTPException(status_code=404, detail="Agent not found")
    return {"message": "Agent deleted successfully"}
