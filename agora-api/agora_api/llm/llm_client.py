from abc import ABC, abstractmethod
import os
from typing import List, Optional


class LLMClient(ABC):
    @abstractmethod
    async def generate_text(self, prompt: str):
        pass

    @classmethod
    def get(cls, model:Optional[str]=None):
        if model is None:
            model = os.environ['LLM_CLIENT_DEFAULT_MODEL']
        provider, provider_model = tuple(model.split(':'))

        if provider == 'google-gemini':
            from .google_gemini_llm_client import GoogleGeminiLLMClient
            return GoogleGeminiLLMClient(provider_model)
        else:
            raise ValueError(f"Invalid Provider {provider} ({model})")
