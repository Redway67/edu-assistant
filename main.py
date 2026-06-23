from dotenv import load_dotenv

from edu_assistant.config import Config
from edu_assistant.llm_client import get_llm_client

INPUT_PROMPT = "Почему началась Первая мировая война?"

load_dotenv()

config = Config.from_yaml_file("config.yml")
llm_config = config.llms["ollama"]

system_prompt = config.render_system_instructions(
    role="history_tutor",
    template="tutor_quick_answer",
)
llm_client = get_llm_client(llm_config)

response = llm_client.responses.create(
    model=llm_config.model,
    instructions=system_prompt,
    input=INPUT_PROMPT,
    max_output_tokens=llm_config.max_output_tokens,
)

print(response.output_text)
