import os
from typing import List

from llama_index.core.agent import AgentRunner
from llama_index.core.callbacks import CallbackManager
from llama_index.core.tools import BaseTool
from llama_index.llms.openai import OpenAI

def get_chat_engine(params=None, event_handlers=None, **kwargs):
    system_prompt = os.getenv("SYSTEM_PROMPT")
    tools: List[BaseTool] = []
    callback_manager = CallbackManager(handlers=event_handlers or [])

    llm_model = os.getenv("LLM_MODEL", "gpt-4o-mini")
    llm_temperature = os.getenv("LLM_TEMPERATURE", "0")
    llm_api_key = os.getenv("OPENAI_API_KEY", "")
    llm = OpenAI(
        model=llm_model,
        temperature=int(llm_temperature),
        api_key=llm_api_key,
    )

    return AgentRunner.from_llm(
        llm=llm,
        tools=tools,
        system_prompt=system_prompt,
        callback_manager=callback_manager,
        verbose=True,
    )
