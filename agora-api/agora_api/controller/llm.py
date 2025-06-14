from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from agora_api.llm.llm_client import LLMClient

router = APIRouter()

class GenerateTestRequest(BaseModel):
    model: Optional[str] = None
    prompt: str

@router.post("/llm/generate_text")
async def generate_text_endpoint(request: GenerateTestRequest):
    llm_client = LLMClient.get(request.model)
    generated_text = await llm_client.generate_text(request.prompt)
    return {"generated_text": generated_text}
