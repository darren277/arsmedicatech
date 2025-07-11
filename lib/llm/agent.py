""""""
import enum
import json
from typing import Callable

from openai import OpenAI

from lib.llm.mcp_tools import fetch_mcp_tool_defs
from lib.services.encryption import get_encryption_service

from settings import logger


DEFAULT_SYSTEM_PROMPT = """
You are a clinical assistant that helps healthcare providers with patient care tasks.
You can answer questions, provide information, and assist with various healthcare-related tasks.
Your responses should be accurate, concise, and helpful.
"""

tools_with_keys = ['rag']

ToolDefinition = dict

class LLMModel(enum.Enum):
    """Enumeration of supported LLM models."""
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"

    def __str__(self):
        return self.value

async def process_tool_call(tool_call, tool_dict, session_id: str = None):
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    for key, val in tool_dict.items():
        logger.debug(f"Tool: {key} -> {val}") # [DEBUG] Tool: _call -> <function fetch_mcp_tool_defs.<locals>.wrap.<locals>._call at 0x7f78720b23e0>
        logger.debug(f"Function: {function_name} -> {val.__name__}") # [DEBUG] Function: rag -> _call

    tool_function = tool_dict[function_name]
    if function_name in tools_with_keys:
        tool_result = await tool_function(session_id=session_id, **arguments)
    else:
        tool_result = await tool_function(**arguments)

    result = json.dumps(tool_result)

    return {"role": "function", "name": function_name, "content": result}

class LLMAgent:
    def __init__(self, custom_llm_endpoint: str = None, model: LLMModel = LLMModel.GPT_4_1_NANO, api_key: str = None, system_prompt: str = DEFAULT_SYSTEM_PROMPT, **params):
        self.custom_llm_endpoint = custom_llm_endpoint
        self.model = model
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.params = params

        self.tool_definitions = []
        self.tool_func_dict = dict()

        self.message_history = self.fetch_history()

        if self.custom_llm_endpoint:
            # TODO...
            raise NotImplementedError("Custom LLM endpoint is not yet implemented.")
        if not self.api_key:
            raise ValueError("API key must be provided for LLM access.")

        self.client = OpenAI(api_key=self.api_key)

    def add_tool(self, tool_name: str, tool: Callable, tool_def: ToolDefinition):
        """Add a tool to the agent."""
        if not callable(tool):
            raise ValueError("Tool must be a callable function.")
        self.tool_definitions.append(tool_def)
        self.tool_func_dict[tool_name] = tool

    def fetch_history(self):
        """ Fetch history from database. """
        # TODO.
        return [{"role": "system", "content": self.system_prompt}]

    def to_dict(self):
        """Serialize the agent state to a dictionary for Flask session storage."""
        return {
            'message_history': self.message_history,
            'model': self.model.value,
            'system_prompt': self.system_prompt,
            'params': self.params
        }

    def reset_conversation(self):
        """Reset the conversation history while keeping system prompt."""
        self.message_history = [{"role": "system", "content": self.system_prompt}]

    @classmethod
    def from_dict(cls, data, api_key, tool_definitions=None, tool_func_dict=None):
        """Create an agent instance from serialized data."""
        agent = cls(
            model=LLMModel(data.get('model', LLMModel.GPT_4_1)),
            api_key=api_key,
            system_prompt=data.get('system_prompt', DEFAULT_SYSTEM_PROMPT),
            **data.get('params', {})
        )
        
        # Restore message history
        agent.message_history = data.get('message_history', [{"role": "system", "content": "You are a helpful assistant."}])
        
        # Restore tools if provided
        if tool_definitions and tool_func_dict:
            agent.tool_definitions = tool_definitions
            agent.tool_func_dict = tool_func_dict
        
        return agent

    @classmethod
    async def from_mcp(cls, mcp_url: str, api_key: str, **kwargs):
        """
        Build an LLMAgent that proxies every tool call to the given MCP server.
        """
        # 1) Discover tools from MCP
        defs, funcs = await fetch_mcp_tool_defs(mcp_url)

        # 2) Instantiate the agent
        agent = cls(api_key=api_key, **kwargs)
        for d in defs:
            name = d["function"]["name"]
            logger.debug("Adding tool:", d["function"]["name"], funcs[name], d)
            agent.add_tool(name, funcs[name], d)
        return agent

    async def complete(self, prompt: str or None, **kwargs):
        if prompt:
            self.message_history.append({"role": "user", "content": prompt})

        api_key = get_encryption_service().encrypt_api_key(self.api_key)

        logger.debug("Sending request to OpenAI with model:", self.model.value)
        logger.debug("API Key:", api_key)

        if not api_key:
            raise ValueError("API key is required for LLM access.")

        completion = self.client.chat.completions.create(
            model=self.model.value,
            messages=self.message_history,
            tools=self.tool_definitions,
            #tool_choice="auto",
            #tool_choice='required',
            extra_headers={
                "x-user-pw": api_key
            }
        )

        top_choice = completion.choices[0].message

        # process tool calls if any...
        tool_calls = top_choice.tool_calls
        logger.debug("Top choice:", top_choice)

        if tool_calls:
            await self.process_tool_calls(tool_calls)

            # Recurse to handle tool calls
            return await self.complete(None, **kwargs)
        else:
            # Add assistant response to message history
            self.message_history.append({"role": "assistant", "content": top_choice.content})

        return {"response": top_choice.content}

    async def process_tool_calls(self, tool_calls):
        api_key = get_encryption_service().encrypt_api_key(self.api_key)

        logger.debug("Sending request to OpenAI with model:", self.model.value)
        logger.debug("API Key:", api_key)

        if not api_key: raise ValueError("API key is required for LLM access.")

        for tool_call in tool_calls:
            result = await process_tool_call(tool_call, self.tool_func_dict, session_id=api_key)
            self.message_history.append(result)

