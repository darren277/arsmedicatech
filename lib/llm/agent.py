"""
LLM Agent Module
"""
import enum
import json
from typing import Callable, Dict, List

import openai
from openai import OpenAI
from openai.types.beta.threads.runs import ToolCall

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
    """
    Enumeration of supported LLM models.
    """
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"

    def __str__(self) -> str:
        return self.value

async def process_tool_call(
        tool_call: ToolCall,
        tool_dict: Dict[str, Callable],
        session_id: str = None
    ) -> Dict[str, str]:
    """
    Process a tool call from the LLM and execute the corresponding function.
    :param tool_call: ToolCall object containing the function name and arguments.
    :param tool_dict: Dictionary mapping function names to callable functions.
    :param session_id: Optional session ID for tools that require it.
    :return: Dict containing the role, function name, and result content.
    """
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
    """
    An agent that interacts with an LLM to perform tasks using tools.
    """
    def __init__(
            self,
            custom_llm_endpoint: str = None,
            model: LLMModel = LLMModel.GPT_4_1_NANO,
            api_key: str = None,
            system_prompt: str = DEFAULT_SYSTEM_PROMPT,
            **params: Dict[str, str]  # Additional parameters for the agent (e.g., temperature, max_tokens, etc.
    ) -> None:
        """
        Initialize the LLMAgent with the given parameters.
        :param custom_llm_endpoint: Endpoint for a custom LLM service (if any).
        :param model: LLMModel enum value representing the model to use.
        :param api_key: API key for accessing the LLM service.
        :param system_prompt: System prompt to set the context for the agent.
        :param params: Additional parameters for the agent, such as temperature, max_tokens, etc.
        :return: None
        """
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

    def add_tool(self, tool_name: str, tool: Callable, tool_def: ToolDefinition) -> None:
        """
        Add a tool to the agent.
        :param tool_name: Name of the tool to add.
        :param tool: Callable function that implements the tool's functionality.
        :param tool_def: Tool definition containing metadata about the tool.
        :return: None
        """
        if not callable(tool):
            raise ValueError("Tool must be a callable function.")
        self.tool_definitions.append(tool_def)
        self.tool_func_dict[tool_name] = tool

    def fetch_history(self) -> list:
        """
        Fetch history from database.
        This method should be overridden to fetch conversation history from a database or other storage.
        :return: List of message history, starting with the system prompt.
        """
        # TODO.
        return [{"role": "system", "content": self.system_prompt}]

    def to_dict(self) -> Dict[str, str]:
        """
        Serialize the agent state to a dictionary for Flask session storage.
        :return: Dictionary containing the agent's state.
        """
        return {
            'message_history': self.message_history,
            'model': self.model.value,
            'system_prompt': self.system_prompt,
            'params': self.params
        }

    def reset_conversation(self) -> None:
        """
        Reset the conversation history while keeping system prompt.
        This method clears the message history but retains the system prompt.
        :return: None
        """
        self.message_history = [{"role": "system", "content": self.system_prompt}]

    @classmethod
    def from_dict(
            cls,
            data: Dict[str, str],
            api_key: str = None,
            tool_definitions: List[ToolDefinition] = None,
            tool_func_dict: Dict[str, Callable] = None
    ) -> 'LLMAgent':
        """
        Create an agent instance from serialized data.
        :param data: Dictionary containing serialized agent state.
        :param api_key: API key for accessing the LLM service.
        :param tool_definitions: List of tool definitions to restore.
        :param tool_func_dict: Dictionary mapping tool names to their callable functions.
        :return: An instance of LLMAgent with restored state.
        """
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
    async def from_mcp(cls, mcp_url: str, api_key: str, **kwargs: Dict[str, str]) -> 'LLMAgent':
        """
        Build an LLMAgent that proxies every tool call to the given MCP server.
        :param mcp_url: URL of the MCP server to fetch tool definitions from.
        :param api_key: API key for accessing the LLM service.
        :param kwargs: Additional parameters for the agent.
        :return: An instance of LLMAgent with tools fetched from the MCP server.
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

    async def complete(self, prompt: str or None, **kwargs: Dict[str, str]) -> Dict[str, str]:
        """
        Complete a prompt using the LLM, processing any tool calls if necessary.
        :param prompt: The user prompt to send to the LLM. If None, uses the existing message history.
        :param kwargs: Additional parameters for the LLM completion (e.g., temperature, max_tokens).
        :return: Dict containing the LLM's response.
        """
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

    async def process_tool_calls(self, tool_calls: List[ToolCall]) -> None:
        """
        Process a list of tool calls by executing the corresponding functions.
        :param tool_calls: List of ToolCall objects to process.
        :return: None
        """
        api_key = get_encryption_service().encrypt_api_key(self.api_key)

        logger.debug("Sending request to OpenAI with model:", self.model.value)
        logger.debug("API Key:", api_key)

        if not api_key: raise ValueError("API key is required for LLM access.")

        for tool_call in tool_calls:
            result = await process_tool_call(tool_call, self.tool_func_dict, session_id=api_key)
            self.message_history.append(result)

