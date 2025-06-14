import os
from agora_api.llm.llm_client import LLMClient
from google import genai


class GoogleGeminiLLMClient(LLMClient):
    def __init__(self, model: str):
        super().__init__()

        self.model = model
        self.client = genai.Client(api_key=os.environ['LLM_CLIENT_GOOGLE_GEMINI_API_KEY'])

    async def generate_text(self, prompt: str):
        return (await self.client.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt]
        )).text