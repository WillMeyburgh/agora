from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from agora_api.database.models import Discussion, Message
from agora_api.database.crud.agent import get_agent
from agora_api.llm.llm_client import LLMClient
from agora_api.llm.google_gemini_llm_client import GoogleGeminiLLMClient
from agora_api.database import db # Import db module
from sqlalchemy.orm import Session

router = APIRouter()

async def run_discussion_in_background(
    discussion_id: int,
    agent_ids: List[int],
    topic: str,
    session: Session # Use Annotated with Session
):
    llm_client: LLMClient = LLMClient.get()
    messages = []
    
    # Re-fetch agents within the background task's session
    agents = []
    for agent_id in agent_ids:
        agent = get_agent(session, agent_id)
        if not agent:
            # This should ideally not happen if agents were validated in the main endpoint
            print(f"Error: Agent with ID {agent_id} not found in background task.")
            return
        agents.append(agent)

    num_agents = len(agents)

    for i in range(4):  # 4 turns of conversation
        current_agent_index = i % num_agents
        current_agent = agents[current_agent_index]

        prompt = f"Topic: {topic}\n"
        prompt += f"Your persona: {current_agent.persona_prompt}\n"
        if messages:
            prompt += "Conversation so far:\n" + "\n".join([f"{msg.agent.name}: {msg.content}" for msg in messages])
        prompt += f"\n{current_agent.name}'s turn to speak. What do you say?"

        response_content = await llm_client.generate_text(prompt)

        message = Message(
            discussion_id=discussion_id,
            agent_id=current_agent.id,
            content=response_content
        )
        session.add(message)
        session.commit()
        session.refresh(message)
        messages.append(message)

@router.post("/discussions/start")
def start_discussion(
    topic: str,
    agent_ids: List[int],
    background_tasks: BackgroundTasks,
    session = Depends(db.get_db),
):
    if len(agent_ids) < 2:
        raise HTTPException(status_code=400, detail="At least two agent IDs are required for a discussion.")

    # Validate agents before creating discussion
    for agent_id in agent_ids:
        agent = get_agent(session, agent_id)
        if not agent:
            raise HTTPException(status_code=404, detail=f"Agent with ID {agent_id} not found")

    discussion = Discussion(topic=topic)
    session.add(discussion)
    session.commit()
    session.refresh(discussion)

    # Pass a new session to the background task to avoid session conflicts
    # This requires a new session to be created for the background task
    # For simplicity, I'll pass the discussion_id and agent_ids, and let the background task get its own session.
    background_tasks.add_task(run_discussion_in_background, discussion.id, agent_ids, topic, next(db.get_db()))

    return {"message": "Discussion started in the background", "discussion_id": discussion.id}
