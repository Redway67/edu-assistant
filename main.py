from edu_assistant.assistant import create_response

# Prepare prompt for LLM
INPUT_PROMPT = "Кто победил, печенеги или половцы?"

# Call assistant
response = create_response(
    llm_key="ollama",
    role="history_tutor",
    template="tutor_quick_answer",
    prompt=INPUT_PROMPT,
)

print(response)
