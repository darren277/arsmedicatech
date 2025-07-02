""""""
import enum
import json
from openai import OpenAI


DEFAULT_SYSTEM_PROMPT = """
You are a clinical assistant that helps healthcare providers with patient care tasks.
You can answer questions, provide information, and assist with various healthcare-related tasks.
Your responses should be accurate, concise, and helpful.
"""

class LLMModel(enum.Enum):
    """Enumeration of supported LLM models."""
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4_1_NANO = "gpt-4.1-nano"

    def __str__(self):
        return self.value

def process_tool_call(tool_call, tool_dict):
    function_name = tool_call.function.name
    arguments = json.loads(tool_call.function.arguments)

    tool_function = tool_dict[function_name]
    tool_result = tool_function(**arguments)

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

    def add_tool(self, tool, tool_def):
        """Add a tool to the agent."""
        if not callable(tool):
            raise ValueError("Tool must be a callable function.")
        self.tool_definitions.append(tool_def)
        self.tool_func_dict[tool.__name__] = tool

    def fetch_history(self):
        """ Fetch history from database. """
        # TODO.
        return [{"role": "system", "content": "You are a helpful assistant."}]

    def complete(self, prompt: str or None, **kwargs):
        if prompt:
            self.message_history.append({"role": "user", "content": prompt})

        completion = self.client.chat.completions.create(
            model=self.model.value,
            messages=self.message_history,
        )

        top_choice = completion.choices[0].message

        # process tool calls if any...
        tool_calls = top_choice.message.tool_calls
        print(top_choice)

        if tool_calls:
            self.process_tool_calls(tool_calls)

            # Recurse to handle tool calls
            self.complete(None, **kwargs)

    def process_tool_calls(self, tool_calls):
        for tool_call in tool_calls:
            result = process_tool_call(tool_call, self.tool_func_dict)
            self.message_history.append(result)

