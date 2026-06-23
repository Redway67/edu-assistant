from dotenv import load_dotenv

from edu_assistant.config import Config
from edu_assistant.llm_client import get_llm_client

# Load environment variables from .env file
load_dotenv()

# Prepare prompt for LLM
INPUT_PROMPT = "Кто ты?"

# Read config from YAML file
config = Config.from_yaml_file("config.yml")
llm_config = config.llms["api"]

# Create llm_client providing llm_config from config
llm_client = get_llm_client(llm_config=llm_config)

# Call llm_client Responses API with input prompt
# Docs: https://developers.openai.com/api/reference/resources/responses/methods/create
response = llm_client.responses.create(
    model=llm_config.model,
    input=INPUT_PROMPT,
    max_output_tokens=llm_config.max_output_tokens,
)

# Print the result (output_text field)
print(response.output_text)
